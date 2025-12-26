CREATE TABLE prueba_usuario (
  id NUMBER PRIMARY KEY,
  nombre VARCHAR2(50)
);
INSERT INTO prueba_usuario VALUES (1, 'Registro de prueba');
SELECT * FROM prueba_usuario; 


INSERT INTO system.proyectos_ignacio VALUES (1, 'Sistema Ventas', 'Joaquín Villarroel');
SELECT * FROM system.proyectos_ignacio;


UPDATE system.proyectos_ignacio SET nombre='Prueba' WHERE id_proyecto=1;