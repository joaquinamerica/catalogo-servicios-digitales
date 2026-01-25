import csv
from collections import defaultdict
from zipfile import ZipFile

# Archivo final
html_filename = "pagina_categorias.html"
zip_filename = "pagina_categorias.zip"

# Aquí pega **TODO tu CSV completo**
csv_data = """Logo,Categoria,Comision
https://cdn.taecel.com/src/app/assets/img/carriers/telcel.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/movistar2.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/unefon2.png,Tiempo Aire,2.00
https://cdn.pagomex.com/src/app/assets/img/carriers/att.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/telmex.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/cfe.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/fiscalcloud.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/maxcom.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/sky.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/virgin-mobile.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/axtel.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/nextel.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/infonavit.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/megacable.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/dish.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/internet-telcel.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/amigo-sin-limite.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/cablevision2.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/totalplay.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/iave.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/televia.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/izzi.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/agua-celaya.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/agua-salamanca.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/arabela.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/avon.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/belcorp.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/fuller.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/ilusion.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/jafra.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/natura.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/swissJust.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/tupperware.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/ivesrocher.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/gas-natural.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/azul-crema.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-xbox-live-gold.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/factura-fiel.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/kaspersky.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/nintendo-eshop.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/netflix.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/pase-urbano.png,Servicios,4.00
https://cdn.taecel.com/src/app/assets/img/carriers/weex.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/spotify.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/deezer.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/rixty.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/flashmobile.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/cea.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/aguasdesaltillo.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/aguadetijuana.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/aguakan.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/amd.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-cdmx.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/edomex.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/interapas.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/vrim-tdc.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/jmas.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/multimedios-saltillo.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/sadm.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/siapa.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/telnor.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/oui2.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/herbalife.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/stanhome.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/yanbal.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-zermat.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-terramar.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/uber.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/cinepolis.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/ps-plus.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/xboxgift.jpeg,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/xboxgp.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/amazongc.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-cespe.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-soapap.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-ecogas.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/telcel.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/movistar2.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-mundojade.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-startv.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-viapass.png,Servicios,4.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-sideapa.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-japay.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-nettv.png ,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-wimo.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-norton.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-office365.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/freedompop.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/cfe.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/googleplay.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/eats.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/oninternet.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/hughesnet.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/secretariafinanzas.jpg,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/gobjalisco.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/internetportiempo.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/PilloFon1.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/soriana-movil.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/Diri2.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/ciapacov.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/comapa.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/sapami.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/sacmex.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/seapal.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/simas.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/starbucks-card.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/bait.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/bait.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/bigcel.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo_miMovil.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/bait.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-17.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-16.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-15.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-13.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-14.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-12.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-07.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-05.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-01.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-02.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-04.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-10.png,Servicios,9.00
https://cdn.pagomex.com/src/app/assets/img/carriers/naucalpan-de-juarez.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/WEB_TCL_MAYO-09.png,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/valor-telecom.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/yobi.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/jrmovil.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/telmovil.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/newww.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/abib.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/compartcarga.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/elektra.png,Servicios,10.00
https://cdn.taecel.com/src/app/assets/img/carriers/blizzard.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/cinemex.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/paramount-plus.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/bitdefender.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/enviaflores.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/bait.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/dalefon.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/netwey.png,Servicios,4.00
https://cdn.taecel.com/src/app/assets/img/carriers/cfeteit.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/axios-mobile.svg,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/rincel.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/vasanta.png,Tiempo Aire,2.00
https://cdn.pagomex.com/src/app/assets/img/carriers/roblox.png,GiftCards,3.00
https://cdn.pagomex.com/src/app/assets/img/carriers/megamovil.png,Tiempo Aire,2.00
https://cdn.pagomex.com/src/app/assets/img/carriers/stargo.png,Servicios,9.00
https://cdn.pagomex.com/src/app/assets/img/carriers/gobierno-coahuila.png,Servicios,9.00
https://cdn.pagomex.com/src/app/assets/img/carriers/gobiernotonala.png,Servicios,9.00
https://cdn.pagomex.com/src/app/assets/img/carriers/giit.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/bienestar.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-ultracel.png,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/cespm.jpeg,Servicios,9.00
https://cdn.taecel.com/src/app/assets/img/carriers/FRC.jpeg,Tiempo Aire,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/beneleit2.png,Tiempo Aire,2.00
https://cdn.pagomex.com/src/app/assets/img/carriers/freefire.png,GiftCards,3.00
https://cdn.pagomex.com/src/app/assets/img/carriers/innovasport.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/krispykreme.jpg,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/minecraft.png,GiftCards,3.00
https://cdn.pagomex.com/src/app/assets/img/carriers/liverpool-regalo.png,GiftCards,3.00
https://cdn.pagomex.com/src/app/assets/img/carriers/youtube.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/gandhi.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/inbursa-aquarium-mexico.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/hym.jpg,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/Giftcard-Innvictus.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/kataplumCard.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/kidzania.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/sealandmx-mexico.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/smartf.png,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/chedraui.jpg,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/justo.jpeg,GiftCards,3.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo-wimo.png,Paquetes,2.00
https://cdn.taecel.com/src/app/assets/img/carriers/rediC.jpg,Servicios,4.00
https://cdn.taecel.com/src/app/assets/img/carriers/logo_miia.png,Servicios,9.00
"""  # <--- Sustituye esto con toda tu lista

