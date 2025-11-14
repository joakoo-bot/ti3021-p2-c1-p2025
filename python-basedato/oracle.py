import oracledb
import os
from dotenv import load_dotenv 

load_dotenv() 

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD") 

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn) 

table=[


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
def create_persona(rut, nombres, apellidos=None, fecha_nacimiento=None, numero_telefono=None):
    sql = (
     "INSERT INTO personas (rut, nombres, apellidos, fecha_nacimiento,numero_telefono) "
     "VALUES (:rut, :nombres, :apellidos, :fecha_nacimiento, :numero_telefono)"
     )
    if fecha_nacimiento:
         bind_fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    else:
         bind_fecha = None
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {             
             "rut": rut,
             "nombres": nombres,
             "apellidos": apellidos,
             "fecha_nacimiento": bind_fecha,
             "numero_telefono": numero_telefono,
             })
        conn.commit()
    print(f"Persona con RUT={rut} creada.")