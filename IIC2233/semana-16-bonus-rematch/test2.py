import pyrematch as REmatch

# Definimos un conjunto de correos que
# necesitamos verificar si cumplen con un patrón.
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com",
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl",
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl",
       "nomail@gmail.coom", "juan.soto@uc.cl"]

# El patrón que ocuparemos es 'gmail'
pattern = r"gmail"

# Compilamos nuestro patrón en un objeto Query
query = REmatch.reql(pattern)

# Verificamos si algun string cumple con el patrón
for s in seq:
    if query.check(s):
        print(f"{s} cumple con el patrón")


