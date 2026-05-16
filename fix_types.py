f=open('/data/data/com.termux/files/home/boutique-pro/index.html','r')
c=f.read()
f.close()
old='''    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:1rem; max-width:700px; margin:0 auto;">
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.5rem 1rem; text-align:center;">
      <div style="font-size:2rem; margin-bottom:0.5rem;">👗</div>
      <div style="font-weight:600; font-size:0.88rem; color:var(--green);">Mode & Vêtements</div>
    </div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.5rem 1rem; text-align:center;">
      <div style="font-size:2rem; margin-bottom:0.5rem;">💄</div>
      <div style="font-weight:600; font-size:0.88rem; color:var(--green);">Cosmétiques</div>
    </div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.5rem 1rem; text-align:center;">
      <div style="font-size:2rem; margin-bottom:0.5rem;">📱</div>
      <div style="font-weight:600; font-size:0.88rem; color:var(--green);">Électronique</div>
    </div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.5rem 1rem; text-align:center;">
      <div style="font-size:2rem; margin-bottom:0.5rem;">🍎</div>
      <div style="font-weight:600; font-size:0.88rem; color:var(--green);">Alimentation</div>
    </div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.5rem 1rem; text-align:center;">
      <div style="font-size:2rem; margin-bottom:0.5rem;">👠</div>
      <div style="font-weight:600; font-size:0.88rem; color:var(--green);">Chaussures</div>
    </div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.5rem 1rem; text-align:center;">
      <div style="font-size:2rem; margin-bottom:0.5rem;">🛋️</div>
      <div style="font-weight:600; font-size:0.88rem; color:var(--green);">Maison & Déco</div>
    </div>
  </div>'''
new='''    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(130px,1fr)); gap:1rem; max-width:760px; margin:0 auto;">
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">👗</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Mode & Vêtements</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">💄</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Cosmétiques</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">📱</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Électronique</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">🍽️</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Restaurant</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">⚡</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Électricien</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">🏪</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">TPE & Commerce</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">🏗️</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Artisan & BTP</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">🍎</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Alimentation</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">💇</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Salon & Beauté</div></div>
    <div style="background:var(--cream); border:1px solid var(--border); border-radius:14px; padding:1.2rem 0.8rem; text-align:center;"><div style="font-size:1.8rem; margin-bottom:0.4rem;">🚗</div><div style="font-weight:600; font-size:0.82rem; color:var(--green);">Auto & Garage</div></div>
  </div>'''
c=c.replace(old,new)
f=open('/data/data/com.termux/files/home/boutique-pro/index.html','w')
f.write(c)
f.close()
print('OK' if old in open('/data/data/com.termux/files/home/boutique-pro/index.html').read()==False else 'Types mis à jour ✅')
