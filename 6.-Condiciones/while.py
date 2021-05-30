numero = 123456789
contador_digitos = 0

while numero >= 1:
    # contador_digitos = contador_digitos + 1
    contador_digitos += 1

    numero = numero / 10
else:
    print(contador_digitos)