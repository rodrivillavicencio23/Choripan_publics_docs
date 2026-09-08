sinfonia = [["fa", "mi", "fa", "mi", "do", "re"],
            ["mi", "fa"],
            ["mi", "do", "re"],
            ["mi", "re"]]

#def sincronizar(sinfonia):
#    tiempos = len(sinfonia[0])-1
#    for a in range (0,tiempos):
#        if sinfonia[1][a] != sinfonia[0][a]:
#            sinfonia[1].insert(a,"--")
#    return sinfonia

def sincronizar(sinfonia):
    ejemplo = sinfonia[0]
    for a in sinfonia[1:len(sinfonia)]:
        new_inst = []
        b = 0
        for nota in ejemplo:
            if b < len(a) and a[b] == nota:
                new_inst.append(a[b])
                b +=1
            else:
                new_inst.append("--")
        print(new_inst)

    return sinfonia


ey = sincronizar(sinfonia)
for equisde in ey:
    print(equisde)