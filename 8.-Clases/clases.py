# Attrs de clase
# Attrs de instancia

class Usuario:

    # Object
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    def saludar(self):
        mensaje = self.obtener_mensaje()
        print(mensaje)

    def obtener_mensaje(self):
        return f'Hola, {self.username} te saluda.'

cody = Usuario('Cody')
cody.saludar()