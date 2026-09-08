#clase 12.2
#comparar string con comparadores (<,>,=) sin  len nos ordena alfabéticamente
#si x = 39493249132
#para usar len con x hay que pasarlo a str -> len(str(x))
mayor = ""
seguir = True
n= 0
while seguir:
    n = str(input("word?: "))
    if n == "fin":
        seguir = False
    elif len(n) > len(mayor):
        mayor = n
print(f"the longest word is {mayor}")
