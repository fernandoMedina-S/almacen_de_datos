import petl as etl

#1.- Toma las primeras n filas
etl.head
#2.- Tomas las ultimas n filas
etl.tail
#3.- Tomar un subgrupo de filas
etl.rowslice
#4.- Remover filas
etl.cutout
#5.- Concatenar tablas
etl.concat
#6.- Saltar filas si alguno de los contenidos coincide con el criterio
etl.skipcomments
#7.- Añade un nuevo campo (columna) a la tabla con un valor ya determinado
etl.addfield
#8.- Añade el numero de fila en cada registro
etl.addrownumbers
#9.- renombra nombre de la columna
etl.rename
#10.- Salta filas incluyendo el header
etl.skip