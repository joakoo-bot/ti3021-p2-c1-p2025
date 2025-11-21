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
    rut="22400419-2",
    nombres="pepe",
    apellidos="melo",
    fecha_nacimiento="11-05-2002",
    numero_telefono="989864544",
    correo="el_vio@gmail.com"
);

create_cliente(
    rut="18355987-7",
    nombres="Carlos",
    apellidos="Ramírez",
    fecha_nacimiento="22-09-1998",
    numero_telefono="945672310",
    correo="c.ramirez@example.com"
);

create_cliente(
    rut="20988765-3",
    nombres="María",
    apellidos="López",
    fecha_nacimiento="14-03-2001",
    numero_telefono="987452130",
    correo="m.lopez@example.com"
);

create_cliente(
    rut="17544329-4",
    nombres="Javier",
    apellidos="Fuentes",
    fecha_nacimiento="30-12-1995",
    numero_telefono="923118540",
    correo="j.fuentes@example.com"
);

create_cliente(
    rut="22687912-1",
    nombres="Daniela",
    apellidos="Pérez",
    fecha_nacimiento="05-07-2000",
    numero_telefono="981224709",
    correo="d.perez@example.com"
);


def create_pedido(
                    numero:int, 
                    fecha:str, 
                    RUTcliente:str, 
                    total_a_pagar:int
):
    sql={
       "INSERT INTO CLIENTE (numero,fecha,RUTcliente,total_a_pagar)"
       "VALUES(:numero,:fecha,:RUTcliente,:total_a_pagar)"
   }
    parametros= {
       "numero":numero,
       "RUTcliente":RUTcliente,
       "total_a_pagar":total_a_pagar,
       "fecha":datetime.strptime(fecha,"%y-%m-%d")
   }
    def create_pedido(query):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    print(f"Tabla creada \n {parametros}")
                conn.commit()
        except oracledb.DatabaseError as e:
            err = e
            print(f"No se pudo crear la tabla: {err} \n {parametros}")

create_pedido(
    numero=1, 
    fecha="11-10-2025", 
    RUTcliente="22400419-2", 
    total_a_pagar=24000
);
create_pedido(
    numero=2, 
    fecha="11-10-2025", 
    RUTcliente="18355987-7", 
    total_a_pagar=62500
);
create_pedido(
    numero=3, 
    fecha="11-10-2025", 
    RUTcliente="20988765-3", 
    total_a_pagar=15200
);
create_pedido(
    numero=4, 
    fecha="11-10-2025", 
    RUTcliente="17544329-4", 
    total_a_pagar=100000
);
create_pedido(
    numero=5, 
    fecha="11-10-2025", 
    RUTcliente="22687912-1", 
    total_a_pagar=33500
);
    

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

from typing import Optional 
#update

def update_cliente(
        rut,
        nombres: Optional[str]=None , 
        apellidos: Optional[str]=None , 
        fecha_nacimiento: Optional[str]=None ,
        numero_telefono: Optional[str]=None ,
        correo: Optional[str]=None 

):
    modificaciones=[]
    parametros=("rut"=rut) 
