// Read a "Frames · <piece>" Section back into the layer list build-scenes.py takes.
// Run with use_figma after setting SECTION_ID. Returns JSON: one entry per panel (frames grouped
// by their "NN" prefix, states in x order), every layer with geometry, paint and text, the groups,
// and the image layers to export (node id + the path the layer expects).
const SECTION_ID = "SECTION_ID";

const slug = (s) => s.split(" / ").pop().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "layer";
const hex = (c, a = 1) => {
  const h = (v) => Math.round(v * 255).toString(16).padStart(2, "0");
  return a < 1 ? `rgba(${Math.round(c.r * 255)},${Math.round(c.g * 255)},${Math.round(c.b * 255)},${+a.toFixed(3)})` : `#${h(c.r)}${h(c.g)}${h(c.b)}`;
};
const r1 = (v) => Math.round(v * 10) / 10;

function gradient(p, w, h) {
  const [[a, b, c], [d, e, f]] = p.gradientTransform;
  const det = a * e - b * d || 1;
  const inv = (x, y) => [(e * (x - c) - b * (y - f)) / det, (-d * (x - c) + a * (y - f)) / det];
  const [x0, y0] = inv(0, 0.5), [x1, y1] = inv(1, 0.5);
  const angle = Math.round((Math.atan2((x1 - x0) * w, -(y1 - y0) * h) * 180) / Math.PI);
  const stops = p.gradientStops.map((s) => [+s.position.toFixed(3), hex(s.color, s.color.a * (p.opacity ?? 1))]);
  return p.type === "GRADIENT_RADIAL" ? { type: "radial", stops } : { type: "linear", angle, stops };
}

function paint(fills, w, h) {
  const vis = (fills === figma.mixed ? [] : fills || []).filter((p) => p.visible !== false);
  if (!vis.length) return {};
  const p = vis[vis.length - 1];
  if (p.type === "SOLID") return { fill: hex(p.color, p.opacity ?? 1) };
  if (p.type.startsWith("GRADIENT")) return { fill: gradient(p, w, h) };
  if (p.type === "IMAGE") return { image: true, hash: p.imageHash, fit: p.scaleMode === "FIT" ? "contain" : p.scaleMode === "FILL" ? "cover" : "fill" };
  return {};
}

function effects(n) {
  const o = {};
  for (const e of n.effects || []) {
    if (e.visible === false) continue;
    if (e.type === "LAYER_BLUR") o.blur = r1(e.radius);
    if (e.type === "DROP_SHADOW") o.shadow = { x: e.offset.x, y: e.offset.y, blur: e.radius, color: hex(e.color, e.color.a) };
  }
  return o;
}

const WEIGHT = { thin: 100, extralight: 200, light: 300, regular: 400, medium: 500, semibold: 600, bold: 700, extrabold: 800, black: 900 };

function textProps(n) {
  const first = (v, get) => (v === figma.mixed ? get() : v);
  const size = first(n.fontSize, () => n.getRangeFontSize(0, 1));
  const font = first(n.fontName, () => n.getRangeFontName(0, 1));
  const ls = first(n.letterSpacing, () => n.getRangeLetterSpacing(0, 1));
  const lh = first(n.lineHeight, () => n.getRangeLineHeight(0, 1));
  const base = paint(first(n.fills, () => n.getRangeFills(0, 1)), n.width, n.height).fill || "#000000";
  const segs = n.getStyledTextSegments(["fills"]);
  const accents = [];
  for (const s of segs) {
    const c = paint(s.fills, n.width, n.height).fill;
    if (c && c !== base) accents.push([s.start, s.end, c]);
  }
  const o = {
    type: "text", text: n.characters, size, font: font.family,
    weight: WEIGHT[font.style.toLowerCase().replace(/[\s-]|italic/g, "")] || 400,
    color: base, align: n.textAlignHorizontal.toLowerCase().replace("justified", "left"),
    tracking: ls.unit === "PERCENT" ? +(ls.value / 100).toFixed(3) : +(ls.value / size).toFixed(3),
    lineHeight: lh.unit === "PERCENT" ? +(lh.value / 100).toFixed(3) : lh.unit === "PIXELS" ? lh.value : 1.2,
  };
  if (accents.length) o.accents = accents;
  return o;
}

