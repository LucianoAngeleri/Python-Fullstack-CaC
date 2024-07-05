#Instalar pymysql (pip install PyMySQL)

#Importar pymysql / SQLalchemy / dbmysql
import pymysql

#Conectar con el servidor MySQL
def conectarMySQL():
    #Datos sensibles, debemos utilizar variables de entorno
    host="localhost"
    user="root"
    password="admin1234"
    db="tienda_py"
    return pymysql.connect(host=host,user=user,password=password,database=db)

#GET OBTENER productos
def obtenerProductos():
    #Conexión a MySQL
    conexion = conectarMySQL()
    # Creamos una variable para almacenar los productos
    productos = []
    #Consulta
    with conexion.cursor() as cursor:
        sql = "SELECT * FROM `productos`"
        cursor.execute(sql)
        productos = cursor.fetchall();
    #Devolvemos el resultado de la consulta
    return productos

#CRUD Create / Read / Update / Delete