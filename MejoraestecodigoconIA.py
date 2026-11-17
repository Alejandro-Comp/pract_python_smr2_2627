
import random

notas = []

while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

print("En mi lista tengo", notas.count(0), "ceros.")

# Eliminamos todos los ceros de una sola operación
notas = [nota for nota in notas if nota != 0]

print("Longitud de la lista:", len(notas))
print("Lista sin ceros:", notas)