function layer(n, frame, ctx, ox, oy) {
  const bb = n.absoluteBoundingBox, fb = frame.absoluteBoundingBox;
  const L = { name: n.name, x: r1(bb.x - fb.x - ox), y: r1(bb.y - fb.y - oy), w: r1(bb.width), h: r1(bb.height) };
  if (n.opacity !== undefined && n.opacity < 1) L.opacity = +n.opacity.toFixed(3);
  if (n.visible === false) L.opacity = 0;
  Object.assign(L, effects(n));
  if (n.type === "TEXT") return Object.assign(L, textProps(n));
  if (n.type === "GROUP") {
    const leaves = (g) => g.children.flatMap((c) => (c.type === "GROUP" ? leaves(c) : [c.name]));
    ctx.groups[n.name] = { members: leaves(n) };
    return n.children.map((c) => layer(c, frame, ctx, ox, oy)).flat();
  }
  const p = paint(n.fills, bb.width, bb.height);
  if (p.image || ["BOOLEAN_OPERATION", "STAR", "POLYGON"].includes(n.type) || (n.type === "VECTOR" && !n.vectorPaths?.length)) {
    const src = `assets/screens/${ctx.panel}-${slug(n.name)}${ctx.state > 1 ? "--s" + ctx.state : ""}.png`;
    ctx.exports.push({ node: n.id, src });
    L.type = "image"; L.src = src; L.fit = p.fit || "fill";
    if (p.hash) L.imageHash = p.hash;
  } else if (n.type === "VECTOR") {
    L.type = "vector"; L.paths = n.vectorPaths.map((v) => v.data);
    if (p.fill) L.fill = p.fill;
  } else {
    L.type = n.type === "ELLIPSE" ? "ellipse" : "rect";
    if (p.fill) L.fill = p.fill;
  }
  const r = n.cornerRadius;
  if (r === figma.mixed) L.radius = [n.topLeftRadius, n.topRightRadius, n.bottomRightRadius, n.bottomLeftRadius];
  else if (r) L.radius = r;
  const st = (n.strokes || []).filter((s) => s.visible !== false && s.type === "SOLID");
  if (st.length && n.strokeWeight !== figma.mixed && n.strokeWeight > 0) {
    L.stroke = { color: hex(st[0].color, st[0].opacity ?? 1), width: n.strokeWeight };
    if (n.dashPattern?.length) L.stroke.dashed = true;
  }
  if ("children" in n && n.children.length && L.type !== "image") {
    if (n.clipsContent) L.clip = true;
    L.children = n.children.map((c) => layer(c, frame, ctx, L.x + ox, L.y + oy)).flat();
  }
  return L;
}

const section = await figma.getNodeByIdAsync(SECTION_ID);
if (!section) return { error: `no node ${SECTION_ID}` };
let page = section;
while (page.type !== "PAGE") page = page.parent;
await figma.setCurrentPageAsync(page);
const frames = section.children.filter((n) => n.type === "FRAME" && n.width > 600)
  .sort((a, b) => (Math.abs(a.y - b.y) > a.height / 2 ? a.y - b.y : a.x - b.x));
const notes = section.children.filter((n) => n.type === "TEXT");
const panels = {};
for (const f of frames) {
  const id = (f.name.match(/^(\d{2})/) || [])[1];
  if (!id) continue;
  const P = (panels[id] = panels[id] || { id, name: f.name.replace(/^\d{2}\s*/, "").split(/ [·—-] /)[0], frames: [], layers: [], groups: {}, exports: [] });
  const state = P.frames.length + 1;
  const ctx = { panel: id, state, groups: P.groups, exports: P.exports };
  const note = notes.find((t) => t.x < f.x + f.width && t.x + t.width > f.x && t.y > f.y + f.height);
  P.frames.push({ name: f.name, node: f.id, w: f.width, h: f.height, note: note ? note.characters : null });
  if (state === 1) P.background = paint(f.fills, f.width, f.height).fill;
  for (const c of f.children) {
    for (const L of [layer(c, f, ctx, 0, 0)].flat()) {
      if (state > 1) {
        const first = P.layers.find((x) => x.name === L.name && (x.state || 1) === 1);
        const bare = (x) => JSON.stringify({ ...x, state: undefined, src: undefined });
        if (first && bare(first) === bare(L)) {
          // unchanged across states: one layer, no overlay, no second export
          P.exports.splice(P.exports.findIndex((e) => e.src === L.src), L.src ? 1 : 0);
          continue;
        }
        L.state = state;
      }
      P.layers.push(L);
    }
  }
}
return { section: section.name, panels: Object.values(panels).sort((a, b) => a.id.localeCompare(b.id)) };
