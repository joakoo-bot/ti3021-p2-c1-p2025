import oracledb
import os
from dotenv import load_dotenv  
from typing import Optional 

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
            "id INT(100) PRIMARY KEY,"
            "rut VARCHAR2(50),"
            "nombres VARCHAR2(200),"
            "apellidos VARCHAR2(200),"
            "numero_telefono VARCHAR2(50)," 
            "correo VARCHAR2(100)"
            ")"

        "CREATE TABLE repartidor ("
            "id VARCHAR2(50) PRIMARY KEY,"
            "rut VARCHAR2(50),"
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
            "FOREIGN KEY (Npedido) REFERENCES pedido(numero)"
            ")" 

        "CREATE TABLE pedido_local ("
            "numero_mesa int,"
            "Npedido int ," 
            "FOREIGN KEY (Npedido) REFERENCES pedido(numero)"
            ")" 

        "CREATE TABLE pedido_llevar ("
            "tiempo estimado int,"
            "Npedido int ," 
            "FOREIGN KEY (Npedido) REFERENCES pedido(numero)" 
            ")"
    )
]

for query in tables:
    create_schema(query)


from datetime import datetime
##CREATE
def create_cliente(
                    id:int,
                    rut:str, 
                   nombres:str, 
                   apellidos:str, 
                   fecha_nacimiento:str, 
                   numero_telefono:str,
                   correo:str
):
    sql={
        "INSERT INTO CLIENTE (id,rut,nombres,apellidos,fecha_nacimiento,numero_telefono,correo)"
        "VALUES(:id,:rut,:nombres,apellidos,:fechas_nacimiento,numero_telefono,:correo)"
    }

    parametros = {
        "id":id,
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
    id=1,
    rut="22400419-2",
    nombres="pepe",
    apellidos="melo",
    fecha_nacimiento="11-05-2002",
    numero_telefono="989864544",
    correo="el_vio@gmail.com"
);
create_cliente(
    id=2,
    rut="18355987-7",
    nombres="Carlos",
    apellidos="Ramírez",
    fecha_nacimiento="22-09-1998",
    numero_telefono="945672310",
    correo="c.ramirez@example.com"
);
create_cliente(
    id=3,
    rut="20988765-3",
    nombres="María",
    apellidos="López",
    fecha_nacimiento="14-03-2001",
    numero_telefono="987452130",
    correo="m.lopez@example.com"
);
create_cliente(
    id=4,
    rut="17544329-4",
    nombres="Javier",
    apellidos="Fuentes",
    fecha_nacimiento="30-12-1995",
    numero_telefono="923118540",
    correo="j.fuentes@example.com"
);
create_cliente(
    id=5,
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
    sql={
        "INSERT INTO CLIENTE (id,rut,nombres,apellidos,fecha_nacimiento,numero_telefono,correo)"
        "VALUES(:id,:rut,:nombres,apellidos,:fechas_nacimiento,numero_telefono,:correo)"
    }

    parametros = {
        "id":id,
        "rut":rut,
        "nombres": nombres,
        "apellidos":apellidos,
        "fecha_nacimiento":datetime.strptime(fecha_nacimiento,"%y-%m-%d"),
        "numero_telefono":numero_telefono,
        "correo":correo
    }
    
    def create_repartidor(query):
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
    id="c1",
    rut="20345678-5",
    nombres="Juan",
    apellidos="Pérez",
    fecha_nacimiento="15-03-1999",
    numero_telefono="912345678",
    correo="juan.perez@gmail.com"
);
create_cliente(
    id="c3",
    rut="18900543-7",
    nombres="María",
    apellidos="López",
    fecha_nacimiento="28-11-2001",
    numero_telefono="987654321",
    correo="maria.lopez@hotmail.com"
);
create_cliente(
    id="c7",
    rut="22488991-4",
    nombres="Carlos",
    apellidos="González",
    fecha_nacimiento="02-07-1995",
    numero_telefono="945612378",
    correo="c.gonzalez@yahoo.com"
);
create_cliente(
    id="c12",
    rut="17890234-6",
    nombres="Fernanda",
    apellidos="Riquelme",
    fecha_nacimiento="09-01-2003",
    numero_telefono="934567812",
    correo="fernanda.riquelme@gmail.com"
);
create_cliente(
    id="c15",
    rut="20993344-1",
    nombres="Luis",
    apellidos="Araya",
    fecha_nacimiento="21-09-1998",
    numero_telefono="922334455",
    correo="luis.araya@outlook.com"
);


