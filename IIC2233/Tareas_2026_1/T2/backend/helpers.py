
# =============================================================================
def minutos_totales(time: str) -> int:
    """ 
    Transforma un str de hora del tipo hh:mm
    y retorna los minutos totales
    """
    horas, minutos = time.split(":")
    return int(horas) * 60 + int(minutos)

def formato_hh_mm(minutos: int) -> str:
    """
    Convierte minutos en formato
    string hh:mm
    """
    hh_mm = "%02d:%02d" % (divmod(minutos, 60))
    return hh_mm

def printear_lista(lista: list):
    """
    Printear una lista
    de ejemplo y visualizar su comportamiento
    """
    for num, elem in enumerate(lista):
        print(f"[{num}] : {elem}")

# print(formato_hh_mm(245))






