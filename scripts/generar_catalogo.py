#!/usr/bin/env python3
"""Genera el catálogo de ejemplo de Floristería Aurora.

Produce:
  data/categorias.json   -> lista de categorías
  data/articulos.json    -> 38 artículos (info genérica + específica)
  public/img/*.svg       -> una imagen por artículo (ilustraciones propias, sin derechos de autor)

Uso:  python3 scripts/generar_catalogo.py
"""
import json, math, random, re, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
(RAIZ / "data").mkdir(exist_ok=True)
(RAIZ / "public" / "img").mkdir(parents=True, exist_ok=True)

CATEGORIAS = [
    ("ramos", "Ramos", "Ramos de mano listos para regalar, armados al día con flores de temporada.", "Cuidados: cortar 2 cm de los tallos en diagonal, usar agua fresca y cambiarla cada dos días."),
    ("arreglos", "Arreglos florales", "Cajas, canastas y jarrones con flores arregladas para dejar sobre la mesa.", "Cuidados: mantener la espuma o el agua húmeda y evitar el sol directo."),
    ("plantas-de-interior", "Plantas de interior", "Plantas verdes y suculentas que viven bien dentro de casa u oficina.", "Cuidados: luz indirecta y riego solo cuando el sustrato esté seco al tacto."),
    ("orquideas", "Orquídeas", "Orquídeas en maceta con varas florecidas, de larga duración.", "Cuidados: luz brillante sin sol directo y riego por inmersión una vez por semana."),
    ("bodas-y-eventos", "Bodas y eventos", "Bouquets, accesorios y decoración floral para ceremonias y celebraciones.", "Cuidados: conservar en lugar fresco y rociar con agua hasta el momento del evento."),
    ("accesorios", "Accesorios", "Jarrones, herramientas y productos para cuidar tus flores en casa.", "Uso: guardar en lugar seco y limpiar después de cada uso."),
]

