canciones = [
    ("DÁKITI", "El Último Tour del Mundo", 2309459229, 658316),
    ("LA CANCIÓN", "OASIS", 2242406402, 1170360),
    ("Me Porto Bonito", "Un Verano Sin Ti", 2135068638, 599988),
    ("Tití Me Preguntó", "Un Verano Sin Ti", 1884686112, 558198),
    ("I Like It", "sencillo", 1788274474, 563551),
    ("Ojitos Lindos", "Un Verano Sin Ti", 1768784091, 653551),
    ("Callaita", "sencillo", 1719846933, 621551),
    ("No Me Conoce - Remix", "sencillo", 1659513074, 438238),
    ("Yonaguni", "sencillo", 1569088687, 426875),
    ("Efecto", "Un Verano Sin Ti", 1548549781, 497551),
    ("MIA", "X 100PRE", 1484488575, 384956),
    ("Moscow Mule", "Un Verano Sin Ti", 1432904504, 736851),
    ("un x100to", "sencillo", 1389767287, 586978),
    ("Te Boté - Remix", "sencillo", 1290343647, 487551),
    ("PERRO NEGRO", "Nadie Sabe Lo Que Va a Pasar Mañana", 1168241501, 405493),
    ("La Santa", "YHLQMDLG", 1137647201, 435839),
    ("Diles", "sencillo", 1132552872, 463463),
    ("Soltera (Remix)", "YHLQMDLG", 1118629687, 491922),
    ("LA NOCHE DE ANOCHE", "El Último Tour del Mundo", 1117305085, 253375),
    ("DtMF", "DeBÍ TiRAR MáS FOToS", 1114429740, 252375),
    ("Vete", "YHLQMDLG", 1114287146, 252375),
    ("Si Estuviésemos Juntos", "X 100PRE", 1113745811, 405861),
    ("Lo Siento BB:", "Nadie Sabe Lo Que Va a Pasar Mañana", 1066865087, 587922),
    ("QUE PRETENDES", "OASIS", 1009264764, 252375),
    ("Neverita", "Un Verano Sin Ti", 998481357, 405375),
    ("Safaera", "YHLQMDLG", 991485375, 405375),
    ("Si Veo a Tu Mamá", "YHLQMDLG", 978448975, 252375),
    ("UN DIA (ONE DAY)", "sencillo", 930597552, 252871),
    ("Tarot", "Un Verano Sin Ti", 911485375, 405375),
    ("Volví", "sencillo", 901752508, 252375),
    ("A Tu Merced", "YHLQMDLG", 899485375, 405375),
    ("BAILE INOLVIDABLE", "DeBÍ TiRAR MáS FOToS", 899485375, 191422),
    ("WHERE SHE GOES", "sencillo", 898985375, 324375),
    ("CÓMO SE SIENTE - Remix", "Las Que No Iban a Salir", 898985375, 324375),
    ("Party", "Un Verano Sin Ti", 851265237, 291375)
]

albumes = [("DeBÍ TiRAR MáS FOToS", 2025),
           ("Nadie Sabe Lo Que Va a Pasar Mañana", 2023),
            ("Un Verano Sin Ti", 2022),
            ("YHLQMDLG", 2020),
            ("Oasis", 2019)
        ]

def imprimir_lista(lista: list):
    for a in lista:
        print(a)
    return len(lista)


canciones = filter(lambda x: x[3] >= 600000, canciones)

print(imprimir_lista(list(canciones)))