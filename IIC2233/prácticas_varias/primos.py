"""
--- Función para verificar si un número es primo ---
"""
def es_primo(numero):
    if numero % 2 == 0 and numero != 2:
        print("número es par")
        return False
    else:
        for a in range(2, numero):
            if numero % a == 0:
                print(f"el número {numero} es divisible por {a}")
                return False
    return True


"""
--- Ciclo for para verificar entre rangos si existe algún número primo,
si lo encuentra rompe el ciclo y devuelve el número ---
"""
for number in range(1000000000,1000200000):
    print(number)
    primo_o_no = es_primo(number)
    if primo_o_no:
        print(f"Se encontró un número primo: {number}")
    else:
        pass

