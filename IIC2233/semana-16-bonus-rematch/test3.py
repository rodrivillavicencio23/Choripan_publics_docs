import pyrematch as REmatch

numeros = ["+56 942021999", "+57931316921", "+56 94591740"]

pattern_2 = r"^(\+56)\s[\d]+"
query_2 = REmatch.reql(pattern_2)


for s in numeros:
    if query_2.check(s):
        print(f"{s} cumple con el patrón")


nombres = ["Agustin Villavicencio", "Tiara Donoso", "Jotate", "lucasCepeda", "nombre apellido"]

pattern_3 = r"[A-Z]{1}\w+\s[A-Z]{1}\w+"
query_3 = REmatch.reql(pattern_3)

for s in nombres:
    if query_3.check(s):
        print(f"{s} cumple con el patrón")