# nombre, descripción, categoría, precio USD, tamaño, color, hex, ocasión, contenido
A = [
 ("Ramo Rosas Rojas Clásico","Dos docenas de rosas rojas de tallo largo, envueltas en papel kraft y listón de seda.","ramos",45,"Grande","Rojo","#c4122f","Aniversario","24 rosas rojas"),
 ("Ramo Primavera Pastel","Tulipanes, ranúnculos y eucalipto en tonos suaves, ideal para un regalo delicado.","ramos",32,"Mediano","Rosado pastel","#f3a7bd","Cumpleaños","8 tulipanes, 6 ranúnculos y eucalipto"),
 ("Ramo de Girasoles Alegría","Doce girasoles frescos con follaje verde que llenan de luz cualquier espacio.","ramos",28,"Mediano","Amarillo","#f2b705","Cumpleaños","12 girasoles"),
 ("Ramo de Lirios Blancos","Diez varas de lirios blancos de gran perfume, con hojas de aspidistra.","ramos",38,"Grande","Blanco","#f4f1ee","Gratitud","10 varas de lirio"),
 ("Ramo de Peonías Rosadas","Nueve peonías abiertas de temporada, envueltas en papel de arroz.","ramos",55,"Grande","Rosado","#e4799b","Aniversario","9 peonías"),
 ("Ramo Mini Margaritas","Treinta margaritas pequeñas en un ramo redondo y sencillo.","ramos",18,"Pequeño","Blanco","#fafafa","Detalle","30 margaritas"),
 ("Ramo Silvestre de Lavanda","Lavanda, gypsophila y espigas secas en un ramo de aire campestre.","ramos",24,"Mediano","Lila","#9b7fc7","Detalle","Lavanda, gypsophila y espigas"),
 ("Ramo Tropical de Heliconias","Heliconias, ave del paraíso y hojas de palma en colores cálidos.","ramos",48,"Grande","Naranja","#ee6c1d","Inauguración","6 heliconias y 3 aves del paraíso"),
 ("Caja Sombrerera de Rosas","Rosas rosadas en una caja redonda negra, con espuma floral hidratada.","arreglos",52,"Mediano","Rosado","#e8618c","San Valentín","18 rosas en caja"),
 ("Canasta Campestre","Canasta de mimbre con gerberas, claveles y follaje variado.","arreglos",40,"Mediano","Multicolor","#f08a4b","Cumpleaños","Gerberas, claveles y follaje"),
 ("Jarrón de Hortensias Azules","Cuatro hortensias grandes en jarrón de vidrio con agua incluida.","arreglos",46,"Mediano","Azul","#6b8fd6","Agradecimiento","4 hortensias"),
 ("Centro de Mesa Elegante","Arreglo bajo de rosas blancas y verdes para mesa de comedor o evento.","arreglos",60,"Grande","Blanco","#f1efe9","Eventos","Rosas, lisianthus y eucalipto"),
 ("Corona Floral de Condolencias","Corona de crisantemos y claveles blancos sobre base de espuma, con cinta.","arreglos",85,"Grande","Blanco","#f6f6f2","Condolencias","Crisantemos y claveles blancos"),
 ("Cesta Tropical","Cesta con anturios, ave del paraíso y hojas tropicales.","arreglos",58,"Grande","Naranja","#e8553a","Inauguración","Anturios, ave del paraíso y palma"),
 ("Caja de Tulipanes","Quince tulipanes rojos en caja de cartón rígido, listos para regalar.","arreglos",36,"Pequeño","Rojo","#d62839","Día de la Madre","15 tulipanes"),
 ("Monstera Deliciosa","Planta de hojas grandes y perforadas en maceta de 20 cm.","plantas-de-interior",35,"Mediano","Verde","#2f7d4f","Hogar","1 monstera en maceta de 20 cm"),
 ("Suculentas en Cerámica","Tres suculentas variadas en maceta de cerámica blanca.","plantas-de-interior",14,"Pequeño","Verde grisáceo","#7fa88a","Detalle","3 suculentas"),
 ("Pothos Colgante","Planta colgante de crecimiento rápido, muy fácil de cuidar.","plantas-de-interior",16,"Pequeño","Verde","#3d9660","Hogar","1 pothos en maceta colgante"),
 ("Sansevieria","Planta resistente de hojas verticales, tolera poca luz y poco riego.","plantas-de-interior",22,"Mediano","Verde oscuro","#245f3d","Oficina","1 sansevieria en maceta de 18 cm"),
 ("Ficus Lyrata","Árbol de interior con hojas anchas en forma de lira, de 80 cm de alto.","plantas-de-interior",65,"Grande","Verde","#2c7a46","Hogar","1 ficus de 80 cm"),
 ("Helecho Boston","Helecho frondoso que purifica el aire y prefiere ambientes húmedos.","plantas-de-interior",20,"Mediano","Verde claro","#58b36f","Hogar","1 helecho en maceta de 18 cm"),
 ("Set de Mini Cactus","Tres cactus pequeños en macetas de barro con base de madera.","plantas-de-interior",15,"Pequeño","Verde","#6aa96f","Detalle","3 cactus en macetas de 7 cm"),
 ("Orquídea Phalaenopsis Blanca","Orquídea de dos varas con flores blancas, en maceta decorativa.","orquideas",38,"Mediano","Blanco","#fbfaf7","Hogar","1 planta, 2 varas florecidas"),
 ("Orquídea Phalaenopsis Fucsia","Orquídea de flores fucsia intensas y floración de varios meses.","orquideas",40,"Mediano","Fucsia","#d1286f","Cumpleaños","1 planta, 2 varas florecidas"),
 ("Orquídea Cattleya Lila","Cattleya de flores grandes y perfumadas, ideal para coleccionistas.","orquideas",55,"Mediano","Lila","#b782d6","Aniversario","1 planta con 3 flores abiertas"),
 ("Orquídea Dendrobium Amarilla","Dendrobium con tallos cargados de flores amarillas pequeñas.","orquideas",34,"Mediano","Amarillo","#f0c419","Hogar","1 planta con varias varas"),
 ("Orquídea de Triple Vara","Phalaenopsis de tres varas en maceta de cerámica, un regalo de lujo.","orquideas",62,"Grande","Rosado","#ee9fc0","Aniversario","1 planta, 3 varas florecidas"),
 ("Bouquet de Novia Clásico","Bouquet en cascada de rosas blancas, peonías y eucalipto con cinta de seda.","bodas-y-eventos",95,"Grande","Blanco","#f6f1ea","Boda","Rosas, peonías y eucalipto"),
 ("Bouquet de Dama de Honor","Bouquet pequeño de rosas rosadas y ranúnculos a juego con el de la novia.","bodas-y-eventos",45,"Mediano","Rosado","#eaa0b6","Boda","Rosas y ranúnculos"),
 ("Botonier para Novio","Botonier de rosa y hojas de olivo con alfiler incluido.","bodas-y-eventos",8,"Pequeño","Blanco","#f7f4ee","Boda","1 rosa con follaje"),
 ("Corona Floral para el Cabello","Corona flexible de flores frescas y gypsophila para novias e invitadas.","bodas-y-eventos",25,"Mediano","Multicolor","#e9a4c4","Boda","Flores frescas variadas"),
 ("Pétalos de Rosa para Ceremonia","Bolsa de pétalos frescos de rosa para pasillo o lanzamiento.","bodas-y-eventos",20,"Mediano","Rojo y rosado","#d9436b","Boda","Aproximadamente 500 pétalos"),
 ("Guirnalda Floral por Metro","Guirnalda de follaje y flores para decorar mesas, arcos y escaleras.","bodas-y-eventos",30,"Grande","Verde y blanco","#7bb28a","Eventos","1 metro de guirnalda"),
 ("Jarrón de Vidrio Clásico","Jarrón transparente de 25 cm, apto para ramos de hasta 25 tallos.","accesorios",18,"Mediano","Transparente","#a9cfe0","Hogar","1 jarrón de 25 cm"),
 ("Nutriente para Flores Cortadas","Sobres de nutriente que alargan la vida de las flores en el jarrón.","accesorios",9,"Pequeño","Verde","#8bc48a","Hogar","10 sobres"),
 ("Tijeras de Podar Profesionales","Tijeras de acero inoxidable con mango antideslizante para cortes limpios.","accesorios",15,"Pequeño","Plateado","#9aa5ad","Hogar","1 tijera de 20 cm"),
 ("Espuma Floral Oasis","Dos bloques de espuma floral para sostener arreglos hidratados.","accesorios",7,"Pequeño","Verde","#6fb07a","Eventos","2 bloques"),
 ("Set de Tarjetas y Listones","Diez tarjetas de dedicatoria y dos rollos de listón de satén.","accesorios",6,"Pequeño","Multicolor","#e7a1ba","Detalle","10 tarjetas y 2 listones"),
]
DESTACADOS = {1, 5, 9, 16, 23, 28}  # posiciones (1-based) que aparecen en el inicio


