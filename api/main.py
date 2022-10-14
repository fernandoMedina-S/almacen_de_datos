import petl as etl
import pymysql


connection = pymysql.connect(host="localhost", user="root", password='', database='nuevas_escuelas')
connection.cursor().execute('SET SQL_MODE=ANSI_QUOTES')

#Con esto subes los datos de escuelas
"""csvEscuelas = etl.fromcsv("./concentrado_escuelas_jalisco.csv", encoding="UTF-8")
tabla2 = etl.cut(csvEscuelas, "Nombre del centro de trabajo", "Domicilio", "Nombre del municipio o delegación", "Alumnos total", "Nombre del control (Público o Privado)", "Nombre de la colonia", "Tipo educativo")
tabla2 =  etl.rename(tabla2, {"Nombre del centro de trabajo": "nombre", "Domicilio": "calle", "Nombre del municipio o delegación": "ciudad", "Alumnos total": "numero_alumnos", "Nombre del control (Público o Privado)": "control", "Nombre de la colonia": "colonia", "Tipo educativo": "nivel"})
etl.todb(tabla2, connection, 'dim_escuela')
print(tabla2)
"""

#Con esto subes lo de las rutas de transporte
"""
routesFile = etl.fromcsv("./resources/routes.csv", encoding="utf-8")
tabla2 = etl.cut(routesFile, "route_id", "route_long_name")
tabla2 = etl.rename(tabla2, {"route_id": "ruta", "route_long_name": "destino"})
etl.todb(tabla2, connection, 'dim_transporte')
print(tabla2)
"""