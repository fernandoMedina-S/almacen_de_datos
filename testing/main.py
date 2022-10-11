import petl as etl
csvDatabase = etl.fromcsv('./resources/data.csv')

# imprimir filas de la tabla
print(csvDatabase.head(2))

tabla2 = [['nombre','edad'],['jorge', 20],['maria', 30],['jose', 40],['jose', 50]]
etl.tocsv(tabla2, 'misdatos.csv')

print(tabla2.head(1))