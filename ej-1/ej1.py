class Nodo():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.conexiones = []
    
    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
        
    def enviar_mensaje(self, mensaje, usuarios):
        for usuario in usuarios:
            if usuario in self.conexiones:
                usuario.recibir_mensaje(mensaje)
            else:
                print(f"El nodo {usuario.nombre} no está conectado a este nodo.")

    def recibir_mensaje(self, mensaje):
        print(f"El nodo {self.nombre} ha recibido el mensaje: {mensaje}")
        
# Crear nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

# Conectar nodos
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

# Lista de usuarios a los que enviar el mensaje
usuarios = [cliente1, cliente2, cliente3]

# Enviar mensaje a todos los usuarios
servidor.enviar_mensaje("Hola a todos", usuarios)
