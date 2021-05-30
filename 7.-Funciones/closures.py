def saludar(username):
    mensaje = f'Hola {username}' # Variable Local

    def mostrar_mensaje(): # Anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)

username = 'Eduardo'

respuesta()
respuesta()
respuesta()