def lower(string: str) -> str:
    return string.lower()

def upper(string: str) -> str:
    return string.upper()

strings = ['Señores pasajeros', 'Disculpen', 'mi', 'IntencIÓN', 'no', 'Es', 'MolEstar']
mapeo = map(upper, strings)

print(', '.join(mapeo))



# SIN FUNCIÓN APARTE
mapeo_2 = list(map(lambda x: x.lower(), strings))

print(mapeo_2)