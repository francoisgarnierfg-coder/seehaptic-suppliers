#!/usr/bin/env python3
"""Generate PDF – SeeHaptic supplier screening. Redesigned v2."""

import base64, sys, urllib.request

# ── Image URLs ───────────────────────────────────────────────────────────────
IMAGES = {
    "rokid":    "https://global.rokid.com/cdn/shop/files/001_6_48afc345-c913-4148-bfaf-4984f1f62ff9.jpg?v=1768896106&width=1500",
    "inmo":     "https://cdn.shopify.com/s/files/1/0551/5657/2294/files/inmoair3-img01.png?v=1756873397",
    "rayneo":   "https://heyupnow.com/cdn/shop/files/3_b3c92ad1-5bbc-4768-8889-f0d0fdb54058_600x600.png?v=1736491937",
    "xreal":    "https://resource.xreal.com/www-xreal-com/images/home/home_herosection_1S_Desktop.webp",
    "alibaba":  "https://yqintl.alicdn.com/ff6c57d40bba69f8fbb13ac4f63f35346b0d1ca0.jpeg",
    "xiaomi":   "https://roadtovrlive-5ea0.kxcdn.com/wp-content/uploads/2025/06/xiaomi-ai-glasses-hero.jpg",
    "huawei":   "https://consumer.huawei.com/dam/content/dam/huawei-cbg-site/common/mkt/pdp/audio/huawei-eyewear-2/new/img/kv/huawei-eyewear-2-kv-thumb.jpg",
    "htc":      "https://glassalmanac.com/wp-content/uploads/2025/12/87906-htc-reveals-vive-eagle-with-multi-ai-support-in-2025-why-it-matters-now.jpg.png",
    "mentra":   "https://mentraglass.com/assets/product_photos/frame.png",
    "goertek":  "https://www.goertek.com/en/Upload/image/20250306/20250306113231_0234.jpg",
    "luxshare": "https://www.luxshare-ict.com/Public/Uploads/uploadfile/images/20231018/logo2.svg",
    "mcl":      "https://www.antavicai.com/cdn/shop/files/m02-ai-glass-black06.jpg?v=1774424570&width=1500",
    "joysee":   "https://www.joysee-optical.com/wp-content/uploads/2025/07/Joysee-Eyewear-Smart-Glasses-Manufacturers-With-Camera-AI-Glasses-044.jpg",
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36",
    "Accept": "image/webp,image/png,image/jpeg,*/*",
}
MIME = {"jpg":"image/jpeg","jpeg":"image/jpeg","png":"image/png","webp":"image/webp","svg":"image/svg+xml"}