def create_pedido_local(
                        numero_mesa :int,
                        Npedido:int
):
    sql={
        "INSERT INTO CLIENTE (numero_mesa,Npedido)"
        "VALUES(:numero_mesa,:Npedido)"
    }

    parametros = {
        "numero_mesa":numero_mesa,
        "Npedido":Npedido
    }
    
    def create_pedido_local(query):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    print(f"Tabla creada \n {parametros}")
                conn.commit()
        except oracledb.DatabaseError as e:
            err = e
            print(f"No se pudo crear la tabla: {err} \n {parametros}")   

create_pedido_local(
    numero_mesa=1,
    Npedido=101
);
create_pedido_local(
    numero_mesa=3,
    Npedido=102
);
create_pedido_local(
    numero_mesa=5,
    Npedido=103
);
create_pedido_local(
    numero_mesa=7,
    Npedido=104
);
create_pedido_local(
    numero_mesa=10,
    Npedido=105 
);


def create_pedido_llevar(
                        tiempo_estimado: int,
                        Npedido:int,                       
):
    sql={
        "INSERT INTO CLIENTE (tiempo_estimado,Npedido)"
        "VALUES(:numero_mesa,:Npedido)"
    }

    parametros = {
        "tiempo_estimado":tiempo_estimado,
        "Npedido":Npedido
    }
    
    def create_pedido_llevar(query):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    print(f"Tabla creada \n {parametros}")
                conn.commit()
        except oracledb.DatabaseError as e:
            err = e
            print(f"No se pudo crear la tabla: {err} \n {parametros}")    
    
create_pedido_llevar(
    tiempo_estimado=15,
    Npedido=201
);
create_pedido_llevar(
    tiempo_estimado=20,
    Npedido=202
);
create_pedido_llevar(
    tiempo_estimado=12,
    Npedido=203
);
create_pedido_llevar(
    tiempo_estimado=25,
    Npedido=204
);
create_pedido_llevar(
    tiempo_estimado=18,
    Npedido=205
);


def create_pedido_domicilio(
                            direccion :str,
                            Npedido: int,
                            RUTrepartidor : str, 
                            
):
    sql={
        "INSERT INTO CLIENTE (numero_mesa,Npedido)"
        "VALUES(:numero_mesa,:Npedido)"
    }

    parametros = {
        "direccion":direccion,
        "Npedido":Npedido,
        "RUTrepartidor": RUTrepartidor
    }
    
    def create_pedido_domicilio(query):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query)
                    print(f"Tabla creada \n {parametros}")
                conn.commit()
        except oracledb.DatabaseError as e:
            err = e
            print(f"No se pudo crear la tabla: {err} \n {parametros}")  

create_pedido_domicilio(
    direccion="Av. Las Torres 1456, Puente Alto",
    Npedido=301,
    RUTrepartidor="17.890.234-6"
);
create_pedido_domicilio(
    direccion="Calle Los Alerces 223, La Florida",
    Npedido=302,
    RUTrepartidor="20.345.667-3"
);
create_pedido_domicilio(
    direccion="Pasaje Azul 987, Maipú",
    Npedido=303,
    RUTrepartidor="17.890.234-6"
);
create_pedido_domicilio(
    direccion="Av. Pedro de Valdivia 450, Ñuñoa",
    Npedido=304,
    RUTrepartidor="22.123.556-8"
);
create_pedido_domicilio(
    direccion="Los Copihues 1120, Providencia",
    Npedido=305,
    RUTrepartidor="20.345.667-3"
);


#read-consultar datos
def read_pedido():
    sql = (
        "SELECT * FROM pedido"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla pedido")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")
#=====================================================#
def read_pedido_by_id(numero):
    sql = (
        "SELECT * FROM pedido WHERE numero = :numero"
    )

    parametros = {"numero": numero}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql, parametros)
                print(f"Consulta a la tabla cliente por ID")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")


def read_cliente():
    sql = (
        "SELECT * FROM cliente"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla cliente")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")
