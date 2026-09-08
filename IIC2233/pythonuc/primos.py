def es_primo(numero):
    if numero < 2:
        return False #0 y 1 no son primo
    if numero == 2:
        return True #2 es primo
    if numero % 2 == 0:
        return False #el número es par, entonces no es primo
    
    mitad_numero = (numero//2)+1
    for divisor in range(3,mitad_numero,2):
        if numero % divisor == 0:
            return False
    return True
        
    
# --- Buscar números primos en un rango grande ---

for numero in range(100, 10000):
    primo_o_no = es_primo(numero)
    if primo_o_no:
        print(f"{numero}: es primo")
    else:
        print(f"{numero}: no es primo")