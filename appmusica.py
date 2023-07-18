class AppMusica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.artistas = []
        self.canciones = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_artista(self, artista):
        self.artistas.append(artista)

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.nombre}")

    def mostrar_artistas(self):
        for artista in self.artistas:
            print(f"Artista: {artista.nombre}")

    def mostrar_canciones(self):
        for cancion in self.canciones:
            print(f"Cancion: {cancion.nombre} de {cancion.artista.nombre}")

    def metodo_nuevo():
        pass