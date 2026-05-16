f=open('/data/data/com.termux/files/home/boutique-pro/index.html','r')
c=f.read()
f.close()
section='''<div style="background:#F0E8D2;padding:60px 24px;text-align:center">
<p style="font-size:.72rem;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#C8973A;margin-bottom:12px">En chiffres</p>
<h2 style="font-family:Cormorant Garamond,serif;font-size:2.2rem;color:#1C3D35;margin-bottom:36px">Ce que vous gagnez</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:20px;max-width:900px;margin:0 auto">
<div style="background:#fff;border-radius:16px;padding:24px 16px;border:1px solid #e8dcc8"><div style="font-size:1.8rem">🛒</div><div style="font-family:Cormorant Garamond,serif;font-size:2.5rem;font-weight:700;color:#1C3D35" class="cnt" data-t="3">0</div><div style="font-size:.8rem;color:#6B6560;margin-top:6px">x plus de commandes</div><span style="background:#E8F5ED;color:#1E7A40;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:20px;margin-top:8px;display:inline-block">↑ Ventes</span></div>
<div style="background:#fff;border-radius:16px;padding:24px 16px;border:1px solid #e8dcc8"><div style="font-size:1.8rem">⏱️</div><div style="font-family:Cormorant Garamond,serif;font-size:2.5rem;font-weight:700;color:#1C3D35" class="cnt" data-t="72">0</div><div style="font-size:.8rem;color:#6B6560;margin-top:6px">heures délai maximum</div><span style="background:#E8F5ED;color:#1E7A40;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:20px;margin-top:8px;display:inline-block">Livraison rapide</span></div>
<div style="background:#fff;border-radius:16px;padding:24px 16px;border:1px solid #e8dcc8"><div style="font-size:1.8rem">📱</div><div style="font-family:Cormorant Garamond,serif;font-size:2.5rem;font-weight:700;color:#1C3D35" class="cnt" data-t="100">0</div><div style="font-size:.8rem;color:#6B6560;margin-top:6px">% commandes sur WhatsApp</div><span style="background:#E8F5ED;color:#1E7A40;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:20px;margin-top:8px;display:inline-block">↑ Conversion</span></div>
<div style="background:#fff;border-radius:16px;padding:24px 16px;border:1px solid #e8dcc8"><div style="font-size:1.8rem">💰</div><div style="font-family:Cormorant Garamond,serif;font-size:2.5rem;font-weight:700;color:#1C3D35" class="cnt" data-t="0">0</div><div style="font-size:.8rem;color:#6B6560;margin-top:6px">€ de frais mensuels</div><span style="background:#E8F5ED;color:#1E7A40;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:20px;margin-top:8px;display:inline-block">Paiement unique</span></div>
<div style="background:#fff;border-radius:16px;padding:24px 16px;border:1px solid #e8dcc8"><div style="font-size:1.8rem">🌍</div><div style="font-family:Cormorant Garamond,serif;font-size:2.5rem;font-weight:700;color:#1C3D35" class="cnt" data-t="7">0</div><div style="font-size:.8rem;color:#6B6560;margin-top:6px">secteurs couverts</div><span style="background:#E8F5ED;color:#1E7A40;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:20px;margin-top:8px;display:inline-block">Tous secteurs</span></div>
<div style="background:#fff;border-radius:16px;padding:24px 16px;border:1px solid #e8dcc8"><div style="font-size:1.8rem">⭐</div><div style="font-family:Cormorant Garamond,serif;font-size:2.5rem;font-weight:700;color:#1C3D35" class="cnt" data-t="24">0</div><div style="font-size:.8rem;color:#6B6560;margin-top:6px">h réponse garantie</div><span style="background:#E8F5ED;color:#1E7A40;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:20px;margin-top:8px;display:inline-block">Support réactif</span></div>
</div></div>
<script>
(function(){var els=document.querySelectorAll(".cnt");function anim(){els.forEach(function(el){var t=+el.dataset.t;if(t===0){el.textContent="0";return}var d=1800,s=t/60,cur=0;var tm=setInterval(function(){cur+=s;if(cur>=t){cur=t;clearInterval(tm)}el.textContent=Math.floor(cur)},d/60)})}
var o=new IntersectionObserver(function(e){e.forEach(function(en){if(en.isIntersecting){anim();o.disconnect()}})},{threshold:0.3});var sec=document.querySelector(".cnt");if(sec)o.observe(sec.parentElement.parentElement)})();
</script>
'''
c=c.replace('<!-- SERVICES -->',section+'<!-- SERVICES -->')
f=open('/data/data/com.termux/files/home/boutique-pro/index.html','w')
f.write(c)
f.close()
print('OK ✅')