def slug(t):
    t = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def flor(cx, cy, r, col, n=8):
    s = ""
    for i in range(n):
        a = 2 * math.pi * i / n
        x, y = cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a)
        s += (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r*0.5:.1f}" ry="{r*0.3:.1f}" '
              f'transform="rotate({math.degrees(a):.1f} {x:.1f} {y:.1f})" fill="{col}" stroke="#00000022" stroke-width="1"/>')
    return s + f'<circle cx="{cx}" cy="{cy}" r="{r*0.24:.1f}" fill="#f5c542"/>'


VERDE = "#3d7a55"


def svg(cat, col, i):
    rnd = random.Random(i * 7 + 3)
    fondo = ["#e9f1ea", "#f6e6ea", "#eaf0f6", "#f7efe0", "#efe8f4"][i % 5]
    b = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><rect width="600" height="600" fill="{fondo}"/>'
    b += '<ellipse cx="300" cy="560" rx="190" ry="22" fill="#00000012"/>'
    if cat in ("ramos", "bodas-y-eventos"):
        pts = [(300, 170, 60), (215, 225, 52), (385, 225, 52), (255, 140, 44), (345, 140, 44), (170, 290, 40), (430, 290, 40)]
        for x, y, r in pts:
            b += f'<path d="M300 520 Q{(300+x)/2:.0f} {(520+y)/2:.0f} {x} {y}" stroke="{VERDE}" stroke-width="7" fill="none"/>'
        b += f'<path d="M205 360 L395 360 L330 540 L270 540 Z" fill="#c9a97a"/><path d="M270 540 L330 540 L318 520 L282 520 Z" fill="#b08f60"/>'
        b += f'<path d="M250 420 L350 420" stroke="#e9d9bd" stroke-width="10"/>'
        for x, y, r in pts:
            b += flor(x, y, r, col, 8 + rnd.randint(0, 3))
        b += f'<ellipse cx="170" cy="340" rx="42" ry="14" transform="rotate(-30 170 340)" fill="{VERDE}"/><ellipse cx="430" cy="340" rx="42" ry="14" transform="rotate(30 430 340)" fill="{VERDE}"/>'
    elif cat == "arreglos":
        b += '<path d="M150 400 L450 400 L420 540 L180 540 Z" fill="#a9825a"/><path d="M150 400 L450 400" stroke="#8a6a46" stroke-width="10"/>'
        for k, (x, y, r) in enumerate([(220, 340, 54), (300, 300, 62), (380, 340, 54), (260, 390, 40), (345, 395, 40)]):
            b += f'<path d="M{x} {y} L{x} 400" stroke="{VERDE}" stroke-width="6"/>' + flor(x, y, r, col if k % 2 == 0 else "#ffffffcc", 9)
    elif cat in ("plantas-de-interior", "orquideas"):
        b += '<path d="M220 420 L380 420 L355 545 L245 545 Z" fill="#c9795a"/><rect x="210" y="405" width="180" height="26" rx="6" fill="#b4664a"/>'
        if cat == "plantas-de-interior":
            for k in range(9):
                a = -math.pi / 2 + (k - 4) * 0.34
                x, y = 300 + 190 * math.cos(a), 410 + 330 * math.sin(a) * 0.75
                b += f'<path d="M300 410 Q{(300+x)/2:.0f} {(410+y)/2-40:.0f} {x:.0f} {y:.0f}" stroke="#2c6b45" stroke-width="5" fill="none"/>'
                b += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="46" ry="24" transform="rotate({math.degrees(a)+90:.0f} {x:.0f} {y:.0f})" fill="{col}"/>'
        else:
            b += f'<path d="M300 410 C300 250 330 170 420 150" stroke="{VERDE}" stroke-width="7" fill="none"/>'
            for k, (x, y, r) in enumerate([(308, 330, 38), (322, 262, 36), (355, 205, 34), (405, 170, 30), (440, 150, 24)]):
                b += flor(x, y, r, col, 5)
            b += '<ellipse cx="250" cy="400" rx="70" ry="18" transform="rotate(-12 250 400)" fill="#2c6b45"/><ellipse cx="350" cy="400" rx="70" ry="18" transform="rotate(12 350 400)" fill="#2c6b45"/>'
    else:  # accesorios
        b += f'<path d="M230 230 Q210 330 235 540 L365 540 Q390 330 370 230 Z" fill="{col}" opacity=".55" stroke="#ffffff" stroke-width="5"/>'
        b += f'<path d="M300 520 L300 200" stroke="{VERDE}" stroke-width="6"/>' + flor(300, 170, 48, "#f4a9c0", 8)
    return b + "</svg>"


