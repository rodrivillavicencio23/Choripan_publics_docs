def cordenada (ejex):
    realx = 0
    letras = ["a","b","c","d","e","f","g","h"]
    for a in range(0, len(letras)):
        if ejex == letras[a]:
            realx = a
            return realx
        
cord = "a4"
cord = list(cord)
cordx = cordenada(cord[0])
cordy = int(cord[1])-1
print(cord)
print(cordx,",", cordy)