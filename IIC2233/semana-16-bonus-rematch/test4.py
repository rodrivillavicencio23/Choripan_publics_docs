import re

""" 
Enunciado: 
El Extractor de Logs (Análisis de Sistemas)
Cuando un servidor falla, genera miles de líneas de texto. Tu misión es extraer información crítica de ellos.

El desafío: Dado un string de log, extrae únicamente la IP, la Fecha/Hora y el Mensaje de Error solo si el estatus es ERROR o CRITICAL.

Texto de prueba:
[2026-06-15 14:32:01] [192.168.1.45] [INFO] Usuario inició sesión.
[2026-06-15 14:33:12] [200.45.12.112] [ERROR] Conexión a la base de datos fallida.

Tip: Usa grupos de captura () con re.search() o re.findall() para separar la IP del mensaje.

"""
string_lock = """[2026-06-15 14:32:01] [192.168.1.45] [INFO] Usuario inició sesión. 
                [2067-06-15 14:33:12] [200.45.12.112] [ERROR] Conexion a la base de datos fallida. 
                [2000-01-11 14:33:12] [200.45.12.112] [CRITICAL] El jotate se ha metido a la base de datos."""

ejemplos = ["[2026-06-17] [200.45.12.112] [ERROR] a.",
             "[2025-05-15][ERROR]",
             "[2026-06-15 14:33:12] [200.45.12.112] [ERROR] Conexion a la base de datos fallida.",
             "[2000-01-11 14:33:12] [200.45.12.112] [CRITICAL] El jotate se ha metido a la base de datos, mish."]


print("=" * 30, "\nVerificar Lista :\n", "=" * 30)

patron = r"(\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\])\s+(\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\])\s+\[(?:ERROR|CRITICAL)\]\s+(.+)"

for s in ejemplos:
    if re.match(patron, s):
        print(s)

print("=" * 30, "\nVerificar string completo :\n", "=" * 30)

coincidencias = re.finditer(patron, string_lock)
print(coincidencias)
for match in coincidencias:
    # .group(0) es toda la línea que coincidió
    # .group(1), (2), (3) son nuestros paréntesis de captura
    fecha = match.group(1)
    ip = match.group(2)
    mensaje = match.group(3)
    
    print(f"Alerta detectada:")
    print(f"   Fecha:   {fecha}")
    print(f"   IP:      {ip}")
    print(f"   Mensaje: {mensaje}\n")

# Development . . .
# =========================================================

patron_2 = r"\[\d{4}-\d{2}-\d{2}\]\s"
patron_3 = r"(\[ERROR\])\s.+\."

# patron 2
if re.match(patron_2, "[2026-15-11] "):
    print("cumple patrón 2\n")

# patron 3
if re.match(patron_3, "[ERROR] Hola bro."):
    print("cumple patrón 3\n")

# =========================================================