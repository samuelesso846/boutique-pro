f = open('/data/data/com.termux/files/home/boutique-pro/index.html','r')
c = f.read()
f.close()
t = '''
<section style="padding:4rem 1.5rem;background:#fff;text-align:center;">
<div style="font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#C9933A;margin-bottom:.8rem;">Témoignages</div>
<h2 style="font-family:Cormorant Garamond,serif;font-size:2rem;color:#163D28;margin-bottom:2rem;">Ce que disent nos clients</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.5rem;max-width:820px;margin:0 auto;">
<div style="background:#FFFBF4;border:1px solid #EDE3D5;border-radius:16px;padding:1.8rem;text-align:left;">
<div style="color:#C9933A;margin-bottom:.8rem;">★★★★★</div>
<p style="font-size:.87rem;color:#6B5D52;line-height:1.7;margin-bottom:1.2rem;">"Ma boutique est en ligne, mes clientes commandent sur WhatsApp directement. J'ai eu mes premières commandes en 2 jours !"</p>
<div style="display:flex;align-items:center;gap:.7rem;"><div style="width:38px;height:38px;border-radius:50%;background:#163D28;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">A</div><div><div style="font-weight:600;font-size:.85rem;color:#163D28;">Aminata K.</div><div style="font-size:.75rem;color:#6B5D52;">Boutique beauté</div></div></div>
</div>
<div style="background:#FFFBF4;border:1px solid #EDE3D5;border-radius:16px;padding:1.8rem;text-align:left;">
<div style="color:#C9933A;margin-bottom:.8rem;">★★★★★</div>
<p style="font-size:.87rem;color:#6B5D52;line-height:1.7;margin-bottom:1.2rem;">"Livré en 48h, design très professionnel. Mes clients pensent que j'ai une grande boutique. Je recommande !"</p>
<div style="display:flex;align-items:center;gap:.7rem;"><div style="width:38px;height:38px;border-radius:50%;background:#1E5438;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">K</div><div><div style="font-weight:600;font-size:.85rem;color:#163D28;">Kofi M.</div><div style="font-size:.75rem;color:#6B5D52;">Vêtements & accessoires</div></div></div>
</div>
<div style="background:#FFFBF4;border:1px solid #EDE3D5;border-radius:16px;padding:1.8rem;text-align:left;">
<div style="color:#C9933A;margin-bottom:.8rem;">★★★★★</div>
<p style="font-size:.87rem;color:#6B5D52;line-height:1.7;margin-bottom:1.2rem;">"Avant je perdais des clients sans catalogue. Maintenant j'envoie mon lien à tout le monde. Simple et efficace !"</p>
<div style="display:flex;align-items:center;gap:.7rem;"><div style="width:38px;height:38px;border-radius:50%;background:#C9933A;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;">F</div><div><div style="font-weight:600;font-size:.85rem;color:#163D28;">Fatoumata D.</div><div style="font-size:.75rem;color:#6B5D52;">Alimentation & épicerie</div></div></div>
</div>
</div></section>
'''
c = c.replace('<!-- ── CONTACT ── -->', t + '<!-- ── CONTACT ── -->')
f = open('/data/data/com.termux/files/home/boutique-pro/index.html','w')
f.write(c)
f.close()
print('OK')
