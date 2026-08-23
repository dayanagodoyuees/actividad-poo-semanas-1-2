class Cliente:

    def __init__(self, cedula, nombre, telefono, estado):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__telefono = telefono
        self.__estado = estado

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_estado(self):
        return self.__estado

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_estado(self, estado):
        self.__estado = estado

    def mostrar_datos(self):
        print("Cédula:", self.__cedula)
        print("Nombre:", self.__nombre)
        print("Teléfono:", self.__telefono)
        print("Estado:", self.__estado)