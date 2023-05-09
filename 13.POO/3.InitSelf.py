'''class FabricaTelefono()
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huawei"
telefono = FabricaTelefono()
telefono.ElaborarHuawei()
print(telefono.marca)'''

class FabricaTelefono():
    def __int__(self , marca , color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefono('Huawei' , "Negro")
print(telefono.marca)
print(telefono.color)