# Convertimos a diccionario
reader = csv.DictReader(csv_data.strip().split('\n'))
grouped = defaultdict(list)
for row in reader:
    grouped[row['Categoria']].append((row['Logo'], row['Comision']))

# HTML plantilla
html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Listado por Categorías</title>
  <style>
    body { font-family: 'Segoe UI', sans-serif; background-color: #f9f9f9; margin: 0; }
    .tabs { display: flex; background: #34495e; overflow-x: auto; }
    .tabs button {
      flex: 1; padding: 15px; background: none; border: none; color: white;
      font-size: 16px; cursor: pointer; transition: background 0.3s ease;
    }
    .tabs button:hover, .tabs button.active { background: #2c3e50; }
    .tab-content { display: none; padding: 20px; flex-wrap: wrap; gap: 20px; }
    .tab-content.active { display: flex; flex-wrap: wrap; justify-content: flex-start; }
    .card {
      width: 180px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      padding: 15px; text-align: center;
    }
    .card img { max-width: 100px; height: auto; }
    .commission { margin-top: 10px; font-weight: bold; color: #27ae60; }
  </style>
</head>
<body>

<div class="tabs">
"""

# Tabs
for i, category in enumerate(grouped):
    active = "active" if i == 0 else ""
    html += f'<button class="{active}" onclick="showTab(event, \'{category}\')">{category}</button>\n'
html += "</div>\n"

# Contenido de las pestañas
for i, (category, items) in enumerate(grouped.items()):
    active = "tab-content active" if i == 0 else "tab-content"
    html += f'<div id="{category}" class="{active}">\n'
    for logo, com in items:
        html += f"""
        <div class="card">
            <img src="{logo}" alt="Logo">
            <div class="commission">Comisión: ${com}</div>
        </div>
        """
    html += "</div>\n"

# Script
html += """
<script>
function showTab(evt, tabName) {
  var i, tabcontent, tabbuttons;
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].classList.remove("active");
  }
  tabbuttons = document.getElementsByTagName("button");
  for (i = 0; i < tabbuttons.length; i++) {
    tabbuttons[i].classList.remove("active");
  }
  document.getElementById(tabName).classList.add("active");
  evt.currentTarget.classList.add("active");
}
</script>

</body>
</html>
"""

# Guardar HTML
with open(html_filename, "w", encoding="utf-8") as f:
    f.write(html)

# Comprimir en ZIP
with ZipFile(zip_filename, 'w') as zipf:
    zipf.write(html_filename)

print(f"Archivo generado: {zip_filename}")
