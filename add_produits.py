f = open('/data/data/com.termux/files/home/boutique-pro/index.html','r')
c = f.read()
f.close()

nouveaux = '''
        <div class="product-card">
          <div class="product-img"><img src="https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=300&h=300&fit=crop" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="product-info">
            <div class="product-name">Robe Élégante</div>
            <div class="product-price">15 000 FCFA</div>
            <a class="btn-wa" href="https://wa.me/22891547843?text=Bonjour%20je%20veux%20commander%20la%20Robe%20%C3%89l%C3%A9gante%20(15%20000%20FCFA)" target="_blank"><span class="wa-icon">💬</span> Commander</a>
          </div>
        </div>
        <div class="product-card">
          <div class="product-img"><img src="https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=300&h=300&fit=crop" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="product-info">
            <div class="product-name">Chemise Oxford</div>
            <div class="product-price">8 000 FCFA</div>
            <a class="btn-wa" href="https://wa.me/22891547843?text=Bonjour%20je%20veux%20commander%20la%20Chemise%20Oxford%20(8%20000%20FCFA)" target="_blank"><span class="wa-icon">💬</span> Commander</a>
          </div>
        </div>
        <div class="product-card">
          <div class="product-img"><img src="https://images.unsplash.com/photo-1542272604-787c3835535d?w=300&h=300&fit=crop" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="product-info">
            <div class="product-name">Pantalon Slim</div>
            <div class="product-price">10 000 FCFA</div>
            <a class="btn-wa" href="https://wa.me/22891547843?text=Bonjour%20je%20veux%20commander%20le%20Pantalon%20Slim%20(10%20000%20FCFA)" target="_blank"><span class="wa-icon">💬</span> Commander</a>
          </div>
        </div>
        <div class="product-card">
          <div class="product-img"><img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300&h=300&fit=crop" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="product-info">
            <div class="product-name">Chaussures Derby</div>
            <div class="product-price">18 000 FCFA</div>
            <a class="btn-wa" href="https://wa.me/22891547843?text=Bonjour%20je%20veux%20commander%20les%20Chaussures%20Derby%20(18%20000%20FCFA)" target="_blank"><span class="wa-icon">💬</span> Commander</a>
          </div>
        </div>
        <div class="product-card">
          <div class="product-img"><img src="https://images.unsplash.com/photo-1449505278894-297fdb3edbc1?w=300&h=300&fit=crop" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="product-info">
            <div class="product-name">Mocassins Cuir</div>
            <div class="product-price">14 000 FCFA</div>
            <a class="btn-wa" href="https://wa.me/22891547843?text=Bonjour%20je%20veux%20commander%20les%20Mocassins%20Cuir%20(14%20000%20FCFA)" target="_blank"><span class="wa-icon">💬</span> Commander</a>
          </div>
        </div>
        <div class="product-card">
          <div class="product-img"><img src="https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=300&h=300&fit=crop" alt="produit" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="product-info">
            <div class="product-name">Escarpins Dorés</div>
            <div class="product-price">12 000 FCFA</div>
            <a class="btn-wa" href="https://wa.me/22891547843?text=Bonjour%20je%20veux%20commander%20les%20Escarpins%20Dor%C3%A9s%20(12%20000%20FCFA)" target="_blank"><span class="wa-icon">💬</span> Commander</a>
          </div>
        </div>
'''

c = c.replace('</div><!-- /products-grid -->', nouveaux + '</div><!-- /products-grid -->')
f = open('/data/data/com.termux/files/home/boutique-pro/index.html','w')
f.write(c)
f.close()
print('6 nouveaux produits ajoutés ✅')
