from datetime import date

class persona:
    def __init__(self,nombres:str,apellidos:str,rut:str,fecha_nacimiento:date,telefono:int,codigo_area:int):
        self.rut :str =rut 
        self.nombres:str=nombres 
        self.apellidos:str=apellidos 
        self.fecha_nacimiento:date=fecha_nacimiento
        self.telefono:int=telefono
        self.codigo_area:int=codigo_area


def __str__(self):
    return f"{self.rut}{self.nombres}{self.apellidos}{self.fecha_nacimiento}{self.telefono}{self.codigo_area}"


personas : list[persona] = []



def create_personas():
    rut:str = input("ingresa el rut de la persona: ")
    nombres:str = input("ingresa los nombres de la persona: ")
    epellidos:str= input("ingresa los nombres de la persona: ")
    telefono:int= int(input("ingresa el rut de la persona: "))
    cod_area:int = int(input("ingresa los nombres de la persona: "))
    fecha_nacimiento:date = date(
        year = anio_nacimiento,
        mont = mes_nacimiento , 
        day = dia_nacimiento
        )
    
    persona = persona(
        rut=rut,
        nombres=nombres,
        fecha_nacimiento=fecha_nacimiento,
        apellidos=epellidos,
        telefono=telefono,
        cod_area=cod_area
    )
if persona_existe(persona):
    return print (f"la persona con el rut{persona.rut} ya existe. intente con otro rut")


def read_personas():
    for personas in personas:
        print(persona)

def update_personas():
    pass  

def delete_peronas():
    pass
def persona_existe(persona_nueva:persona)-> bool:
    for persona in personas :
        if personas.rut == persona_nueva.rut:
            print("persona existe")
    print("persona no existe")
    return False  


