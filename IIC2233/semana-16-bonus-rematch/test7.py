import pyrematch as REmatch

document = 'Jotate@19,Rodri@23,Chori@67'
pattern = "(^|,)!text{!name{[^,]+}@!number{[^,]+}}($|,)"
query = REmatch.reql(pattern)

print("=" * 40)

for match in query.finditer(document):
    print("El texto encontrado fue " + match.group('text') + "\n", 
          match.group('name'), "-", match.group('number'))
    
print("=" * 40)