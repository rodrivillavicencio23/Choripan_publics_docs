def contar (x,y):
    contar = 0
    for letra in x:
        if y in letra:
            contar +=1
    return contar

print(contar("cabrontunnove","o"))



s = "colocolo"

c_s = s.count("c")
print(c_s)