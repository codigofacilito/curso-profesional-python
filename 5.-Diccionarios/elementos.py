diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)

"""
valor = diccionario['z']
print(valor)
"""

# get
# setdefault
valor = diccionario.setdefault('e', 5)

print(valor)
print(diccionario)