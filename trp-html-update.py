import os

BASE = '/Users/david/Desktop/trp-website'

HAMBURGER = '    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false">\n      <span></span><span></span><span></span>\n    </button>'

JS = '<script>(function(){var t=document.getElementById("navToggle"),n=document.getElementById("mobileNav");function cl(){t.classList.remove("open");n.classList.remove("open");document.body.classList.remove("nav-open");}t.addEventListener("click",function(){var o=n.classList.toggle("open");t.classList.toggle("open");document.body.classList.toggle("nav-open");t.setAttribute("aria-expanded",o);});document.addEventListener("keydown",function(e){if(e.key==="Escape")cl();});})()</script>'

OLD_NAV_END = '    </div>\n  </div>\n</nav>'

pages = [('index.html','home'),('about.html','about'),('programs.html','programs'),('contact.html','contact')]

for fname, page in pages:
    fp = os.path.join(BASE, fname)
    with open(fp,'r') as f:
        html = f.read()
    if 'mobile-nav' in html:
        print(fname+': skip')
        continue
    acts = {'home':'','about':'','programs':'','contact':''}
    acts[page] = ' active'
    mnav = '<div class="mobile-nav" id="mobileNav"><div class="mobile-nav-inner">'
    mnav += '<a href="index.html" class="mobile-link'+acts['home']+'">Home</a>'
    mnav += '<a href="about.html" class="mobile-link'+acts['about']+'">About</a>'
    mnav += '<a href="programs.html" class="mobile-link'+acts['programs']+'">Programs</a>'
    mnav += '<a href="contact.html" class="mobile-link'+acts['contact']+'">Contact</a>'
    mnav += '<div class="mobile-nav-footer">'
    mnav += '<a href="https://trpapply.zite.so" target="_blank" class="btn btn-primary btn-lg">Apply / Tour</a>'
    mnav += '<a href="https://trpenrolled.zite.so" target="_blank" class="btn btn-outline-navy">Enrolled Families</a>'
    mnav += '</div><p class="mobile-nav-meta">info@therosspreschool.org</p>'
    mnav += '</div></div>' + JS
    new_end = '    </div>\n' + HAMBURGER + '\n  </div>\n</nav>\n' + mnav
    if OLD_NAV_END in html:
        html = html.replace(OLD_NAV_END, new_end, 1)
        print(fname+': OK')
    else:
        print(fname+': pattern not found - checking...')
        idx = html.find('</nav>')
        print('  near nav:', repr(html[idx-60:idx+8]))
    with open(fp,'w') as f:
        f.write(html)

print('done')
