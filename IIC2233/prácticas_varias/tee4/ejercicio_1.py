# MIDTERM 2024-2
# PREGUNTA 20

def printear(lista):
    for a in lista:
        print(a)


fondas = {"Choripan": 4,
          "Sopaipillas": 3,
          "Anticuchos": 6,
          "Asado": 0}


var_1 = filter(lambda x: len(x) > 0, fondas.keys())

var_1_5 = filter(lambda x: x % 2 == 0, fondas.values())

var_2 = map(lambda x: x * 2, var_1_5)


#printear(var_1)

#printear(var_2)

print(list(zip(var_1, var_2)))