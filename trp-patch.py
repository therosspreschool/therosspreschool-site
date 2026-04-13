import os, re

BASE = os.path.expanduser('~/Desktop/trp-website')

# ---- styles.css ----
with open(f'{BASE}/styles.css', 'r') as f:
    css = f.read()

# Fix page-hero-bg inset
css = css.replace(
    ".page-hero-bg {\n  position: absolute;\n  inset: 0;\n  background-size: cover;\n  background-position: center;\n  opacity: 0.25;\n}",
    ".page-hero-bg {\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  background-size: cover;\n  background-position: center;\n  opacity: 0.25;\n}"
)

# Fix video-overlay inset
css = css.replace(
    ".video-overlay {\n  position: absolute;\n  inset: 0;\n  background: rgba(17,29,68,0.38);",
    ".video-overlay {\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  background: rgba(17,29,68,0.38);"
)

# Fix mobile-nav inset
css = css.replace(
    ".mobile-nav {\n  display: none;\n  position: fixed;\n  inset: 0;\n  z-index: 200;",
    ".mobile-nav {\n  display: none;\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  z-index: 200;"
)

# Add hero bg mobile position
css = css.replace(
    '  .home-hero { min-height: 88vh; }\n  .home-hero-content',
    '  .home-hero { min-height: 88vh; }\n  .home-hero-bg { background-position: 72% top; }\n  .home-hero-content'
)

# Add teacher photo mobile size
css = css.replace(
    '@media (max-width: 480px) {\n  .teacher-grid { grid-template-columns: repeat(2, 1fr); }\n}',
    '@media (max-width: 480px) {\n  .teacher-grid { grid-template-columns: repeat(2, 1fr); }\n  .teacher-photo-wrap { width: 100px; height: 100px; }\n}'
)

with open(f'{BASE}/styles.css', 'w') as f:
    f.write(css)
print('styles.css done')

# ---- index.html ----
with open(f'{BASE}/index.html', 'r') as f:
    html = f.read()

# Fix Life at TRP inline grid style
html = html.replace(
    '<div class="icon-box-grid" style="grid-template-columns: repeat(3,1fr);">',
    '<div class="icon-box-grid">'
)

# Update stylesheet version
html = html.replace('styles.css?v=2', 'styles.css?v=3')
html = html.replace('styles.css?v=3', 'styles.css?v=3')

# Add SEO head if not already present
if 'og:title' not in html:
    old_head = '<link rel="preconnect" href="https://fonts.googleapis.com">\n  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">\n  <link rel="stylesheet" href="styles.css?v=3">'
    new_head = """<meta name=\"keywords\" content=\"preschool Ross CA, preschool Marin County, play-based preschool, pre-K Ross California, child care Marin, preschool enrollment, The Ross Preschool\">
  <meta name=\"robots\" content=\"index, follow\">
  <link rel=\"canonical\" href=\"https://www.therosspreschool.org/\">
  <meta property=\"og:type\" content=\"website\">
  <meta property=\"og:site_name\" content=\"The Ross Preschool\">
  <meta property=\"og:title\" content=\"The Ross Preschool | Play-Based Preschool in Ross, Marin County CA\">
  <meta property=\"og:description\" content=\"Play-based preschool &amp; pre-K in Ross, Marin County. Ages 2-5. Building capable, compassionate humans. Now enrolling.\">
  <meta property=\"og:url\" content=\"https://www.therosspreschool.org/\">
  <meta property=\"og:image\" content=\"https://www.therosspreschool.org/hero.jpg\">
  <meta name=\"twitter:card\" content=\"summary_large_image\">
  <meta name=\"twitter:title\" content=\"The Ross Preschool | Play-Based Preschool in Ross, Marin County CA\">
  <meta name=\"twitter:description\" content=\"Play-based preschool &amp; pre-K in Ross, Marin County. Ages 2-5. Building capable, compassionate humans. Now enrolling.\">
  <meta name=\"twitter:image\" content=\"https://www.therosspreschool.org/hero.jpg\">
  """ + old_head
    html = html.replace(old_head, new_head)

with open(f'{BASE}/index.html', 'w') as f:
    f.write(html)
print('index.html done')

# ---- sitemap.xml ----
sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.therosspreschool.org/</loc><lastmod>2026-04-05</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://www.therosspreschool.org/about.html</loc><lastmod>2026-04-05</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>https://www.therosspreschool.org/programs.html</loc><lastmod>2026-04-05</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>
  <url><loc>https://www.therosspreschool.org/contact.html</loc><lastmod>2026-04-05</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>
</urlset>'''
with open(f'{BASE}/sitemap.xml', 'w') as f:
    f.write(sitemap)
print('sitemap.xml done')

# ---- robots.txt ----
robots = 'User-agent: *\nAllow: /\n\nSitemap: https://www.therosspreschool.org/sitemap.xml\n'
with open(f'{BASE}/robots.txt', 'w') as f:
    f.write(robots)
print('robots.txt done')

print('ALL DONE')
