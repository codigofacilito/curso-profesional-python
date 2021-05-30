"""
a -> La función principal (Decorador)
b -> La función de decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print('>>> Antes del llamado.')
        
        resultado = funcion_b(*args, **kwargs)

        print('>>> Después del llamado.')

        return resultado
    
    return funcion_c


@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(15, 60)
print(resultado)