#=====================================================#
def read_cliente_by_id(id):
    sql = (
        "SELECT * FROM cliente WHERE id = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql, parametros)
                print(f"Consulta a la tabla cliente por ID")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")


def read_repartidor():
    sql = (
        "SELECT * FROM repartidor"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla reparidor")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")
#=====================================================#
def read_repartidor_by_id(id):
    sql = (
        "SELECT * FROM cliente WHERE id = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql, parametros)
                print(f"Consulta a la tabla repartidor por ID")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")


def read_pedido_domicilio():
    sql = (
        "SELECT * FROM pedido_domicilio"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla pedido_domicilio")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")
#=====================================================#
def read_pedido_domicilio_by_id(Npedido):
    sql = (
        "SELECT * FROM cliente WHERE Npedido = :Npedido"
    )

    parametros = {"Npedido": Npedido}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql, parametros)
                print(f"Consulta a la tabla repartidor por el numero del pedido")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")


def read_pedido_llevar():
    sql = (
        "SELECT * FROM pepedido_llevar"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla pedido llevar")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")
#=====================================================#
def read_pedido_llevar_by_id(Npedido):
    sql = (
        "SELECT * FROM cliente WHERE Npedido = :Npedido"
    )

    parametros = {"Npedido": Npedido}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql, parametros)
                print(f"Consulta a la tabla pedido_llevar por el numero del pedido")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")


def read_pedido_local():
    sql = (
        "SELECT * FROM pepedido_local"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla pedido local")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")
#=====================================================#
def read_pedido_local_by_id(Npedido):
    sql = (
        "SELECT * FROM cliente WHERE Npedido = :Npedido"
    )

    parametros = {"Npedido": Npedido}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql, parametros)
                print(f"Consulta a la tabla pedido_local por el numero del pedido")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")


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
    parametros= {"id":id}
 
    if rut is not None:
        modificaciones.append("rut =: rut")
        parametros["rut"] = rut
    if nombres is not None:
        modificaciones.append("nombres =: nombres")
        parametros["nombres"] = nombres
    if apellidos is not None:
        modificaciones.append("apellidos =: apellidos")
        parametros["apellidos"] = apellidos
    if numero_telefono is not None:
        modificaciones.append("numero_telefono =: numero_telefono")
        parametros["numero_telefono"] = numero_telefono
    if correo is not None:
        modificaciones.append("correo =: correo")
        parametros["correo"] = correo
    if fecha_nacimiento is not None:
        modificaciones.append("fecha_nacimiento =: fecha_nacimiento")
        parametros["fecha_nacimiento"] = datetime.strptime(
            fecha_nacimiento, "%Y-%m-%d")
    if not modificaciones:
        return print("No hay campos para actualizar.")
 
    sql = f"UPDATE personas SET {", ".join(modificaciones)} WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Persona con RUT={rut} actualizada.") 


def update_repartidor(
        id,
        nombre: Optional[str]=None,
        apellido: Optional[str]=None,
        vehiculo: Optional[str]=None
):
    modificaciones = []
    parametros = {"id": id}

    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        parametros["nombre"] = nombre

    if apellido is not None:
        modificaciones.append("apellido =: apellido")
        parametros["apellido"] = apellido

    if vehiculo is not None:
        modificaciones.append("vehiculo =: vehiculo")
        parametros["vehiculo"] = vehiculo

    if not modificaciones:
        return print("No hay campos para actualizar.")

    sql = f"UPDATE repartidor SET {', '.join(modificaciones)} WHERE id =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Repartidor con ID={id} actualizado.")


def update_pedido_domicilio(
        Npedido,
        direccion: Optional[str]=None,
        RUTrepartidor: Optional[str]=None
):
    modificaciones = []
    parametros = {"Npedido": Npedido}

    if direccion is not None:
        modificaciones.append("direccion =: direccion")
        parametros["direccion"] = direccion

    if RUTrepartidor is not None:
        modificaciones.append("RUTrepartidor =: RUTrepartidor")
        parametros["RUTrepartidor"] = RUTrepartidor

    if not modificaciones:
        return print("No hay campos para actualizar.")

    sql = f"UPDATE pedido_domicilio SET {', '.join(modificaciones)} WHERE Npedido =: Npedido"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Pedido domicilio actualizado {Npedido}.")


def update_pedido_llevar(
        Npedido,
        tiempo_estimado: Optional[int]=None
):
    modificaciones = []
    parametros = {"Npedido": Npedido}

    if tiempo_estimado is not None:
        modificaciones.append('"tiempo estimado" =: tiempo_estimado')
        parametros["tiempo_estimado"] = tiempo_estimado

    if not modificaciones:
        return print("No hay campos para actualizar.")

    sql = f'UPDATE pedido_llevar SET {", ".join(modificaciones)} WHERE Npedido =: Npedido'

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Pedido llevar actualizado {Npedido}.")


