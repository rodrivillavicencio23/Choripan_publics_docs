#Variables

chocolates = int(input("¿Cuántos chocolates hay?"))
personas = int(input("¿Cuántas personas hay?"))

#Condición

if personas > chocolates:
    print("no hay chance pibe, no alcanzan los chocolates")
elif chocolates >= personas:
    print("Bien pibe, alcanza para todos")