import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_coches"
    )
    cursor = conexion.cursor(buffered=True)
    print("...¡Conexion Exitosa!...")
except:
    print("...¡Por el momento NO es posible conectarse con la Base de Datos!, ...¡Vuelve a intentar!...")