def update_pedido_local(
        Npedido,
        numero_mesa: Optional[int]=None
):
    modificaciones = []
    parametros = {"Npedido": Npedido}

    if numero_mesa is not None:
        modificaciones.append("numero_mesa =: numero_mesa")
        parametros["numero_mesa"] = numero_mesa

    if not modificaciones:
        return print("No hay campos para actualizar.")

    sql = f"UPDATE pedido_local SET {', '.join(modificaciones)} WHERE Npedido =: Npedido"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, parametros)
        conn.commit()
        print(f"Pedido local actualizado {Npedido}.")


#eliminar datos 

def eliminar_cliente(id:int): 
    sql=(
        "DELETE FROM cliente WHERE id=id"
    ) 

    parametros ={"id":id} 

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"dato eliminado {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al eliminar dato: {err} \n {sql} \n {parametros}")


def eliminar_pedido_local(Npedido:int):
    sql = (
        "DELETE FROM pedido_local WHERE Npedido=Npedido"
    )

    parametros = {"Npedido": Npedido}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"dato eliminado {parametros}")
    except oracledb.DatabaseError as e:
        print(f"Error al eliminar dato: {e} \n {sql} \n {parametros}")


def eliminar_pedido_llevar(Npedido:int):
    sql = (
        "DELETE FROM pedido_llevar WHERE Npedido=Npedido"
    )

    parametros = {"Npedido": Npedido}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"dato eliminado {parametros}")
    except oracledb.DatabaseError as e:
        print(f"Error al eliminar dato: {e} \n {sql} \n {parametros}")


def eliminar_pedido_domicilio(Npedido:int):
    sql = (
        "DELETE FROM pedido_domicilio WHERE Npedido=Npedido"
    )

    parametros = {"Npedido": Npedido}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"dato eliminado {parametros}")
    except oracledb.DatabaseError as e:
        print(f"Error al eliminar dato: {e} \n {sql} \n {parametros}")


