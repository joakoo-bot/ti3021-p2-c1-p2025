class cliente:
    def __init__(self, nombre:str,apellido:str,run:int,numero_verificador:int,telefono:str,correo:str):
     self.__nombre:str=nombre
     self.__apellido:str=apellido
     self.__run:int=run
     self.__numero_vereficador:int=numero_verificador
     self.__telefono:str=telefono
     self.__correo:str=correo


    @property
    def nombre(self):
        return self.__nombre 
    @property
    def apellido(self):
        return self.__apellido
    @property
    def run(self):
        return self.__run
    @property
    def numero_verificador(self):
        return self.__numero_vereficador
    @property
    def telefono(self):
        return self.__telefono
    @property
    def correo(self):
        return self.__correo
     
class pedido: 
    def __init__(self,numero:int , fecha:int ,total_a_pagar:int):
        self.__numero:int=numero 
        self.__fecha:int=fecha 
        self.__total_a_pagar:int=total_a_pagar 
        
    @staticmethod
    def prosesar(procesar):
        print(procesar)
    
    @property
    def numero(self):
        return self.__numero
    @property
    def fecha(self):
        return self.__fecha
    @property
    def total_a_pagar(self):
        return self.__total_a_pagar  
    