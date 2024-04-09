class Nodo():
    def __init__(self,nom) -> None:
        self.nombre = nom
        self.conexiones = []
    
    def agregar_conexion (self, nodo):
        self.conexiones.append(nodo)
        
    def enviar_mensaje(self, mensaje):
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"El nodo {self.nombre} ha recibido el mensaje: {mensaje}")
        
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")

servidor.agregar_conexion(cliente1)

servidor.enviar_mensaje("hola")