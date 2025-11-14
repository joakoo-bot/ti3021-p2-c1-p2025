    CREATE TABLE 
        cliente (
            rut  INTEGER  PRIMARY KEY,
            nombre VARCHAR,
            apellido VARCHAR, 
            correo VARCHAR, 
            telefono VARCHAR
            
        ) ;
    
    CREATE TABLE 
        pedido(
            numero INTEGER PRIMARY KEY, 
            fecha date ,
            RUTcliente  INTEGER, 
            total_a_pagar int,   
            FOREIGN KEY (RUTcliente) REFERENCES cliente(rut)
        );

    
    CREATE TABLE 
        pedido_local (
            numero_mesa int,
            Npedido INTEGER
            FOREIGN KEY (Npedido) REFERENCES pedido(numero)

        );
    
    CREATE TABLE 
        pedido_para_llevar (
            tiempo_estimado int,
            Npedido INTEGER
            FOREIGN KEY (Npedido) REFERENCES pedido(numero)

        );   
    
    CREATE TABLE 
        pedido_a_domicilio (
            direccion int,
            Npedido INTEGER
            FOREIGN KEY (Npedido) REFERENCES pedido(numero) ,
            RUTrepartidor  INTEGER, 
            FOREIGN KEY (RUTrepartidor) REFERENCES repartidor(rut)
        );
    
    CREATE TABLE 
        repartidor (
            rut  INTEGER  PRIMARY KEY,
            nombre VARCHAR,
            apellido VARCHAR, 
            correo VARCHAR, 
            telefono VARCHAR
            
        ); 