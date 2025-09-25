class Cliente:
    def __init__(self, nombre:str, rut:str , edad:int):
        self.__nombre: str =nombre
        self.__rut : str = rut
        self.__edad:int = edad

        @property
        def nombre(self):
            return self.__nombre

Cliente1 :Cliente = Cliente (
    nombre="joaquin villarroel ",
    rut= "22408908-2",
    edad=21
)

print(Cliente1)