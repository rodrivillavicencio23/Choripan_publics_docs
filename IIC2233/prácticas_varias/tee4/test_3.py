from collections import namedtuple

# DOS FORMAS DE CREAR LAS NAMEDTUPLES
Helicoptero = namedtuple('helicoptero_type', ['nombre', 'vida', 'origen'])
Duenos = namedtuple('duenos_type', 'nombre, nombre_mascota')

mi_24 = Helicoptero('Mi-24', 2250, 'Ruso')
ka_52 = Helicoptero('Ka-52', 2400, 'Ruso')

print(mi_24.origen)