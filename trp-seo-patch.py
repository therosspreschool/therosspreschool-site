import os

BASE = os.path.expanduser('~/Desktop/trp-website')

pages = {
    'about.html': {
        'title': 'About Us | The Ross Preschool - Ross, Marin County CA',
        'desc': 'Learn about The Ross Preschool philosophy, mission, and dedicated teaching team. Play-based preschool in Ross, Marin County, serving families ages 2-5.',
        'keywords': 'about The Ross Preschool, preschool philosophy Marin, play-based learning, preschool teachers Ross CA',
        'canonical': 'https://www.therosspreschool.org/about.html',
        'og_title': 'About Us | The Ross Preschool - Ross, Marin County CA',
        'og_desc': 'Meet the team and learn about the philosophy behind The Ross Preschool. Play-based, nature-oriented preschool in Ross, CA.',
    },
    'programs.html': {
        'title': 'Programs & Learning | The Ross Preschool - Ross, Marin County CA',
        'desc': 'Play-based, nature-oriented curriculum for ages 2-5. Social-emotional learning, kindergarten readiness, outdoor classroom, and afterschool enrichment in Ross, Marin County.',
        'keywords': 'preschool programs Ross CA, play-based curriculum, kindergarten readiness Marin, nature-based preschool, afterschool enrichment',
        'canonical': 'https://www.therosspreschool.org/programs.html',
        'og_title': 'Programs & Learning | The Ross Preschool - Ross, Marin County CA',
        'og_desc': 'Play-based, nature-oriented curriculum for ages 2-5 in Ross, Marin County. Kindergarten readiness, social-emotional learning, outdoor classroom.',
    },
    'contact.html': {
        'title': 'Contact & Apply | The Ross Preschool - Ross, Marin County CA',
        'desc': 'Apply for enrollment or schedule a tour at The Ross Preschool in Ross, Marin County CA. Reach us at team@therosspreschool.org or (415) 634-7111.',
        'keywords': 'contact The Ross Preschool, preschool enrollment Ross CA, schedule tour preschool Marin, apply preschool Marin County',
        'canonical': 'https://www.therosspreschool.org/contact.html',
        'og_title': 'Contact & Apply | The Ross Preschool - Ross, Marin County CA',
        'og_desc': 'Apply for enrollment or schedule a tour at The Ross Preschool in Ross, Marin County CA. Reach us at team@therosspreschool.org.',
    },
}

for fname, info in pages.items():
    fp = os.path.join(BASE, fname)
    with open(fp, 'r') as f:
        html = f.read()

    # Update CSS version
    html = html.replace('styles.css?v=2', 'styles.css?v=3')

    # Add SEO tags if not already present
    if 'og:title' not in html:
        old_link = '<link rel="preconnect" href="https://fonts.googleapis.com">'
        seo_block = f"""<meta name="keywords" content="{info['keywords']}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{info['canonical']}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="The Ross Preschool">
  <meta property="og:title" content="{info['og_title']}">
  <meta property="og:description" content="{info['og_desc']}">
  <meta property="og:url" content="{info['canonical']}">
  <meta property="og:image" content="https://www.therosspreschool.org/hero.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{info['og_title']}">
  <meta name="twitter:description" content="{info['og_desc']}">
  <meta name="twitter:image" content="https://www.therosspreschool.org/hero.jpg">
  """ + old_link
        html = html.replace(old_link, seo_block)

    with open(fp, 'w') as f:
        f.write(html)
    print(f'{fname} done')

print('ALL DONE')
