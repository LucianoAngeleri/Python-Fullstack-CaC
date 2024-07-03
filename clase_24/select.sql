/* USE sirve para seleccionar la base de datos que queremos usar. */
USE `curso-24165`;
/* SELECT sirve para seleccionar registros de una tabla. */
/* El selector universarl (*) selecciona todas las columnas de una tabla*/
/* FROM indica la tabla a la que queremos hacer la consulta*/
SELECT * FROM usuarios;
/*SELECT nombre_col1, nombre_col2, ... FROM nombre_tabla; Si queremos que la consulta nos devuelva solo ciertas columnas.*/
SELECT nombre, email FROM usuarios;

/* WHERE sirve para condicionar la consulta con ciertos criterios*/
SELECT * FROM usuarios WHERE id=1;

/* LIMIT sirve para limitar la consulta a cierto numero de registros a mostrar*/
SELECT * FROM usuarios LIMIT 2;

/* El uso del WHERE y LIKE sirve para que la consulta devuelva un resultado de acuerdo al criterio establecido*/
/* En este caso WHERE nombre LIKE "luciano" busca en la columna nombre los registros que coninciden con "luciano"*/
SELECT * FROM usuarios WHERE nombre LIKE "luciano";
/* Podemos usar el WHERE con operadores como OR y AND para combinar los criterios de consulta*/
/* En este caso devolvera los registros cuyos nombres sean "luciano" o "bruno"*/
SELECT * FROM usuarios WHERE nombre="luciano" OR nombre="bruno";
