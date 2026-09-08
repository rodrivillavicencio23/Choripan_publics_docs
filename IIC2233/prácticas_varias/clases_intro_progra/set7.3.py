#Pe causa no ocupar

#entrada = "p1,Lesionado,Si;p2,Nada,No;p3,Tercera_edad,No;p4,Nada,Si;p5,Nada,Si;p6,Tercera_edad,No;p7,Embarazada,No;p8,Nada,No"
#cajas = entrada.split(";")
#for c in range(len(cajas)):
#    cajas[c] = cajas[c].split(",")

cajas = [['p1', 'Lesionado', 'Si'],
['p2', 'Nada', 'No'],
['p3', 'Tercera_edad', 'No'],
['p4', 'Nada', 'Si'],
['p5', 'Nada', 'Si'],
['p6', 'Tercera_edad', 'No'],
['p7', 'Embarazada', 'No'],
['p8', 'Nada', 'No']]

no_colado = []
colado = []
for d in cajas:
    if d[2] == "Si":
        colado.append(d)
    else:
        no_colado.append(d)

#No colados
pref = []
no_pref = []
for e in no_colado:
    if e[1] == "Tercera_edad" or e[1] == "Embarazada":
        pref.append(e)
    else:
        no_pref.append(e)
grupo_fiel = pref+no_pref
#Colados:
pref2 = []
no_pref2 = []
for f in colado:
    if f[1] == "Tercera_edad" or f[1] == "Embarazada":
        pref2.append(f)
    else:
        no_pref2.append(f)
grupo_infiel = pref2+no_pref2

cajas = grupo_fiel + grupo_infiel
for k in cajas:
    print(k)