def eliminar_repartidor(id:str):
    sql = (
        "DELETE FROM repartidor WHERE id=id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, parametros)
            conn.commit()
            print(f"dato eliminado {parametros}")
    except oracledb.DatabaseError as e:
        print(f"Error al eliminar dato: {e} \n {sql} \n {parametros}")


#menu
def main ():
    while True : 
        os.system("cls")
        print(
            """
            ╔═════════════════════════════════════════╗
            ║           crud con oraclesql            ║          
            ║              (っ◕‿◕)っ                 ║
            ╠═════════════════════════════════════════╣
            ║ ●1.aplicar esquema en la baser de datos ║  
            ║ ●2.tabla cliente                        ║    
            ║ ●3.tabla pedido                         ║ 
            ║ ●4.tabla repartidor                     ║  
            ║ ●0.salir                                ║  
            ╚═════════════════════════════════════════╝  
            """
        )
        opcion = input("selecciona una opcion[1-4, 0 para salir]:")
        if opcion == 0: 
            print("Saliendo del menú...  (￣▽￣)/")
            input("presiona ENTER para continuar...")
            break 
        elif opcion=="1":
            pass
        elif opcion=="2":
            menu_cliente()
        elif opcion=="3":
            menu_pedidos()
        else : 
            print("opcion invalida")
            input("presione ENTER para continuar...")
            break


#menus tablas

def menu_cliente ():
    while True : 
        os.system("cls")
        print(
            """
            ╔═════════════════════════════════════════╗
            ║           menu tabla cliente            ║          
            ║                (˶ˆᗜˆ˵)                  ║
            ╠═════════════════════════════════════════╣
            ║ ●1.insertar cliente                     ║  
            ║ ●2.leer cliente                         ║  
            ║ ●3.leer cliente por id                  ║  
            ║ ●4.modificar cliente                    ║
            ║ ●5.eliminar cliente                     ║                        
            ║ ●0.salir                                ║  
            ╚═════════════════════════════════════════╝  
            """
        ) 

        opcion = input("selecciona una opcion[1-5, 0 para salir]:")
        if opcion == 0: 
            print("Saliendo del menú de clientes... (￣▽￣)/")
            input("presiona ENTER para continuar...")
            break 
        elif opcion=="1": 
            try :
                id =int(input("ingrese el id de la persona"))
                rut=input("ingrese el rut de la persona")
                nombres=input("ingrese los nombres de la persona")
                apellidos=input("ingrese los apellidos de la persona")
                fecha_nacimiento =input("Ingresa la fecha de nacimiento (año-mes-dia). Ej: 2002-12-30: ")
                correo=input("ingrese el correo de la persona")
                numero_telefono=input("ingrese el numero de telefono de la persona")
                create_cliente(id,rut,nombres,apellidos,fecha_nacimiento,correo,numero_telefono)
            except ValueError :
                print("ingreso un valor no numerico")
            input("presione ENTER para continuar...")

        elif opcion=="2":
            read_cliente()
            input("Presiona ENTER para continuar...")
        elif opcion=="3":
            try:
                id = int(input("Ingrese el id numerico de la persona: "))
                read_cliente_by_id(id)
            except ValueError:
                print("Ingresaste un valor no númerico")
            
            input("Presiona ENTER para continuar...")
        elif opcion=="4":
            try:
                id = int(input("Ingrese el id numerico de la persona: "))
                print("Sólo digite cuándo quiera modificar el dato")
                rut = input("Ingresa el rut. Ej: 12345678-4: ")
                nombres = input("Ingrese nombres de la persona: ")
                apellidos = input("Ingrese apellidos de la persona: ")
                fecha_nacimiento = input("Ingresa la fecha de nacimiento (año-mes-dia). Ej: 2002-12-30: ")
                correo=input("ingrese el correo de la persona")
                numero_telefono=input("ingrese el numero de telefono de la persona. Ej: +56 9 8764 7877")
                if len(rut.strip()) == 0:
                    rut = None
                if len(nombres.strip()) == 0:
                    nombres = None
                if len(apellidos.strip()) == 0:
                    apellidos = None
                if len(fecha_nacimiento.strip()) == 0:
                    fecha_nacimiento = None
                if len(correo.strip()) == 0:
                    correo = None
                if len(numero_telefono.strip()) == 0:
                    numero_telefono = None
                    update_cliente(id,rut,nombres,apellidos,fecha_nacimiento,correo,numero_telefono)
            except ValueError:
                print("Ingresaste un valor no númerico")

            input("Presiona ENTER para continuar...")
        elif opcion=="5":
            try:
                id = int(input("Ingrese el id numerico de la persona: "))
                eliminar_cliente(id)
            except ValueError:
                print("Ingresaste un valor no númerico")

        else : 
            print("opcion invalida")
            input("presione ENTER para continuar...")
            break


def menu_pedido_local():
    while True:
        os.system("cls")
        print(
            """
            ╔═════════════════════════════════════════╗
            ║         menu tabla pedido local         ║          
            ║                  ᕙ(⇀‸↼‵)ᕗ              ║
            ╠═════════════════════════════════════════╣
            ║ ●1.insertar pedido local                ║  
            ║ ●2.leer pedidos local                   ║  
            ║ ●3.leer pedido local por id             ║  
            ║ ●4.modificar pedido local               ║
            ║ ●5.eliminar pedido local                ║
            ║ ●6.leer el total a pagar por id         ║                        
            ║ ●0.salir                                ║  
            ╚═════════════════════════════════════════╝  
            """
        )

        opcion = input("selecciona una opcion[1-6, 0 para salir]:")

        if opcion == "0":
            print("Saliendo del menú de pedidos local...  (￣▽￣)/")
            input("presiona ENTER para continuar...")
            break

        elif opcion == "1":
            try:
                Npedido = int(input("ingrese el número de pedido: "))
                numero_mesa = int(input("ingrese el número de mesa: "))
                create_pedido_local(Npedido, numero_mesa)
            except ValueError:
                print("ingresaste un valor no numerico")
            input("presiona ENTER para continuar...")

        elif opcion == "2":
            read_pedido_local()
            input("Presiona ENTER para continuar...")

        elif opcion == "3":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                read_pedido_local_by_id(Npedido)
            except ValueError:
                print("Ingresaste un valor no númerico")
            input("Presiona ENTER para continuar...")

        elif opcion == "4":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                numero_mesa = input("Nuevo número de mesa (opcional): ")
                if len(numero_mesa.strip()) == 0:
                    numero_mesa = None
                update_pedido_local(Npedido, numero_mesa)
            except ValueError:
                print("Ingresaste un valor no numerico")
            input("Presiona ENTER para continuar...")

        elif opcion == "5":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                eliminar_pedido_local(Npedido)
            except ValueError:
                print("Ingresaste un valor no numerico")
            input("Presiona ENTER para continuar...")
        elif opcion == "6": 
            try:
                numero = int(input("Ingrese el número del pedido: "))
                read_pedido_by_id(numero)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")

        else:
            print("opcion invalida")
            input("presione ENTER para continuar...")
            break


def menu_pedido_llevar():
    while True:
        os.system("cls")
        print(
            """
            ╔═════════════════════════════════════════╗
            ║        menu tabla pedido para llevar    ║          
            ║              ᕙ(⇀‸↼‵)ᕗ                  ║
            ╠═════════════════════════════════════════╣
            ║ ●1.insertar pedido llevar               ║  
            ║ ●2.leer pedidos llevar                  ║  
            ║ ●3.leer pedido llevar por id            ║  
            ║ ●4.modificar pedido llevar              ║
            ║ ●5.eliminar pedido llevar               ║
            ║ ●6.leer el total a pagar por id         ║                                     
            ║ ●0.salir                                ║  
            ╚═════════════════════════════════════════╝  
            """
        )

        opcion = input("selecciona una opcion[1-6, 0 para salir]:")

        if opcion == "0":
            print("Saliendo del menú de pedidos para llevar...  (￣▽￣)/")
            input("presiona ENTER para continuar...")
            break

        elif opcion == "1":
            try:
                Npedido = int(input("ingrese número de pedido: "))
                tiempo = int(input("ingrese tiempo estimado: "))
                create_pedido_llevar(tiempo, Npedido)
            except ValueError:
                print("Valor no numerico")
            input("presiona ENTER para continuar...")

        elif opcion == "2":
            read_pedido_llevar()
            input("Presiona ENTER para continuar...")

        elif opcion == "3":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                read_pedido_llevar_by_id(Npedido)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")

        elif opcion == "4":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                tiempo = input("Nuevo tiempo estimado (opcional): ")
                if len(tiempo.strip()) == 0:
                    tiempo = None
                update_pedido_llevar(Npedido, tiempo)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")

        elif opcion == "5":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                eliminar_pedido_llevar(Npedido)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")
        
        elif opcion == "6": 
            try:
                numero = int(input("Ingrese el número del pedido: "))
                read_pedido_by_id(numero)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")

        else:
            print("opción invalida")
            input("presione ENTER para continuar...")
            break


def menu_pedido_domicilio():
    while True:
        os.system("cls")
        print(
            """
            ╔═════════════════════════════════════════╗
            ║      menu tabla pedido  a domicilio     ║          
            ║               ᕙ(⇀‸↼‵)ᕗ                 ║
            ╠═════════════════════════════════════════╣
            ║ ●1.insertar pedido domicilio            ║  
            ║ ●2.leer pedidos domicilio               ║  
            ║ ●3.leer pedido domicilio por id         ║  
            ║ ●4.modificar pedido domicilio           ║
            ║ ●5.eliminar pedido domicilio            ║
            ║ ●6.leer el total a pagar por id         ║            
            ║ ●0.salir                                ║  
            ╚═════════════════════════════════════════╝  
            """
        )

        opcion = input("selecciona una opcion[1-6, 0 para salir]:")

        if opcion == "0":
            print("Saliendo del menú de pedido a domicilio...  (￣▽￣)/")
            input("presiona ENTER para continuar...")
            break

        elif opcion == "1":
            try:
                Npedido = int(input("ingrese número de pedido: "))
                direccion = input("ingrese dirección: ")
                rut = input("ingrese RUT repartidor: ")
                create_pedido_domicilio(direccion, Npedido, rut)
            except ValueError:
                print("Valor no numerico")
            input("presiona ENTER para continuar...")

        elif opcion == "2":
            read_pedido_domicilio()
            input("Presiona ENTER para continuar...")

        elif opcion == "3":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                read_pedido_domicilio_by_id(Npedido)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")

        elif opcion == "4":
            try:
                Npedido = int(input("Ingrese número del pedido: "))
                direccion = input("Nueva dirección (opcional): ")
                rut = input("Nuevo RUT repartidor (opcional): ")
                if len(direccion.strip()) == 0:
                    direccion = None
                if len(rut.strip()) == 0:
                    rut = None
                update_pedido_domicilio(Npedido, direccion, rut)
            except ValueError:
                print("Valor no numérico")
            input("Presiona ENTER para continuar...")

        elif opcion == "5":
            try:
                Npedido = int(input("Ingrese el número del pedido: "))
                eliminar_pedido_domicilio(Npedido)
            except ValueError:
                print("Valor no numérico")
            input("Presiona ENTER para continuar...") 
        
        elif opcion == "6": 
            try:
                numero = int(input("Ingrese el número del pedido: "))
                read_pedido_by_id(numero)
            except ValueError:
                print("Valor no numerico")
            input("Presiona ENTER para continuar...")

        else:
            print("opción invalida")
            input("presione ENTER para continuar...")
            break


def menu_repartidor():
    while True:
        os.system("cls")
        print(
            """
            ╔═════════════════════════════════════════╗
            ║           MENU TABLA REPARTIDOR         ║          
            ║               (ദ്ദി˙ᗜ˙)                   ║
            ╠═════════════════════════════════════════╣
            ║ ●1. insertar repartidor                 ║  
            ║ ●2. leer repartidores                   ║  
            ║ ●3. leer repartidor por id              ║  
            ║ ●4. modificar repartidor                ║
            ║ ●5. eliminar repartidor                 ║                        
            ║ ●0. salir                               ║  
            ╚═════════════════════════════════════════╝  
            """
        )

        opcion = input("Selecciona una opción [1-5, 0 para salir]: ")

        if opcion == "0":
            print("Saliendo del menú de repartidor...  (￣▽￣)/")
            input("Presiona ENTER para continuar...")
            break

        elif opcion == "1":
            try:
                id = input("Ingresa el ID del repartidor (string): ")
                rut = input("Ingresa el RUT: ")
                nombre = input("Ingresa el nombre: ")
                telefono = input("Ingresa el teléfono: ")
                create_repartidor(id, rut, nombre, telefono)
            except:
                print("Error al insertar.")
            input("Presiona ENTER para continuar...")

        elif opcion == "2":
            read_repartidor()
            input("Presiona ENTER para continuar...")

        elif opcion == "3":
            id_repartidor = input("Ingresa el ID del repartidor (string): ")
            read_repartidor_by_id(id)
            input("Presiona ENTER para continuar...")

        elif opcion == "4":
            id = input("Ingresa el ID del repartidor (string): ")
            print("Deja vacío lo que NO quieras modificar.")
            rut = input("Nuevo RUT: ")
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")

            if rut.strip() == "": rut = None
            if nombre.strip() == "": nombre = None
            if telefono.strip() == "": telefono = None

            update_repartidor(id, rut, nombre, telefono)
            input("Presiona ENTER para continuar...")

        elif opcion == "5":
            id = input("Ingresa el ID del repartidor (string): ")
            eliminar_repartidor(id)
            input("Presiona ENTER para continuar...")

        else:
            print("Opción inválida")
            input("Presiona ENTER para continuar...")
            break


def menu_pedidos():
    while True:
        os.system("cls")
        print(
            """
            ╔══════════════════════════════════════════╗
            ║               MENU PEDIDOS               ║          
            ║                (っ＾▿＾)                 ║
            ╠══════════════════════════════════════════╣
            ║ ●1. Pedido Local                         ║  
            ║ ●2. Pedido Para Llevar                   ║  
            ║ ●3. Pedido a Domicilio                   ║  
            ║ ●0. Salir                                ║  
            ╚══════════════════════════════════════════╝  
            """
        )

        opcion = input("Selecciona una opción [1-3, 0 para salir]: ")

        if opcion == "0":
            print("Saliendo del menú de pedidos...  (￣▽￣)/")
            input("Presiona ENTER para continuar...")
            break

        elif opcion == "1":
            menu_pedido_local()
            input("Presiona ENTER para continuar...")

        elif opcion == "2":
            menu_pedido_llevar()
            input("Presiona ENTER para continuar...")

        elif opcion == "3":
            menu_pedido_domicilio()
            input("Presiona ENTER para continuar...")

        else:
            print("Opción inválida")
            input("Presiona ENTER para continuar...")

if __name__ == "__main__":
    main() 

