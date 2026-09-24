import itertools

nombre = input("Nombre: ").strip()
segundo_nombre = input("Segundo nombre: ").strip()
apellido1 = input("Primer apellido: ").strip()
apellido2 = input("Segundo apellido: ").strip()
ci = input("CI: ").strip()
dia = input("Día de nacimiento (dd): ").strip()
mes = input("Mes de nacimiento (mm): ").strip()
anio = input("Año de nacimiento (aaaa): ").strip()

palabras = [
    nombre,
    segundo_nombre,
    apellido1,
    apellido2,
    ci,
    dia,
    mes,
    anio,
    dia + mes,
    dia + mes + anio,
]

# Variaciones
base = set()

for p in palabras:
    if p:
        base.add(p)
        base.add(p.lower())
        base.add(p.upper())
        base.add(p.capitalize())

# Combinaciones de dos elementos
resultado = set(base)

for a, b in itertools.permutations(base, 2):
    resultado.add(a + b)

# Agregar sufijos comunes
sufijos = ["123", "1234", "2024", "2025", "2026", "@", "#", "!"]

final = set(resultado)

for palabra in resultado:
    for s in sufijos:
        final.add(palabra + s)

with open("diccionario.txt", "w", encoding="utf-8") as archivo:
    for linea in sorted(final):
        archivo.write(linea + "\n")

print(f"Se generaron {len(final)} combinaciones.")
print("Archivo guardado como diccionario.txt")