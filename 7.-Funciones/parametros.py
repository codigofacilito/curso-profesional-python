def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)


def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance
    
    def retiro(n1, n2):
        return cantidad - balance
    
    if tipo == 'deposito':
        return deposito(cantidad, balance)

    elif tipo == 'retiro':
        return deposito(cantidad, balance)

    # Por default las funciones en Python retornara None