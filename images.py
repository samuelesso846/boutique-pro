f = open('/data/data/com.termux/files/home/boutique-pro/index.html','r')
c = f.read()
f.close()

imgs = [
  ('🧴', 'https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=300&h=300&fit=crop'),
  ('🫙', 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=300&h=300&fit=crop'),
  ('🌸', 'https://images.unsplash.com/photo-1541643600914-78b084683702?w=300&h=300&fit=crop'),
  ('🧼', 'https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=300&h=300&fit=crop'),
  ('💊', 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=300&h=300&fit=crop'),
  ('🌿', 'https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=300&h=300&fit=crop'),
]

for emoji, url in imgs:
  old = f'<div class="product-img">{emoji}</div>'
  new = f'<div class="product-img"><img src="{url}" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>'
  c = c.replace(old, new)

f = open('/data/data/com.termux/files/home/boutique-pro/index.html','w')
f.write(c)
f.close()
print('Images ajoutées ✅')
