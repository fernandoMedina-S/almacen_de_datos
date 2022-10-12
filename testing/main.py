import petl as etl

# Toma el archivo y lo transforma en un formato imprimible
csvDatabase = etl.fromcsv('./resources/data.csv')

# imprime el contenido del archivo csv
print(csvDatabase)

# creacion de un nuevo set de datos conteniendo las columnas nombre y edad
tabla2 = [['nombre','edad'],['jorge', 20],['maria', 30],['jose', 40],['jose', 50]]

# exportamos el contenido del nuevo set de datos a un archivo csv
etl.tocsv(tabla2, './resources/newData.csv')

# abrimos el archivo recien creado y guardamos su contenido en una nueva variable
newDatabase = etl.fromcsv('./resources/newData.csv')

# imprimimos el contenido de nuestra segunda tabla
print(newDatabase)
