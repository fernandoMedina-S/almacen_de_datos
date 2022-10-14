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