categorias = []
articulos = []
for i, (nombre, desc, cat, precio, tam, color, hexa, ocasion, contenido) in enumerate(A, start=1):
    aid = slug(nombre)
    img = f"/img/{aid}.svg"
    (RAIZ / "public" / "img" / f"{aid}.svg").write_text(svg(cat, hexa, i), encoding="utf-8")
    articulos.append({
        "id": aid,
        "nombre": nombre,
        "descripcion": desc,
        "categoria": cat,
        "imagen": img,
        "etiquetas": sorted({slug(color).replace("-", " "), slug(ocasion).replace("-", " "), cat.replace("-", " ")}),
        "destacado": i in DESTACADOS,
        "precio": precio,
        "tamano": tam,
        "color": color,
        "ocasion": ocasion,
        "contenido": contenido,
    })

for slg, nombre, desc, cuidados in CATEGORIAS:
    primero = next(a for a in articulos if a["categoria"] == slg)
    categorias.append({"slug": slg, "nombre": nombre, "descripcion": desc, "cuidados": cuidados, "imagen": primero["imagen"]})

(RAIZ / "data" / "categorias.json").write_text(json.dumps(categorias, ensure_ascii=False, indent=2), encoding="utf-8")
(RAIZ / "data" / "articulos.json").write_text(json.dumps(articulos, ensure_ascii=False, indent=2), encoding="utf-8")
(RAIZ / "public" / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#1f3d2f"/>'
    + flor(50, 50, 30, "#f2a3bd", 8) + "</svg>", encoding="utf-8")
print(f"{len(articulos)} artículos, {len(categorias)} categorías")
