from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import json
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to the database
connection = mysql.connector.connect(
    user='root', password='', host='localhost', database='nuevas_escuelas')
# Retrive the cursor
cursor = connection.cursor()

cursor.execute('set global max_allowed_packet=67108864')
cursor.execute('SET GLOBAL connect_timeout = 10')


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

# -------------------------------------------------------
# Escuelas por colonia
@app.get("/escuelas-por-colonia/")
def escuelas_por_colonia():
    consulta = """SELECT COUNT(id_colonia), id_escuela 
                    FROM colonia_escuela
                    GROUP BY id_escuela 
                    LIMIT 10;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado.insert(0, ("Escuelas", "Colonia"))
    return resultado

# Negocios por colonia
@app.get("/negocios-por-colinia/")
def negocios_por_colonia():
    consulta = """SELECT COUNT(id_colonia), id_negocio 
                    FROM colonia_negocio
                    LIMIT 10;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

# Escuelas con mayor numero de estudiantes del estado del jalisco
@app.get("/escuelas-num-estudiantes/")
def escuelas_num_estudiantes():
    consulta = """SELECT nombre, ciudad, numero_alumnos 
                    FROM dim_escuela
                    ORDER BY numero_alumnos desc
                    LIMIT 10;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

# Numero de alumnos en las escuelas segun su nivel academico en guadalajara
@app.get("/nivel-escuelas/")
def nivel_escuelas():
    consulta = """SELECT nivel, sum(numero_alumnos) AS num_alumnos 
                    FROM dim_escuela
                    WHERE ciudad='GUADALAJARA' AND numero_alumnos != 0
                    GROUP BY nivel;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado.insert(0, ("Tipo de escuela", "Alumnos"))
    return resultado

# Porcentaje de escuelas de nivel publico contra nivel privado en el estado de jalisco
# Para esto se necesitan hacer los resultados de las dos consultas para poder sacar el porcentaje
# TOTAL = 15901 (100%)

# 12266 (77.2%)
@app.get("/numero-escuelas-publicas/")
def numero_escuelas_publicas():
    consulta = """SELECT count(*) 
                    FROM dim_escuela
                    WHERE control='PUBLICO';"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

#3635 (22.8%)
@app.get("/numero-escuelas-privadas/")
def numero_escuelas_privadas():
    consulta = """SELECT count(*) 
                    FROM dim_escuela
                    WHERE control='PRIVADO';"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado
# -------------------------------------------------------

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