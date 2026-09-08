# pip install z3-solver
from z3 import *

def solve_map_coloring(countries, edges, color_names=("Azul","Rojo","Verde","Amarillo")):
    """
    countries: lista de nombres de países (strings)
    edges: conjunto/lista de pares (u, v) con u!=v, vecinos (no dirigir, solo 1 vez cada arista)
    color_names: tu paleta; por defecto 3 colores
    """
    k = len(color_names)
    s = Solver()

    # C[c][d] es True ssi el país c toma el color d
    C = {
        c: [Bool(f"C_{c}_{color_names[d]}") for d in range(k)]
        for c in countries
    }

    # 1) Cada país recibe EXACTAMENTE un color (al menos uno y a lo más uno)
    for c in countries:
        s.add(AtLeast(*C[c], 1))   # al menos 1
        s.add(AtMost(*C[c], 1))    # a lo más 1

    # 2) Vecinos no pueden compartir color
    for (u, v) in edges:
        for d in range(k):
            s.add(Not(And(C[u][d], C[v][d])))

    if s.check() != sat:
        print("No hay coloración con", k, "colores.")
        return None

    m = s.model()
    coloring = {}
    for c in countries:
        for d, name in enumerate(color_names):
            if m.evaluate(C[c][d], model_completion=True):
                coloring[c] = name
                break

    return coloring

# ------------------- EJEMPLO: Sudamérica -------------------
countries = [
    "Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador",
    "Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela",
    "French_Guiana","Inglaterra"
]

edges = {
    # Argentina
    ("Argentina","Bolivia"), ("Argentina","Brazil"), ("Argentina","Chile"),
    ("Argentina","Paraguay"), ("Argentina","Uruguay"), ("Argentina","Inglaterra"),
    # Bolivia
    ("Bolivia","Brazil"), ("Bolivia","Chile"), ("Bolivia","Paraguay"),
    ("Bolivia","Peru"),
    # Brazil
    ("Brazil","Colombia"), ("Brazil","Guyana"), ("Brazil","Paraguay"),
    ("Brazil","Peru"), ("Brazil","Suriname"), ("Brazil","Uruguay"),
    ("Brazil","Venezuela"), ("Brazil","French_Guiana"), ("Brazil","Argentina"), ("Brazil","Bolivia"),
    # Chile
    ("Chile","Peru"), ("Chile","Bolivia"), ("Chile","Argentina"),
    # Colombia
    ("Colombia","Ecuador"), ("Colombia","Peru"), ("Colombia","Venezuela"),
    ("Colombia","Brazil"),
    # Ecuador
    ("Ecuador","Peru"),
    # Guyana
    ("Guyana","Suriname"), ("Guyana","Venezuela"), ("Guyana","Brazil"),
    # Paraguay
    ("Paraguay","Brazil"), ("Paraguay","Bolivia"), ("Paraguay","Argentina"),
    # Peru
    ("Peru","Brazil"), ("Peru","Chile"), ("Peru","Ecuador"), ("Peru","Colombia"), ("Peru","Bolivia"),
    # Suriname
    ("Suriname","French_Guiana"), ("Suriname","Brazil"),
    # Uruguay
    ("Uruguay","Argentina"), ("Uruguay","Brazil"),
    # Venezuela
    ("Venezuela","Brazil"), ("Venezuela","Guyana"), ("Venezuela","Colombia"),
    # French Guiana
    ("French_Guiana","Brazil"), ("French_Guiana","Suriname"),
}

coloring = solve_map_coloring(countries, edges, ("Azul","Rojo","Verde","Amarillo"))
if coloring:
    for c in sorted(coloring):
        print(f"{c:14s} -> {coloring[c]}")
