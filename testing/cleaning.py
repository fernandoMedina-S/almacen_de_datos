import petl as etl
import mysql.connector
import sqlite3
import psycopg2
import pymysql

tabla1 = etl.fromcsv('data.csv')
"""
print(tabla1.head(2)) # Muestra las dos primeras filas
print(tabla1.tail(2)) # Muestra las dos ultimos filas

tabla2 = [['nombre','edad'],['jorge', 20],['maria', 30],['jose', 40],['jose', 50]]
etl.tocsv(tabla2, 'misdatos.csv')

"""
tabla2 = etl.rename(tabla1,'salary','salary_pesos')
#print(tabla2.head(2))

tabla3 = etl.skip(tabla2, 1)
#print(tabla3.head(0))

tabla2 = etl.convert(tabla2, 'salary_pesos', float)
tabla3 = etl.addfield(tabla2, 'salary_dolars', lambda x:  round(x['salary_pesos'] * 21.5,2))
tabla3 = etl.convert(tabla3, 'firstname','upper')
tabla3 = etl.convert(tabla3, 'lastname','lower')
#print(tabla3.head(4))

tabla4 = etl.search(tabla3, '.ille.')
#print(tabla4.head(4))

tabla5 = etl.search(tabla3,'firstname','.ille.')
#print(tabla5.head(4))

tabla11 = [['id','color'],['1','red'],['2','blue'],['3','green'],['4','yellow'],['5','orange']]
tabla12 = [['id','languague'],['1','english'],['2','spanish'],['3','french'],['4','german']]

tabla13 = etl.join(tabla11, tabla12, key='id')
#print(tabla13.head(5))

tabla14 = etl.leftjoin(tabla11, tabla12, key='id')
#print(tabla14.head(5))

tabla15 = etl.antijoin(tabla11, tabla12, key='id')
#print(tabla15.head(5))

etl.tohtml(tabla3,'resultados.html',caption='Datos procesados')
etl.tojson(tabla3,'resultados.json')


try:
    conexion = mysql.connector.connect(port=3306, host='localhost', user='root', password='12345', database='sakila')
    tabla8 = etl.fromdb(conexion,'select * from actor')
    print(tabla8.head(4))
except Exception as e:
    print(e)

""" 
try:
    conexion = psycopg2.connect('dbname=almacen user=postgres password=12345 port=5432')
    etl.todb(tabla3,conexion,'tabla_nueva', create=False)
except Exception as e:
    print(e)
conexion = sqlite3.connect('database.db')
etl.todb(tabla3, conexion, 'tabla_nueva', create=True)
"""
