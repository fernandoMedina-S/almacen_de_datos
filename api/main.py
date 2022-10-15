from fastapi import FastAPI
import mysql.connector
import json
app = FastAPI()

# Connect to the database
connection = mysql.connector.connect(
    user='root', password='', host='localhost', database='nuevas_escuelas')
# Retrive the cursor
cursor = connection.cursor()


def getResults(cursor):
    print(type(cursor))
    encabezado = [i[0] for i in cursor.description]
    resultado = []
    for fila in cursor.fetchall():
        resultado.append(dict(zip(encabezado, fila)))
    return json.dumps(resultado)


@app.get('/')
def root():
    return "HOME"


@app.get("/colonia_negocios/{colonia}")
def colonia_negocios(colonia: str):
    consulta = """SELECT dim_colonia.nombre, dim_negocio.nombre, dim_negocio.giro FROM colonia_negocio 
    INNER JOIN dim_colonia on colonia_negocio.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_negocio on colonia_negocio.id_negocio = dim_negocio.id_negocio where dim_colonia.nombre = '{}'""".format(
        colonia)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.get("/ciudad_negocios/{ciudad}")
def ciudad_negocios(ciudad: str):
    consulta = """SELECT dim_colonia.nombre, dim_negocio.nombre, dim_negocio.giro FROM colonia_negocio 
    INNER JOIN dim_colonia on colonia_negocio.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_negocio on colonia_negocio.id_negocio = dim_negocio.id_negocio where dim_colonia.ciudad = '{}'""".format(
        ciudad)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.get("/colonia_escuelas/{colonia}")
def colonia_escuelas(colonia: str):
    consulta = """SELECT dim_colonia.nombre, dim_escuela.nombre, dim_escuela.nivel, dim_escuela.control FROM colonia_escuela 
    INNER JOIN dim_colonia on colonia_escuela.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_escuela on colonia_escuela.id_escuela = dim_escuela.id_escuela where dim_colonia.nombre = '{}'""".format(
        colonia)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.get("/ciudad_escuelas/{ciudad}")
def ciudad_escuelas(ciudad: str):
    consulta = """SELECT dim_colonia.nombre, dim_escuela.nombre, dim_escuela.nivel, dim_escuela.control FROM colonia_escuela
    INNER JOIN dim_colonia on colonia_escuela.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_escuela on colonia_escuela.id_escuela = dim_escuela.id_escuela where dim_colonia.ciudad = '{}'""".format(
        ciudad)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado