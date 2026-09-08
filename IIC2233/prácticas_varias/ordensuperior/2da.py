from uso_map import imprimir_lista

# Formato: (nombre, departamento, salario, antigüedad_en_años)
empleados = [
    ("Ana Torres", "Ventas", 1200, 3),
    ("Luis Pérez", "Marketing", 1500, 5),
    ("Carla Gómez", "Ventas", 1350, 2),
    ("Pedro Ruiz", "TI", 2000, 7),
    ("Sofía Díaz", "TI", 2200, 10),
    ("Javier López", "Marketing", 1600, 4),
    ("María Herrera", "RRHH", 1400, 6),
    ("Andrés Silva", "RRHH", 1300, 1),
    ("Valentina Castro", "Ventas", 1450, 4),
    ("Rodrigo Soto", "TI", 2100, 8),
    ("Camila Vargas", "Marketing", 1550, 3),
    ("Felipe Rojas", "Ventas", 1250, 2),
    ("Ignacio Fuentes", "TI", 2300, 12),
    ("Paula Morales", "RRHH", 1350, 2),
    ("Diego Contreras", "Marketing", 1700, 6),
    ("Fernanda Reyes", "Ventas", 1400, 5),
    ("Tomás Navarro", "TI", 1950, 6),
    ("Isabel Paredes", "RRHH", 1450, 7),
    ("Cristóbal Vega", "Marketing", 1650, 4),
    ("Martina León", "Ventas", 1500, 3),
    ("Ivan06", "Ventas", 1500, 5)
]
# Formato: (departamento, bono)

departamento = [("Ventas", 0.25),
                ("Marketing", 0.3),
                ("RRHH", 0.35),
                ("TI", 0.4)]
# Formato: (producto, categoría, precio_unitario, stock)
productos = [
    ("Laptop", "Electrónica", 950, 12),
    ("Mouse", "Electrónica", 25, 150),
    ("Escritorio", "Muebles", 200, 20),
    ("Silla", "Muebles", 80, 50),
    ("Impresora", "Electrónica", 120, 30),
    ("Cuaderno", "Papelería", 2, 500),
    ("Bolígrafo", "Papelería", 1, 1000),
    ("Lámpara", "Muebles", 35, 40),
    ("Monitor", "Electrónica", 180, 25),
    ("Teclado", "Electrónica", 30, 100),
    ("Archivador", "Muebles", 60, 35),
    ("Calculadora", "Papelería", 15, 80),
    ("Auriculares", "Electrónica", 50, 70),
    ("Mesa de Reunión", "Muebles", 300, 10),
    ("Agenda", "Papelería", 5, 200),
    ("Router", "Electrónica", 70, 40),
    ("Sofá", "Muebles", 400, 5),
    ("Pizarra", "Papelería", 25, 30),
    ("Cámara Web", "Electrónica", 60, 50),
    ("Estantería", "Muebles", 150, 15)
]
# Formato: (id_venta, producto, cantidad, vendedor)
ventas = [
    (101, "Laptop", 2, "Ana Torres"),
    (102, "Mouse", 5, "Carla Gómez"),
    (103, "Silla", 3, "Luis Pérez"),
    (104, "Impresora", 1, "Pedro Ruiz"),
    (105, "Cuaderno", 50, "Javier López"),
    (106, "Bolígrafo", 100, "María Herrera"),
    (107, "Lámpara", 2, "Andrés Silva"),
    (108, "Laptop", 1, "Ana Torres"),
    (109, "Monitor", 3, "Valentina Castro"),
    (110, "Teclado", 10, "Rodrigo Soto"),
    (111, "Archivador", 4, "Camila Vargas"),
    (112, "Calculadora", 6, "Felipe Rojas"),
    (113, "Auriculares", 8, "Ignacio Fuentes"),
    (114, "Mesa de Reunión", 1, "Paula Morales"),
    (115, "Agenda", 20, "Diego Contreras"),
    (116, "Router", 2, "Fernanda Reyes"),
    (117, "Sofá", 1, "Tomás Navarro"),
    (118, "Pizarra", 3, "Isabel Paredes"),
    (119, "Cámara Web", 5, "Cristóbal Vega"),
    (120, "Estantería", 2, "Martina León")
]


# filtrar 1 lista: 
equisde = filter(lambda x: x[3] >= 5, empleados)

print(imprimir_lista(list(equisde)))

def bono_empleado(lista_empleados: list, lista_departamento: list,
                    rango_edad: int, sueldo_max: int):
    
    """Recibe una lista de empleados donde a cada empleado que cumpla
    con un tiempo de antiguedad menor o igual que rango_edad y su sueldo sea menor
    que sueldo_max se le asigne un bono en relación al departamento que pertenece.
    
    Se debe retornar una lista de tuplas con: nombre empleado, departamento, y bono
    (salario * )"""
    pass