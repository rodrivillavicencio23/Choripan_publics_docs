a = 349183249134

astring = str(a)
len_astring = len(astring)
valor = 1
print(0,len(astring))

for x in range(len_astring):
    print(x)
    multi = 10**(len_astring-1)
    valor2 = int(x)
    print(multi*valor2)
    valor += 1


xd ="choripan"
print(xd[3:5])