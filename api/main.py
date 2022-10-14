from fastapi import FastAPI
import mysql.connector
import json
app = FastAPI()

# Connect to the database
connection = mysql.connector.connect(user='root', password='admin', host='localhost', database='sakila')
# Retrive the cursor
cursor = connection.cursor()


def getResults(cursor):
    print(type(cursor))
    encabezado = [i[0] for i in cursor.description]
    resultado  = []
    for fila in cursor.fetchall():
        resultado.append(dict(zip(encabezado, fila)))
    return json.dumps(resultado)


@app.get('/')
def root():
    return "HOME"

import petl as etl
import pymysql

#para la conexxión de petl
"""
connection = pymysql.connect(host="localhost", user="root", password='', database='nuevas_escuelas')
connection.cursor().execute('SET SQL_MODE=ANSI_QUOTES')
"""

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