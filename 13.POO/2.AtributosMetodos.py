class FabricaTelefono():
    marca = "Huawei"
    color = "negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self , mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando Musica")

telefono = FabricaTelefono()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar("Hola, ¿Con quien hablo?"))
telefono.escucharMusica()