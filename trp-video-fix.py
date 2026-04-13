import os

BASE = os.path.expanduser('~/Desktop/trp-website')
fp = os.path.join(BASE, 'index.html')

with open(fp, 'r') as f:
    html = f.read()

# The VideoObject block to insert
video_schema = '''  <!-- VideoObject schema - fixes Google Search Console uploadDate timezone warning from embedded Vadoo iframe -->
  <script type="application/ld+json">{
    "@context": "https://schema.org",
    "@type": "VideoObject",
    "name": "The Ross Preschool - Raising Capable, Compassionate Humans",
    "description": "A look inside The Ross Preschool - a play-based, nature-oriented preschool and pre-K program in Ross, Marin County CA. See how we partner with families to raise capable, compassionate humans.",
    "thumbnailUrl": "https://www.therosspreschool.org/hero.jpg",
    "uploadDate": "2021-06-08T15:56:52-07:00",
    "contentUrl": "https://api.vadoo.tv/iframe_test?id=XFccw252I4u38RWXUVY-0bUFueSZ-69c",
    "embedUrl": "https://api.vadoo.tv/iframe_test?id=XFccw252I4u38RWXUVY-0bUFueSZ-69c",
    "publisher": {
      "@type": "Organization",
      "name": "The Ross Preschool",
      "url": "https://www.therosspreschool.org",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.therosspreschool.org/images/logo.png"
      }
    }
  }</script>'''

# Only add if not already present
if 'VideoObject' not in html:
    marker = '  <link rel="preconnect" href="https://fonts.googleapis.com">'
    html = html.replace(marker, video_schema + '
' + marker)
    with open(fp, 'w') as f:
        f.write(html)
    print('VideoObject schema added to index.html')
else:
    print('VideoObject schema already present - skipping')
