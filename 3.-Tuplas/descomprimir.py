# * -> lista
# _ -> Omitir valor

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, *_, nueve, diez = numeros

print(uno)

print(tres)
print(cuatro)

print(nueve)
print(diez)

# print(resto_numeros)
