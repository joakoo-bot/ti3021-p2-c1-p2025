import oracledb
import os
from dotenv import load_dotenv 

load_dotenv() 

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD") 

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn) 


def create_schema(query):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Tabla creada \n {query}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo crear la tabla: {err} \n {query}")


tables=[


    (  "CREATE TABLE cliente ("
            "rut VARCHAR2(50) PRIMARY KEY,"
            "nombres VARCHAR2(200),"
            "apellidos VARCHAR2(200),"
            "numero_telefono VARCHAR2(50)," 
            "correo VARCHAR2(100)"
            ")"

        "CREATE TABLE repartidor ("
            "rut VARCHAR2(50) PRIMARY KEY,"
            "nombres VARCHAR2(200),"
            "apellidos VARCHAR2(200),"
            "numero_telefono VARCHAR2(50)," 
            "correo VARCHAR2(100)"
            ")" 

        "CREATE TABLE pedido ("
            "numero int PRIMARY KEY,"
            "fecha date,"
            "total a pagar int,"
            "RUTcliente VARCHAR2(50)," 
            "FOREIGN KEY (RUTcliente) REFERENCES cliente(rut)"
            ")" 
    
        "CREATE TABLE pedido_domicilio ("
            "direccion  VARCHAR2(100),"
            "RUTrepartidor VARCHAR2(50),"
            "Npedido int ," 
            "FOREIGN KEY (RUTrepartidor) REFERENCES repartidor(rut),"
            "FOREIGN KEY (Nperdido) REFERENCES pedido(numero)"
            ")" 

        "CREATE TABLE pedido_local ("
            "numero_mesa int,"
            "Npedido int ," 
            "FOREIGN KEY (Nperdido) REFERENCES pedido(numero)"
            ")" 

        "CREATE TABLE pedido_llevar ("
            "tiempo estimado int,"
            "Npedido int ," 
            "FOREIGN KEY (Nperdido) REFERENCES pedido(numero)" 
            ")"
    )
]

for query in tables:
    create_schema(query)


from datetime import datetime
##CREATE
def create_cliente(
                    rut:str, 
                   nombres:str, 
                   apellidos:str, 
                   fecha_nacimiento:str, 
                   numero_telefono:str,
                   correo:str
):
   sql={
       "INSERT INTO CLIENTE (rut,nombres,apellidos,fecha_nacimiento,numero_telefono,correo)"
       "VALUES(:rut,:nombres,apellidos,:fechas_nacimiento,numero_telefono,:correo)"
   }

   parametros = {
       "rut":rut,
       "nombres": nombres,
       "apellidos":apellidos,
       "fecha_nacimiento":datetime.strptime(fecha_nacimiento,"%y-%m-%d"),
       "numero_telefono":numero_telefono,
       "correo":correo
   }
   def create_cliente(query):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Tabla creada \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo crear la tabla: {err} \n {parametros}")

create_cliente(
    rut="22400419"
    nombres=
    apellidos=
    fecha_nacimiento=
    numero_telefono=
    correo=

):


def create_pedido(
                    numero:int, 
                    fecha:str, 
                    RUTcliente:str, 
                    total_a_pagar:int
):
    pass   

def create_repartidor(
                    rut:str, 
                   nombres:str, 
                   apellidos:str, 
                   fecha_nacimiento:str, 
                   numero_telefono:str,
                   correo:str
):
    pass  

def create_pedido_local(
                        numero_mesa :int,
                        Npedido:int
):
    pass   

def create_pedido_llevar(
                        tiempo_estimado: int,
                        Npedido:int,
                        
):
    pass   

def create_pedido_domicilio(
                            direccion :int,
                            Npedido: int,
                            RUTrepartidor : str, 
                            
):
    pass  