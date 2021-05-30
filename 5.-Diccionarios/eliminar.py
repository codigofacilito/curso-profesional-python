diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(diccionario))

del diccionario['a'] # 1
valor = diccionario.pop('b') # 2

diccionario.clear()

print(valor)

print(diccionario)
print(len(diccionario))