sinfonia = [["fa", "mi", "fa", "mi", "do", "re"],
            ["mi", "fa"],
            ["mi", "do", "re"]]
def sincronizar(sinfonia):
    tiempos = len(sinfonia[0])-1
    for a in range (0,tiempos):
        if sinfonia[1][a] != sinfonia[0][a]:
            sinfonia[1].insert(a,"--")

    for b in range (0,tiempos):
        if sinfonia[2][a] != sinfonia[0][b]:
            sinfonia[2].insert(b,"--")
    return sinfonia

l = sincronizar(sinfonia)
print(l)
for b in sinfonia:
    print(b)