def fetch_b64(key, url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        ext  = url.split("?")[0].rsplit(".", 1)[-1].lower()
        mime = MIME.get(ext, "image/jpeg")
        print(f"  OK {key} ({len(data)//1024} KB)")
        return f"data:{mime};base64,{base64.b64encode(data).decode()}"
    except Exception as e:
        print(f"  FAIL {key}: {e}")
        return None

print("Downloading images...")
imgs = {k: fetch_b64(k, url) for k, url in IMAGES.items()}

# ── Helpers ──────────────────────────────────────────────────────────────────
def lnk(url, label):
    return f'<a class="pl" href="{url}">{label}</a>'

def tr(spec, val):
    return f"<tr><td class='sk'>{spec}</td><td>{val}</td></tr>"

def pc(key, num, title, links_html, rows, reco, contain=False):
    """Product card: image banner top, content below."""
    src = imgs.get(key)
    of  = "contain" if contain else "cover"
    bg  = "#f1f5f9" if contain else "#e2e8f0"
    if src:
        img_html = f'<img src="{src}" alt="{title}" style="width:100%;height:155pt;object-fit:{of};background:{bg};display:block;">'
    else:
        img_html = f'<div style="width:100%;height:155pt;background:#f1f5f9;display:table-cell;vertical-align:middle;text-align:center;font-size:7pt;color:#94a3b8;">Image non disponible</div>'
    return f"""
<div class="pcard">
  {img_html}
  <div class="pbody">
    <div class="phead">
      <span class="pnum">{num}</span>
      <span class="ptitle">{title}</span>
    </div>
    <div class="plinks">{links_html}</div>
    <table class="spec">{rows}</table>
    <div class="reco"><span class="reco-icon">&#x1F3AF;</span> {reco}</div>
  </div>
</div>"""

# ── CSS ──────────────────────────────────────────────────────────────────────
print("Building HTML...")

CSS = """
/* ── Force colour printing in Chromium ── */
html { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 9.5pt;
  line-height: 1.6;
  color: #1e293b;
  background: #ffffff;
}

/* ══════════════════════════════════════════
   COVER
══════════════════════════════════════════ */
.cover {
  background-color: #0f172a;
  color: #ffffff;
  width: 100%;
  min-height: 250mm;
  padding: 32mm 22mm 28mm;
  page-break-after: always;
  position: relative;
}
.cover-eyebrow {
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #60a5fa;
  margin-bottom: 14pt;
}
.cover h1 {
  font-size: 28pt;
  font-weight: 800;
  line-height: 1.15;
  color: #f8fafc;
  margin-bottom: 6pt;
}
.cover .cover-sub {
  font-size: 12pt;
  color: #94a3b8;
  margin-bottom: 20pt;
}
.cover-divider {
  width: 36pt;
  height: 3pt;
  background: #3b82f6;
  border-radius: 2pt;
  margin: 16pt 0;
}
.cover blockquote {
  border-left: 2pt solid #3b82f6;
  padding: 8pt 12pt;
  font-size: 9pt;
  color: #cbd5e1;
  line-height: 1.6;
  margin-bottom: 22pt;
}
.cover blockquote strong { color: #93c5fd; }
.cover-badges {
  margin-top: 10pt;
}
.cover-badge {
  display: inline-block;
  border: 1pt solid #334155;
  border-radius: 30pt;
  padding: 3.5pt 10pt;
  font-size: 8pt;
  font-weight: 600;
  color: #94a3b8;
  margin: 0 5pt 6pt 0;
}
.cover-footer {
  position: absolute;
  bottom: 16mm;
  left: 22mm;
  font-size: 7pt;
  color: #475569;
  letter-spacing: .04em;
}

/* ══════════════════════════════════════════
   TABLE DES MATIERES
══════════════════════════════════════════ */
.toc { page-break-after: always; }
.toc-title {
  font-size: 18pt;
  font-weight: 800;
  color: #0f172a;
  padding-bottom: 8pt;
  border-bottom: 2pt solid #3b82f6;
  margin-bottom: 16pt;
}
.toc-section {
  display: table;
  width: 100%;
  padding: 4pt 0;
  border-bottom: .5pt solid #e2e8f0;
  font-size: 9pt;
  font-weight: 600;
  color: #1e293b;
}
.toc-sub {
  display: table;
  width: 100%;
  padding: 2.5pt 0 2.5pt 14pt;
  border-bottom: .5pt dotted #f1f5f9;
  font-size: 8.5pt;
  color: #64748b;
}
.toc-label { display: table-cell; }
.toc-dots  { display: table-cell; width: 100%; border-bottom: 1pt dotted #e2e8f0; vertical-align: bottom; margin: 0 4pt; }
.toc-pg    { display: table-cell; text-align: right; white-space: nowrap; color: #94a3b8; font-weight: 400; padding-left: 6pt; }

/* ══════════════════════════════════════════
   HEADINGS
══════════════════════════════════════════ */
.section-label {
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #3b82f6;
  margin-top: 18pt;
  margin-bottom: 2pt;
}
h2 {
  font-size: 14pt;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 10pt;
  padding-bottom: 6pt;
  border-bottom: 2pt solid #e2e8f0;
  page-break-after: avoid;
}
h2 .h2-accent { color: #3b82f6; }
h3 {
  font-size: 10pt;
  font-weight: 700;
  color: #1e3a5f;
  margin: 14pt 0 5pt;
  page-break-after: avoid;
}
h4 {
  font-size: 9pt;
  font-weight: 700;
  color: #374151;
  margin: 9pt 0 4pt;
}
p { margin-bottom: 6pt; }

/* ══════════════════════════════════════════
   PRODUCT CARD
══════════════════════════════════════════ */
.pcard {
  border: 1pt solid #e2e8f0;
  border-radius: 6pt;
  overflow: hidden;
  margin: 0 0 14pt;
  page-break-inside: avoid;
  background: #ffffff;
}
.pbody { padding: 10pt 13pt 12pt; }
.phead { margin-bottom: 7pt; }
.pnum {
  display: inline-block;
  background: #1d4ed8;
  color: #fff;
  font-size: 7pt;
  font-weight: 700;
  border-radius: 3pt;
  padding: 1pt 5pt;
  margin-right: 4pt;
  vertical-align: middle;
}
.ptitle {
  font-size: 11pt;
  font-weight: 800;
  color: #0f172a;
  vertical-align: middle;
}
.plinks { margin-bottom: 7pt; }
.pl {
  display: inline-block;
  background: #eff6ff;
  color: #1d4ed8;
  border: .5pt solid #bfdbfe;
  border-radius: 3pt;
  padding: 1.5pt 6pt;
  font-size: 7pt;
  font-weight: 600;
  margin: 0 3pt 2pt 0;
  text-decoration: none;
}

/* Spec table inside card */
table.spec {
  width: 100%;
  border-collapse: collapse;
  font-size: 8.5pt;
  margin-bottom: 7pt;
}
table.spec td { padding: 3pt 6pt; border-bottom: .5pt solid #f1f5f9; vertical-align: top; }
table.spec tr:last-child td { border-bottom: none; }
table.spec tr:nth-child(even) td { background: #f8fafc; }
td.sk { font-weight: 600; color: #475569; width: 90pt; white-space: nowrap; }

/* Reco */
.reco {
  background: #f0fdf4;
  border: .5pt solid #bbf7d0;
  border-left: 3pt solid #16a34a;
  border-radius: 4pt;
  padding: 6pt 8pt;
  font-size: 8.5pt;
  color: #14532d;
  line-height: 1.5;
}
.reco strong { color: #15803d; }
.reco-icon { margin-right: 3pt; }

/* ══════════════════════════════════════════
   SUMMARY CARDS (synthese / market)
══════════════════════════════════════════ */
.cards3 { width: 100%; border-collapse: separate; border-spacing: 7pt 0; margin: 8pt 0; display: table; }
.c3 { display: table-cell; width: 33%; vertical-align: top; border: 1pt solid #e2e8f0; border-radius: 5pt; padding: 8pt 9pt; }
.c3.blue  { border-top: 3pt solid #3b82f6; }
.c3.green { border-top: 3pt solid #16a34a; }
.c3.amber { border-top: 3pt solid #f59e0b; }
.c3-label { font-size: 6.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: #94a3b8; margin-bottom: 4pt; }
.c3-val   { font-size: 8.5pt; font-weight: 600; color: #1e293b; line-height: 1.4; }

/* Top 4 priority */
.top4 { display: table; width: 100%; border-collapse: separate; border-spacing: 6pt 0; margin: 8pt 0; }
.t4   { display: table-cell; width: 25%; vertical-align: top; border: 1pt solid #e2e8f0; border-radius: 5pt; padding: 7pt 8pt; }
.t4-num {
  display: inline-block;
  width: 18pt; height: 18pt;
  background: #1d4ed8;
  color: #fff;
  border-radius: 50%;
  text-align: center;
  line-height: 18pt;
  font-size: 8pt;
  font-weight: 700;
  margin-bottom: 5pt;
}
.t4 strong { display: block; font-size: 8.5pt; color: #0f172a; margin-bottom: 1pt; }
.t4 span   { font-size: 7.5pt; color: #64748b; }

/* ══════════════════════════════════════════
   WIDE TABLES (comparatif, contacts, etc.)
══════════════════════════════════════════ */
table.wide {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
  margin: 8pt 0 12pt;
  page-break-inside: avoid;
}
table.wide th {
  background: #1e3a5f;
  color: #f8fafc;
  font-weight: 700;
  font-size: 7.5pt;
  text-align: left;
  padding: 5pt 7pt;
  letter-spacing: .02em;
}
table.wide td {
  padding: 4.5pt 7pt;
  border-bottom: .5pt solid #e2e8f0;
  vertical-align: top;
  line-height: 1.45;
}
table.wide tr:last-child td { border-bottom: none; }
table.wide tr:nth-child(even) td { background: #f8fafc; }
table.wide td strong { color: #0f172a; }
.stars { color: #f59e0b; letter-spacing: .02em; }

/* ══════════════════════════════════════════
   TIER INTRO
══════════════════════════════════════════ */
.tier-intro {
  background: #f0f7ff;
  border: .5pt solid #bfdbfe;
  border-left: 3pt solid #3b82f6;
  border-radius: 4pt;
  padding: 7pt 10pt;
  font-size: 8.5pt;
  color: #1e3a5f;
  margin-bottom: 10pt;
}

/* ══════════════════════════════════════════
   SOFTWARE SCHEMAS
══════════════════════════════════════════ */
.schemas { display: table; width: 100%; border-collapse: separate; border-spacing: 7pt 0; margin: 8pt 0; }
.sc { display: table-cell; width: 33%; vertical-align: top; border: 1pt solid #e2e8f0; border-radius: 5pt; padding: 9pt 10pt; }
.sc-badge {
  display: inline-block;
  font-size: 7pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .05em;
  color: #fff;
  background: #1d4ed8;
  border-radius: 3pt;
  padding: 2pt 6pt;
  margin-bottom: 7pt;
}
.sc.green .sc-badge { background: #15803d; }
.sc.amber .sc-badge { background: #b45309; }
.sc p { font-size: 7.5pt; line-height: 1.5; margin-bottom: 4pt; }

/* ══════════════════════════════════════════
   RISKS
══════════════════════════════════════════ */
.risk-grid { display: table; width: 100%; border-collapse: separate; border-spacing: 7pt; margin: 4pt -7pt; }
.risk-row  { display: table-row; }
.risk-card { display: table-cell; width: 50%; vertical-align: top; border: 1pt solid #fde68a; border-radius: 5pt; padding: 8pt 10pt; background: #fffbeb; }
.risk-card h4 { font-size: 8.5pt; color: #92400e; margin-bottom: 5pt; font-weight: 700; }
.risk-card ul { margin-left: 11pt; }
.risk-card li { font-size: 8pt; line-height: 1.5; margin-bottom: 2.5pt; color: #78350f; }
.risk-card li strong { color: #92400e; }
.risk-card p { font-size: 8pt; color: #78350f; margin-bottom: 4pt; }

/* ══════════════════════════════════════════
   PHASES
══════════════════════════════════════════ */
.phase {
  border: 1pt solid #e2e8f0;
  border-left: 4pt solid #1d4ed8;
  border-radius: 4pt;
  padding: 8pt 11pt;
  margin-bottom: 9pt;
  background: #fafafa;
  page-break-inside: avoid;
}
.phase.p2 { border-left-color: #16a34a; }
.phase.p3 { border-left-color: #f59e0b; }
.phase h4 { font-size: 9pt; color: #0f172a; margin-bottom: 5pt; }
.phase ol, .phase ul { margin-left: 13pt; }
.phase li { font-size: 8pt; line-height: 1.5; margin-bottom: 3pt; }

/* ══════════════════════════════════════════
   MISC
══════════════════════════════════════════ */
.page-break { page-break-after: always; }
.no-break   { page-break-inside: avoid; }
a           { color: #1d4ed8; text-decoration: none; }
strong      { font-weight: 700; }
code        { background: #f1f5f9; border-radius: 2pt; padding: .5pt 3pt; font-family: monospace; font-size: 8pt; }
ul, ol      { margin-left: 13pt; }
li          { margin-bottom: 2pt; }
.footer-note {
  font-size: 7.5pt;
  color: #94a3b8;
  font-style: italic;
  margin-top: 16pt;
  padding-top: 8pt;
  border-top: .5pt solid #e2e8f0;
}
"""

# ── HTML ─────────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Screening Fournisseurs – Lunettes IA SeeHaptic</title>
  <style>{CSS}</style>
</head>
<body>

<!-- ════════════════════════════════════
     COVER
════════════════════════════════════ -->
<div class="cover">
  <div class="cover-eyebrow">SeeHaptic &nbsp;·&nbsp; Document confidentiel &nbsp;·&nbsp; Mai 2026</div>
  <h1>Screening fournisseurs<br>Lunettes intelligentes IA</h1>
  <div class="cover-sub">Remplacement du clip Ikotek &ndash; Marché asiatique</div>
  <div class="cover-divider"></div>
  <blockquote>
    Document préparé pour <strong>SeeHaptic</strong>, solution hardware et software haptique pour les aveugles.<br>
    Objet : identifier les fournisseurs OEM&nbsp;/&nbsp;ODM&nbsp;/&nbsp;produits finis capables d'héberger l'IA propriétaire SeeHaptic sur leur plateforme caméra.
  </blockquote>
  <div class="cover-badges">
    <span class="cover-badge">13 fournisseurs analysés</span>
    <span class="cover-badge">3 tiers d'approche</span>
    <span class="cover-badge">MOQ pilote&nbsp;: 300 – 1&nbsp;000 unités</span>
    <span class="cover-badge">Marché&nbsp;: +64,2&nbsp;% S1 2025</span>
  </div>
  <div class="cover-footer">Confidentiel &ndash; SeeHaptic &copy; 2026 &nbsp;&ndash;&nbsp; Ne pas diffuser sans autorisation</div>
</div>

<!-- ════════════════════════════════════
     TABLE DES MATIÈRES
════════════════════════════════════ -->
<div class="toc">
  <div class="toc-title">Table des matières</div>

  <div class="toc-section"><span class="toc-label">1. Synthèse exécutive</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-section"><span class="toc-label">2. Contexte de marché 2026</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>

  <div class="toc-section"><span class="toc-label">3. Tier 1 — Marques OBM intégrées</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-sub"><span class="toc-label">3.1 Rokid – AI Glasses Style</span></div>
  <div class="toc-sub"><span class="toc-label">3.2 INMO – Air 3</span></div>
  <div class="toc-sub"><span class="toc-label">3.3 RayNeo / TCL – V3</span></div>
  <div class="toc-sub"><span class="toc-label">3.4 Xreal – One</span></div>
  <div class="toc-sub"><span class="toc-label">3.5 Alibaba – Quark / Qwen AI Glasses</span></div>
  <div class="toc-sub"><span class="toc-label">3.6 Xiaomi – AI Glasses</span></div>
  <div class="toc-sub"><span class="toc-label">3.7 Huawei – Eyewear 2 / AI Glasses</span></div>
  <div class="toc-sub"><span class="toc-label">3.8 HTC – VIVE Eagle (Taïwan)</span></div>
  <div class="toc-sub"><span class="toc-label">3.9 Mentra Live (open-source)</span></div>

  <div class="toc-section"><span class="toc-label">4. Tier 2 — ODM tier 1 du supply chain mondial</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-sub"><span class="toc-label">4.1 Goertek &nbsp; 4.2 Luxshare &nbsp; 4.3 Autres ODM tier 1</span></div>

  <div class="toc-section"><span class="toc-label">5. Tier 3 — ODM/OEM Shenzhen white-label</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-sub"><span class="toc-label">5.1 MCL M02 Ultra &nbsp; 5.2 Joysee Eyewear &nbsp; 5.3 Autres ODM Shenzhen</span></div>

  <div class="toc-section"><span class="toc-label">6. Écosystèmes logiciels</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-section"><span class="toc-label">7. Tableau comparatif — Top 10 prioritaires</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-section"><span class="toc-label">8. Risques et points de vigilance</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-section"><span class="toc-label">9. Plan d'action</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-section"><span class="toc-label">10. Contacts à activer en priorité</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
  <div class="toc-section"><span class="toc-label">11. Conclusion</span><span class="toc-dots"></span><span class="toc-pg">—</span></div>
</div>

<!-- ════════════════════════════════════
     1. SYNTHESE
════════════════════════════════════ -->
<div class="page-break"></div>
<div class="section-label">Section 1</div>
<h2>Synthèse exécutive</h2>
<p>Le marché des lunettes intelligentes asiatiques est arrivé à maturité industrielle. SeeHaptic dispose de trois leviers pour remplacer le clip Ikotek :</p>
<div class="cards3">
  <div class="c3 blue">
    <div class="c3-label">Voie rapide &middot; 6 mois</div>
    <div class="c3-val">Partenariat plateforme avec Rokid, INMO ou Mentra</div>
  </div>
  <div class="c3 green">
    <div class="c3-label">Voie custom &middot; 9–12 mois</div>
    <div class="c3-val">ODM Shenzhen — Joysee, MCL, Yunchuang</div>
  </div>
  <div class="c3 amber">
    <div class="c3-label">Voie industrielle &middot; 12–18 mois</div>
    <div class="c3-val">Goertek ou Luxshare pour scale &gt; 50&nbsp;k unités</div>
  </div>
</div>
<h4 style="margin-top:10pt">Quatre candidats à activer en priorité :</h4>
<div class="top4">
  <div class="t4"><div class="t4-num">1</div><strong>INMO</strong><span>Stack logicielle Android native</span></div>
  <div class="t4"><div class="t4-num">2</div><strong>Rokid</strong><span>Facteur de forme + programme partenaire</span></div>
  <div class="t4"><div class="t4-num">3</div><strong>Joysee Eyewear</strong><span>Design custom solaire</span></div>
  <div class="t4"><div class="t4-num">4</div><strong>Goertek</strong><span>Mise à l'échelle industrielle</span></div>
</div>

<!-- ════════════════════════════════════
     2. MARCHE
════════════════════════════════════ -->
<div class="section-label" style="margin-top:18pt">Section 2</div>
<h2>Contexte de marché 2026</h2>
<div class="cards3">
  <div class="c3 blue">
    <div class="c3-label">Croissance S1 2025</div>
    <div class="c3-val">+64,2&nbsp;% — 4,065&nbsp;M unités (IDC)</div>
  </div>
  <div class="c3 green">
    <div class="c3-label">CES 2026</div>
    <div class="c3-val">27&nbsp;/&nbsp;~60 exposants smart glasses venaient de Chine</div>
  </div>
  <div class="c3 amber">
    <div class="c3-label">Projection 2026</div>
    <div class="c3-val">&gt;&nbsp;10&nbsp;M unités vendues (Omdia)</div>
  </div>
</div>
<p style="font-size:8pt;color:#64748b;margin-top:5pt">~80&nbsp;% de la capacité mondiale en composants clés (lentilles, waveguides, SMT, assemblage) est concentrée en Chine.</p>

<!-- ════════════════════════════════════
     3. TIER 1
════════════════════════════════════ -->
<div class="page-break"></div>
<div class="section-label">Section 3</div>
<h2>Tier&nbsp;1 &mdash; Marques OBM intégrées</h2>
<div class="tier-intro">Acteurs vendant leurs propres lunettes sous marque, avec SDK ou programme partenaires. <strong>Voie la plus rapide</strong> vers un produit commercialisable.</div>

{pc("rokid","3.1","Rokid – AI Glasses Style",
  lnk("https://global.rokid.com/products/rokid-ai-glasses-style","&#128279; Page produit officielle") +
  lnk("https://rokid.ai/","&#128279; Programme partenaires B2B"),
  tr("Société","Hangzhou Reality Information Technology Co., Ltd. (杭州灵伴科技), fondée 2014") +
  tr("Poids","<strong>38,5 g</strong> (TR90)") +
  tr("Caméra","<strong>12 MP Sony IMX681</strong> · FOV 109° H · F2.25 · HDR + EIS · vidéo 3K 30 fps") +
  tr("SoC","<strong>Qualcomm Snapdragon AR1 Gen 1 + NXP RT600</strong>") +
  tr("RAM / ROM","2 Go / 32 Go &nbsp;·&nbsp; Wi-Fi 6 · BT 5.3") +
  tr("Autonomie","12 h usage typique · 24 h standby") +
  tr("Display","&#10060; Aucun display") +
  tr("Prix","<strong>299 – 349 USD</strong> (verres correcteurs +79 USD)") +
  tr("AI","ChatGPT 5, Gemini, DeepSeek, Qwen &mdash; 12 langues") +
  tr("Solaires","&#10003; Verres photochromiques 25 s · 6 couleurs · 99&nbsp;% UVA/UVB") +
  tr("SDK","<span class='stars'>&#9733;&#9733;&#9733;&#9733;</span> Rokid Full Stack Open Platform") +
  tr("Production","350&nbsp;k unités 2024 &middot; <strong>34&nbsp;% parts de marché « AR+AI » H2 2025</strong>"),
  "candidat n°1 pour partenariat plateforme. Inscrire SeeHaptic au <strong>Channel Partner Program</strong>. Voyant de confidentialité, 38,5&nbsp;g et écosystème ouvert sont des atouts décisifs."
)}

{pc("inmo","3.2","INMO – Air 3",
  lnk("https://www.inmoxr.com/pages/inmo-air3","&#128279; Page produit") +
  lnk("https://github.com/INMOXR/air3-unity-sdk","&#128279; SDK Unity GitHub") +
  lnk("mailto:support@inmoxr.com","&#128231; support@inmoxr.com"),
  tr("Société","Shanghai INMO Technology") +
  tr("Caméra","<strong>16 MP wide-angle</strong> — meilleure résolution grand public") +
  tr("Display","<strong>Sony Micro OLED 1080p binoculaire</strong> · waveguide 1D · FOV 36° · 600 nits") +
  tr("SoC","<strong>Snapdragon XR 8-core</strong> &nbsp;·&nbsp; 8 Go / 128 Go") +
  tr("OS","<strong>Android 14 natif</strong> — installation libre d'apps") +
  tr("AI","Plateforme « INMO Agent » (n8n open-source) · ChatGPT supporté") +
  tr("SDK","<span class='stars'>&#9733;&#9733;&#9733;&#9733;&#9733;</span> SDK Unity public GitHub · Google Play Store (90&nbsp;% des apps Android)") +
  tr("Solaires","&#9888;&#65039; Verres correcteurs et solaires ajoutables (myopie, hypéropie, progressifs)") +
  tr("Langues","11 (EN, FR, ES, IT, PT, DE, JA, SV, RU, ZH-TW, ZH-CN)"),
  "candidat n°1 sur l'ouverture logicielle. <strong>Android 14 natif</strong> = réseau de neurones directement sur le NPU (on-device, latence &lt;&nbsp;50&nbsp;ms). Contacter immédiatement pour partenariat « accessibility »."
)}

<div class="page-break"></div>
{pc("rayneo","3.3","RayNeo / TCL – V3",
  lnk("https://www.rayneo.com/","&#128279; Page produit officielle"),
  tr("Société","Thunderbird Innovation, filiale <strong>TCL</strong>") +
  tr("Caméra","<strong>12 MP IA</strong> avec reconnaissance de scène et objets") +
  tr("Forme","Lunettes display-free · design moderne · all-day wear") +
  tr("Marché","Leader chinois AR · partenaire olympique officiel") +
  tr("Autres modèles","RayNeo X3 Pro (Micro-LED 6&nbsp;000 nits) · Air 3s"),
  "à explorer pour partenariat OEM / co-brand. Capacité industrielle TCL = top 5 électronique mondial. Contact via TCL Industrial Holdings."
)}

{pc("xreal","3.4","Xreal – One",
  lnk("https://www.xreal.com/","&#128279; Page produit officielle"),
  tr("Société","Xreal (ex-Nreal), Beijing — dépôt IPO HK avril 2026") +
  tr("Display","AR display 3840×1080 natif · FOV ultra-large") +
  tr("SoC","<strong>Chip propriétaire X1</strong>") +
  tr("Force","Leader optique waveguide · partenaire officiel Android XR de Google") +
  tr("Modèles pro","Xreal Light AR Enterprise avec SDK 6DoF gesture recognition"),
  "produits orientés display visuel, <strong>moins prioritaires</strong> pour un usage AI-glasses pure caméra. Intéressant si SeeHaptic envisage un retour visuel pour malvoyants partiels.",
  contain=True
)}

{pc("alibaba","3.5","Alibaba – Quark / Qwen AI Glasses (S1 / G1)",
  lnk("https://www.alibabagroup.com/","&#128279; Page Alibaba Group"),
  tr("Modèles","<strong>G1</strong> (1&nbsp;899&nbsp;¥ / ~270 USD, sans display) — <strong>S1</strong> (3&nbsp;799&nbsp;¥ / ~536 USD, dual in-lens display)") +
  tr("Caméra","<strong>12 MP Sony IMX681</strong> · vidéo 3K · FOV 109° · HDR · lentille 5P") +
  tr("AI","<strong>Qwen</strong> (LLM Alibaba) · reconnaissance produit + prix Taobao via la caméra") +
  tr("Production","Supply chain Alibaba via Goertek / Luxshare") +
  tr("Lancement","MWC 2026"),
  "spécifications caméra excellentes (IMX681 = état de l'art). Écosystème logiciel centré sur services Alibaba en Chine. Pertinent pour benchmark technique ; ouverture partenariat hors Chine à clarifier."
)}

<div class="page-break"></div>
{pc("xiaomi","3.6","Xiaomi – AI Glasses",
  lnk("https://www.mi.com/global/","&#128279; Page Xiaomi Global"),
  tr("Caméra","<strong>12 MP ultra-wide Sony IMX681</strong> · EIS · 5 micros · 2 HP") +
  tr("SoC","<strong>Qualcomm Snapdragon AR1 + BES2700</strong> (audio Bluetooth)") +
  tr("Autonomie","8,6 h · recharge 45 min") +
  tr("Prix","À partir de <strong>1&nbsp;999 ¥ / ~278 USD</strong>") +
  tr("ODM","<strong>Goertek</strong>") +
  tr("AI","Hyper XiaoAI (écosystème fermé Xiaomi en Chine)") +
  tr("Lancement","Juin 2025 (« Human × Car × Home » event)"),
  "très bonne qualité matérielle, ouverture pour partenaire tiers à confirmer. <strong>Plutôt approcher via Goertek pour un projet OEM custom.</strong>"
)}

{pc("huawei","3.7","Huawei – Eyewear 2 / AI Glasses",
  lnk("https://consumer.huawei.com/en/accessories/huawei-eyewear-2/","&#128279; Page produit officielle"),
  tr("Caméra","<strong>Sony 12 MP 1/2.8</strong> · vidéo 1920×1440 @ 30 fps · photo 4&nbsp;092×3&nbsp;072") +
  tr("Fonctions","<strong>HDR Vivid Standard</strong> (1ʳᵉ AI glasses) · AI RAW · EIS · mode basse lumière") +
  tr("Designs","3 designs disponibles") +
  tr("Autonomie","12 h") +
  tr("OS","HarmonyOS") +
  tr("Lancement","2026"),
  "spécifications caméra excellentes (HDR Vivid, AI RAW). <strong>Mais</strong> ouverture pour IA tierce incertaine sur HarmonyOS + risques géopolitiques (Entity List US). Partenariat à négocier spécifiquement."
)}

{pc("htc","3.8","HTC – VIVE Eagle (Taïwan)",
  lnk("https://www.vive.com/us/vive-eagle/","&#128279; Page produit officielle"),
  tr("Caméra","Intégrée · traduction temps réel <strong>13 langues</strong>") +
  tr("Couleurs","Berry · Coffee · Grey · Black") +
  tr("Prix","<strong>15&nbsp;600 NT$ / ~480 EUR</strong>") +
  tr("Marché initial","Taïwan (2020EYEhaus · Taiwan Mobile)") +
  tr("Lancement","Août 2025"),
  "intéressant pour diversifier le risque hors Chine continentale. HTC a une longue expérience VR/AR et est ouverte aux partenariats. Approcher HTC Enterprise."
)}

<div class="page-break"></div>
{pc("mentra","3.9","Mentra Live (open-source)",
  lnk("https://mentraglass.com/live","&#128279; Page produit") +
  lnk("https://mentraglass.com/os","&#128279; OS et SDK") +
  lnk("https://console.mentraglass.com","&#128279; Documentation développeur"),
  tr("Poids","<strong>43 g</strong>") +
  tr("Caméra","<strong>FOV 119°</strong> · vidéo HD 1080p · photo 3&nbsp;264×2&nbsp;448") +
  tr("Audio","2 HP stéréo · 3 micros") +
  tr("Batterie","260 mAh (glasses) + 2&nbsp;200 mAh (case) — 12 h+ usage mixte") +
  tr("OS","<strong>MentraOS</strong> (open-source · TypeScript)") +
  tr("Connectivité","WiFi + Bluetooth · iOS 15.1+ / Android 12+") +
  tr("Prix","<strong>349 USD</strong> — en stock · livraison 1–3 jours") +
  tr("SDK","<span class='stars'>&#9733;&#9733;&#9733;&#9733;&#9733;</span> OS + SDK 100&nbsp;% open-source · MiniApp Store · multi-hardware") +
  tr("Précédent","<strong>Microsoft Seeing AI</strong> (accessibilité aveugles) — précédent direct"),
  "<strong>acheter 2–3 dev kits maintenant</strong> (700–1&nbsp;000 USD). Microsoft Seeing AI = votre use case exact. SDK TypeScript ouvert = portage rapide. Multi-hardware = portabilité future."
)}

<!-- ════════════════════════════════════
     4. TIER 2
════════════════════════════════════ -->
<div class="section-label">Section 4</div>
<h2>Tier&nbsp;2 &mdash; ODM tier&nbsp;1 du supply chain mondial</h2>
<div class="tier-intro">Géants industriels fabriquant les lunettes des grands noms (Meta, Apple, Xiaomi, Alibaba). Design entièrement custom SeeHaptic possible — sous réserve de <strong>volume engagé suffisant</strong>.</div>

{pc("goertek","4.1","Goertek (歌尔股份)",
  lnk("https://www.goertek.com/","&#128279; Site corporate"),
  tr("Société","Goertek Inc. — Shandong · fondée 2001") +
  tr("Statut","<strong>Plus grand ODM XR mondial</strong>") +
  tr("Clients","Meta Quest · Ray-Ban Meta · <strong>Meta Hypernova</strong> (2025) · AirPods · Apple Vision Pro · Xiaomi AI Glasses") +
  tr("Acquisitions","Shanghai OmniLight (optique micro-nano) · financement Plessey UK") +
  tr("Production","Chine + Vietnam") +
  tr("MOQ typique","<strong>&gt;&nbsp;100&nbsp;000 unités / an</strong> pour un design custom"),
  "approcher en <strong>phase 2 (post-MVP)</strong>, quand SeeHaptic aura validé son produit et pourra engager un volume. Contact via sales department ou agent industriel.",
  contain=True
)}

{pc("luxshare","4.2","Luxshare Precision (立讯精密)",
  lnk("https://www.luxshare-ict.com/","&#128279; Site corporate"),
  tr("Société","Luxshare Precision Industry Co. — Shenzhen · coté SZ:002475 · IPO HK en cours") +
  tr("Clients","AirPods · Vision Pro Apple · <strong>Meta Celeste AR glasses</strong> (Q4 2025) · <strong>OpenAI hardware device</strong> (annoncé)") +
  tr("Capacités","Usine Wuxi : <strong>500&nbsp;000 unités AR glasses</strong> · assemblage 98,7&nbsp;% · 100&nbsp;% automatisé") +
  tr("MOQ typique","Comparable à Goertek (&gt;&nbsp;100&nbsp;000 unités / an)"),
  "alternative à Goertek pour projets très volumiques. Même profil MOQ. À envisager après phase pilote.",
  contain=True
)}

<div class="no-break">
<h3>4.3 Autres ODM tier&nbsp;1 à benchmarker</h3>
<table class="wide">
  <tr><th>Fournisseur</th><th>Profil</th><th>Action</th></tr>
  <tr><td><strong>Huaqin Technology</strong></td><td>ODM smartphones / tablettes / IoT. Commandes « 10-million-level » en 2025 sur smart glasses.</td><td>Demande RFQ comparative.</td></tr>
  <tr><td><strong>Longcheer Technology</strong></td><td>ODM smartphones / wearables. Capacité massive.</td><td>Benchmark en parallèle de Huaqin.</td></tr>
  <tr><td><strong>BOE Technology</strong></td><td>Leader mondial displays. Fournisseur Apple, Samsung. Waveguides + micro-OLED.</td><td>Fournisseur composants si micro-display custom.</td></tr>
</table>
</div>

<!-- ════════════════════════════════════
     5. TIER 3
════════════════════════════════════ -->
<div class="page-break"></div>
<div class="section-label">Section 5</div>
<h2>Tier&nbsp;3 &mdash; ODM/OEM Shenzhen white-label (MOQ modéré)</h2>
<div class="tier-intro"><strong>Catégorie probablement la plus pertinente pour la phase pilote SeeHaptic.</strong> MOQ entre 300 et 1&nbsp;000 pièces · OEM/ODM full custom · CE/FCC/RoHS · SDK propriétaires sous NDA.</div>

{pc("mcl","5.1","Shenzhen MCL Technology – M02 Ultra",
  lnk("https://www.globalsources.com/Smart-glasses/ai-smart-glasses-1230316107p.htm","&#128279; Page Global Sources"),
  tr("Société","Shenzhen MCL Technology Co., Ltd. · créée 2012") +
  tr("Caméra","<strong>8 MP HD + EIS logiciel</strong>") +
  tr("AI","Reconnaissance objets temps réel (QR, texte, traduction) · ChatGPT / Doubao") +
  tr("App","HeyCyan (iOS / Android) · transfert WiFi 1080p") +
  tr("Boîtier charge","3&nbsp;600 mAh") +
  tr("MOQ","~500 pcs") +
  tr("Prix unitaire","~33 USD (gros volumes)"),
  "demander échantillons M02 Ultra. Évaluer SDK propriétaire et possibilité d'upgrade caméra à 12 MP. Bon rapport coût / fonctionnalité pour phase pilote."
)}

{pc("joysee","5.2","Joysee Eyewear (Wenzhou / Shenzhen)",
  lnk("https://www.joysee-optical.com/oem-smart-glasses/","&#128279; Page OEM/ODM") +
  lnk("https://www.joysee-optical.com/smart-glasses-with-camera-guide/","&#128279; Guide caméra"),
  tr("Profil","<strong>Fabricant lunettes optiques historique</strong> passé au smart eyewear") +
  tr("Offre","« Frame design + electronics + firmware + packaging — all under one roof »") +
  tr("Caméras","Jusqu'à 1080p") +
  tr("Certifications","<strong>CE · FCC · RoHS</strong>") +
  tr("MOQ","<strong>OEM 300 pcs · ODM 1&nbsp;000 pcs</strong>") +
  tr("White-label","&#10003; Confidentialité totale brand owners") +
  tr("Référence","Startup cycliste berlinoise — ligne caméra 1080p + traduction AR"),
  "<strong>candidat fort phase pilote.</strong> Héritage optique + capacité électronique + MOQ adapté. Envoyer RFQ détaillée (caméra 12&nbsp;MP, accès flux temps réel, design solaire premium)."
)}

<div class="no-break">
<h3>5.3 Autres ODM Shenzhen à approcher</h3>
<table class="wide">
  <tr><th>Fournisseur</th><th>Caméra</th><th>MOQ</th><th>Atout SeeHaptic</th></tr>
  <tr><td><strong>Shenzhen Jingyun IoT</strong></td><td>8 – 13 MP (Q1)</td><td>1&nbsp;000</td><td>Supply chain intégrée (batteries, PCBA, moules). Expertise translation glasses.</td></tr>
  <tr><td><strong>Shenzhen Meellan Industry</strong></td><td>HD audio + caméra</td><td>Négociable</td><td>Spécialiste smart audio sunglasses (E13 wireless waterproof foldable).</td></tr>
  <tr><td><strong>Anpo Intelligence (ENMESI)</strong></td><td>Custom</td><td>OEM/ODM</td><td>« Smart glasses remplaçant le smartphone ». enmesi.com</td></tr>
  <tr><td><strong>Weihang Shidai (Sister Tech)</strong></td><td>1080p</td><td>OEM/ODM</td><td><strong>ISO 9001 + BSCI</strong> — conformité grands retailers EU/US. szistartech.com</td></tr>
  <tr><td><strong>Beautaste Eyewear</strong></td><td>AI sport glasses</td><td>10 M paires/an</td><td>10 ans en optique haut de gamme. Moules internes. beautasteyewear.com</td></tr>
  <tr><td><strong>Yunchuang Zhixiang</strong></td><td>Custom</td><td>OEM/ODM</td><td>&#9888;&#65039; <strong>Référence explicite « OEM Wearable for Blind »</strong> — contact prioritaire.</td></tr>
  <tr><td><strong>SmartGlassesFactory.com</strong></td><td>Selon spec</td><td>OEM/ODM</td><td>Enterprise : logistique, santé, retail.</td></tr>
  <tr><td><strong>Shengye Tech (Valdus)</strong></td><td>5 MP M01</td><td>OEM/ODM</td><td>M01 AI Smart Glasses (caméra 500W, WiFi-4, BT 5.3).</td></tr>
</table>
</div>

<!-- ════════════════════════════════════
     6. ECOSYSTEMES LOGICIELS
════════════════════════════════════ -->
<div class="page-break"></div>
<div class="section-label">Section 6</div>
<h2>Écosystèmes logiciels — Où injecter l'IA SeeHaptic</h2>
<div class="schemas">
  <div class="sc">
    <div class="sc-badge">Schéma A — On-device</div>
    <p><strong>L'IA tourne directement sur le NPU</strong> des lunettes (TensorFlow Lite, ONNX Runtime, Qualcomm AI Engine).</p>
    <p><strong>Candidats :</strong> INMO Air 3 (Android 14), Rokid, certains Vuzix (Android 8.1/9.0).</p>
    <p><strong>&#10003; Avantages :</strong> latence très faible · offline · seamless.</p>
    <p><strong>&#9888; Inconvénients :</strong> autonomie réduite · thermique · modèle à optimiser.</p>
  </div>
  <div class="sc green">
    <div class="sc-badge">Schéma B — Flux smartphone</div>
    <p><strong>Flux caméra + audio streamé</strong> vers l'app SeeHaptic. Résultat haptique renvoyé.</p>
    <p><strong>Candidats :</strong> MentraOS / Mentra Live (open-source TypeScript), AugmentOS, Rokid SDK.</p>
    <p><strong>&#10003; Avantages :</strong> flexibilité IA totale (edge ou cloud).</p>
    <p><strong>&#9888; Inconvénients :</strong> dépendance smartphone · latence ajoutée · conso réseau.</p>
  </div>
  <div class="sc amber">
    <div class="sc-badge">Schéma C — SDK ODM</div>
    <p><strong>SDK propriétaire sous NDA</strong> (Joysee, MCL, Anpo…) pour accès caméra.</p>
    <p><strong>&#10003; Avantages :</strong> hardware optimisé · branding SeeHaptic.</p>
    <p><strong>&#9888; Inconvénients :</strong> qualité SDK variable · dépendance forte.</p>
  </div>
</div>

<!-- ════════════════════════════════════
     7. TABLEAU COMPARATIF
════════════════════════════════════ -->
<div class="section-label" style="margin-top:14pt">Section 7</div>
<h2>Tableau comparatif — Top&nbsp;10 fournisseurs prioritaires</h2>
<table class="wide">
  <tr><th>Fournisseur</th><th>Type</th><th>Caméra</th><th>Ouverture SW</th><th>MOQ</th><th>Action recommandée</th></tr>
  <tr><td><strong>INMO (Air 3)</strong></td><td>OBM</td><td>16 MP wide</td><td><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> Android 14 + SDK Unity</td><td>Faible</td><td>Contact support@inmoxr.com</td></tr>
  <tr><td><strong>Rokid</strong></td><td>OBM</td><td>12 MP IMX681</td><td><span class="stars">&#9733;&#9733;&#9733;&#9733;</span> SDK + Open Platform</td><td>Programme</td><td>Channel Partner Program</td></tr>
  <tr><td><strong>Mentra Live + MentraOS</strong></td><td>OBM open-source</td><td>HD 1080p · FOV 119°</td><td><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> OS TypeScript open-source</td><td>À l'unité</td><td>Acheter 2–3 dev kits</td></tr>
  <tr><td><strong>RayNeo / TCL</strong></td><td>OBM</td><td>12 MP</td><td><span class="stars">&#9733;&#9733;&#9733;</span> SDK sur demande</td><td>Partenariat</td><td>TCL Industrial Holdings</td></tr>
  <tr><td><strong>Alibaba Quark</strong></td><td>OBM</td><td>12 MP IMX681</td><td><span class="stars">&#9733;&#9733;&#9733;</span> SDK Qwen partenaires</td><td>Élevé CN</td><td>Benchmark caméra</td></tr>
  <tr><td><strong>Goertek</strong></td><td>ODM tier 1</td><td>Selon spec</td><td><span class="stars">&#9733;&#9733;</span> NDA</td><td>&gt; 100 k</td><td>Phase 2 post-MVP</td></tr>
  <tr><td><strong>Luxshare</strong></td><td>ODM tier 1</td><td>Selon spec</td><td><span class="stars">&#9733;&#9733;</span> NDA</td><td>&gt; 100 k</td><td>Alternative Goertek</td></tr>
  <tr><td><strong>Joysee Eyewear</strong></td><td>ODM Shenzhen</td><td>Jusqu'à 1080p</td><td><span class="stars">&#9733;&#9733;&#9733;</span> SDK NDA</td><td>OEM 300</td><td>RFQ phase pilote 12 MP</td></tr>
  <tr><td><strong>MCL Technology</strong></td><td>ODM Shenzhen</td><td>8 MP + EIS</td><td><span class="stars">&#9733;&#9733;</span> SDK propriétaire</td><td>~500 pcs</td><td>Échantillons M02 Ultra</td></tr>
  <tr><td><strong>Yunchuang Zhixiang</strong></td><td>ODM Shenzhen</td><td>Custom</td><td><span class="stars">&#9733;&#9733;</span> NDA</td><td>OEM/ODM</td><td>« Wearable for Blind » — prioritaire</td></tr>
</table>

<!-- ════════════════════════════════════
     8. RISQUES
════════════════════════════════════ -->
<div class="page-break"></div>
<div class="section-label">Section 8</div>
<h2>Risques et points de vigilance</h2>
<div class="risk-grid">
  <div class="risk-row">
    <div class="risk-card">
      <h4>&#9888;&#65039;&nbsp; 8.1 Risques géopolitiques</h4>
      <ul>
        <li><strong>Huawei</strong> et entités liées à Entity List US — surveiller pour produit EU / mondial.</li>
        <li><strong>Dépendance Goertek :</strong> Meta tente de diversifier ; anticiper le double sourcing.</li>
        <li><strong>HTC (Taïwan) :</strong> « safe » politiquement mais plus petit en volumes.</li>
      </ul>
    </div>
    <div class="risk-card">
      <h4>&#9888;&#65039;&nbsp; 8.2 Risques RGPD</h4>
      <p>L'UE classe les lunettes-caméra comme <strong>dispositifs haut risque</strong> — sanctions jusqu'à 4&nbsp;% du CA mondial.</p>
      <ul>
        <li>&#10003; Voyant de confidentialité visible (standard chez Meta, Rokid…)</li>
        <li>&#10003; Traitement images en interne — suppression immédiate post-inférence</li>
        <li>&#10003; DPIA avant mise sur le marché EU</li>
      </ul>
    </div>
  </div>
  <div class="risk-row">
    <div class="risk-card">
      <h4>&#9888;&#65039;&nbsp; 8.3 Risques industriels</h4>
      <ul>
        <li><strong>Maturité SDK ODM :</strong> exiger PoC avant signature.</li>
        <li><strong>Stabilité fournisseur :</strong> privilégier &gt; 3 ans d'activité · &gt; 10&nbsp;000 unités vendues.</li>
        <li><strong>MOQ vs phase pilote :</strong> négocier contrats à étapes.</li>
      </ul>
    </div>
    <div class="risk-card">
      <h4>&#9888;&#65039;&nbsp; 8.4 Risques fonctionnels</h4>
      <ul>
        <li><strong>Caméra basse lumière :</strong> tester en intérieur peu éclairé — critique pour malvoyants.</li>
        <li><strong>FOV :</strong> minimum 90°.</li>
        <li><strong>Latence end-to-end</strong> caméra &#8594; IA &#8594; haptique : cible <strong>&lt;&nbsp;200&nbsp;ms</strong>.</li>
      </ul>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════
     9. PLAN D'ACTION
════════════════════════════════════ -->
<div class="section-label" style="margin-top:14pt">Section 9</div>
<h2>Plan d'action</h2>
<div class="phase">
  <h4>Phase 1 — Qualification technique &nbsp;(0–3 mois)</h4>
  <ol>
    <li><strong>Acheter 3 dev kits :</strong> 1× INMO Air 3 · 1× Mentra Live · 1× Rokid AI Glasses Style. Coût total ~2&nbsp;000–3&nbsp;000 EUR.</li>
    <li><strong>Porter l'IA SeeHaptic :</strong> test on-device (INMO) + déporté smartphone (Mentra, Rokid).</li>
    <li><strong>Benchmark caméra :</strong> qualité, latence, FOV, basse lumière, autonomie sous charge IA.</li>
    <li><strong>Engager 5–7 ODM Shenzhen en RFQ parallèle :</strong> Joysee, MCL, Jingyun IoT, Yunchuang Zhixiang, Anpo, Meellan, Beautaste. Brief technique + NDA.</li>
  </ol>
</div>
<div class="phase p2">
  <h4>Phase 2 — Sélection partenaire pilote &nbsp;(3–6 mois)</h4>
  <ul>
    <li>Choisir 1 OBM (Rokid ou INMO) pour partenariat plateforme + premier lancement commercial.</li>
    <li>Choisir 1 ODM (Joysee, MCL ou Yunchuang) pour développement custom SeeHaptic-branded.</li>
    <li>Lancer audit usine (SGS / TÜV / Bureau Veritas) pour partenaire ODM retenu.</li>
    <li>Signer accords-cadres incluant PI, confidentialité, exclusivité régionale.</li>
  </ul>
</div>
<div class="phase p3">
  <h4>Phase 3 — Scale-up &nbsp;(6–18 mois)</h4>
  <ul>
    <li>Si volumes &gt; 50&nbsp;k unités/an : basculer (ou doubler) avec un tier 1 ODM (Goertek ou Luxshare).</li>
    <li>Diversifier géographiquement : Vietnam (Goertek), Thaïlande (Beautaste).</li>
    <li>Capitaliser sur certifications pour ouvrir US, Japon.</li>
  </ul>
</div>

<!-- ════════════════════════════════════
     10. CONTACTS
════════════════════════════════════ -->
<div class="page-break"></div>
<div class="section-label">Section 10</div>
<h2>Contacts à activer en priorité &mdash; Semaine 1</h2>
<table class="wide">
  <tr><th>Fournisseur</th><th>Canal d'entrée</th><th>Message-clé</th></tr>
  <tr><td><strong>INMO</strong></td><td><code>support@inmoxr.com</code> + Kickstarter team</td><td>Partenariat « accessibility / B2B medical » sur Air 3 · accès SDK avancé · OEM ré-habillage solaire.</td></tr>
  <tr><td><strong>Rokid</strong></td><td>Channel Partner Program — rokid.ai</td><td>SeeHaptic, solution haptique pour malvoyants, intéressée par AI Glasses Style + partenariat plateforme Europe.</td></tr>
  <tr><td><strong>Mentra Live / MentraOS</strong></td><td>mentraglass.com/contact + console dev</td><td>Test SDK pour déploiement IA accessibility — mentionner Microsoft Seeing AI comme précédent.</td></tr>
  <tr><td><strong>Joysee Eyewear</strong></td><td>Formulaire OEM joysee-optical.com</td><td>RFQ 1&nbsp;000 pcs pilote · design solaire premium · caméra 12 MP + EIS · SDK custom · CE/FCC/RoHS.</td></tr>
  <tr><td><strong>Yunchuang Zhixiang</strong></td><td>Via GlobalOEMs</td><td>« OEM Wearable for Blind » — partager brief SeeHaptic complet · obtenir échantillons.</td></tr>
  <tr><td><strong>MCL Technology</strong></td><td>Via GlobalSources</td><td>Échantillons M02 Ultra · options upgrade caméra 12 MP · modalités SDK.</td></tr>
  <tr><td><strong>Beautaste Eyewear</strong></td><td>beautasteyewear.com</td><td>Design solaire premium (acétate / TR90) · capacité intégration camera/IA module.</td></tr>
</table>

<!-- ════════════════════════════════════
     11. CONCLUSION
════════════════════════════════════ -->
<div class="section-label" style="margin-top:14pt">Section 11</div>
<h2>Conclusion</h2>
<p>La « meilleure » lunette pour SeeHaptic n'existe pas sous une seule référence : c'est une <strong>combinaison</strong> entre :</p>
<ul style="margin:6pt 0 10pt 16pt">
  <li>un capteur caméra de qualité (<strong>Sony IMX681 ou supérieur, &#8805; 12 MP</strong>),</li>
  <li>un SoC capable d'exécuter le réseau de neurones (<strong>Snapdragon AR1 ou XR2</strong> si on-device),</li>
  <li>une monture <strong>acceptable comme lunettes solaires</strong>,</li>
  <li>un fournisseur logiciel <strong>qui accepte d'exposer le flux caméra</strong>.</li>
</ul>
<h4>Quatre candidats à activer dans les prochaines semaines :</h4>
<div class="top4" style="margin-top:8pt">
  <div class="t4"><div class="t4-num">1</div><strong>INMO</strong><span>Stack logicielle Android native</span></div>
  <div class="t4"><div class="t4-num">2</div><strong>Rokid</strong><span>Facteur de forme + programme partenaire</span></div>
  <div class="t4"><div class="t4-num">3</div><strong>Joysee Eyewear</strong><span>Design custom solaire — phase pilote</span></div>
  <div class="t4"><div class="t4-num">4</div><strong>Goertek</strong><span>Mise à l'échelle industrielle (phase 2)</span></div>
</div>

<div class="footer-note">
  Document préparé en mai 2026 sur la base de sources publiques : sites fabricants (Rokid, INMO, Mentra, RayNeo, Huawei, HTC, Joysee, Beautaste, Goertek, Luxshare), IDC, Counterpoint, presse spécialisée (CES 2026 / MWC 2026, BGR, Pandaily, SCMP, CNBC, TrendForce, Financial Times), plateformes B2B (Made-in-China, Global Sources, GlobalOEMs). &mdash; Confidentiel SeeHaptic &copy; 2026.
</div>

</body>
</html>"""

# ── Save self-contained HTML for Puppeteer ───────────────────────────────────
print("Saving HTML...")
html_path = r"C:\Users\FG\Desktop\Lunettes Co\_pdf_source.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Saved: {html_path}")
