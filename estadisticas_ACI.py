notas = [7, 4, 9, 3, 6, 8, 5]

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Nota media:", sum(notas) / len(notas))

print("¿Hay algún suspenso?", any(nota < 5 for nota in notas))

print("¿No hay ningún cero?", all(nota != 0 for nota in notas))