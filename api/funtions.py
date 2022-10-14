import petl as etl

testTable1 = etl.fromcsv("./resources/test_table1.csv", encoding="UTF-8")
"""
+--------+-----+--------+
| T1A   | T1B | T1C    |
+========+=====+========+
| Carlos | 23  | male   |
+--------+-----+--------+
| Susana | 33  | female |
+--------+-----+--------+
| Pepe   | 12  | male   |
+--------+-----+--------+
"""
testTable2 = etl.fromcsv("./resources/test_table2.csv", encoding="UTF-8")
"""
+-------------+----------+------+
| T2A        | T2B      | T2C  |
+=============+==========+======+
| Toyota      | Yaris    | 1998 |
+-------------+----------+------+
| Chevrolette | Corvette | 2002 |
+-------------+----------+------+
| Ford        | Focus    | 2005 |
+-------------+----------+------+
"""

#1.- Toma las primeras n filas
table_a = etl.head(testTable1,1)
#print(table_a)
"""
+--------+-----+------+
| T1A   | T1B | T1C  |
+========+=====+======+
| Carlos | 23  | male |
+--------+-----+------+
"""
#2.- Tomas las ultimas n filas
table_b = etl.tail(testTable1,1)
#print(table_b)
"""
+------+-----+------+
| T1A | T1B | T1C  |
+======+=====+======+
| Pepe | 12  | male |
+------+-----+------+
"""
#3.- Tomar un subgrupo de filas
table_c = etl.rowslice(testTable2,1,3)
#print(table_c)
"""
+-------------+----------+------+
| T2A        | T2B      | T2C  |
+=============+==========+======+
| Chevrolette | Corvette | 2002 |
+-------------+----------+------+
| Ford        | Focus    | 2005 |
+-------------+----------+------+
"""
#4.- Remover columnas
table_d = etl.cutout(testTable2,"T2B")
#print(table_d)
"""
+-------------+------+
| T2A        | T2C  |
+=============+======+
| Toyota      | 1998 |
+-------------+------+
| Chevrolette | 2002 |
+-------------+------+
| Ford        | 2005 |
+-------------+------+
"""
#5.- Concatenar tablas
table_e = etl.cat(testTable1,testTable2)
#print(table_e)
"""
+--------+------+--------+-------------+----------+------+
| T1A   | T1B  | T1C    | T2A        | T2B      | T2C  |
+========+======+========+=============+==========+======+
| Carlos | 23   | male   | None        | None     | None |
+--------+------+--------+-------------+----------+------+
| Susana | 33   | female | None        | None     | None |
+--------+------+--------+-------------+----------+------+
| Pepe   | 12   | male   | None        | None     | None |
+--------+------+--------+-------------+----------+------+
| None   | None | None   | Toyota      | Yaris    | 1998 |
+--------+------+--------+-------------+----------+------+
| None   | None | None   | Chevrolette | Corvette | 2002 |
+--------+------+--------+-------------+----------+------+
"""
#6.- Saltar filas si algun valor en la primera columna coincide con el criterio
table_f = etl.skipcomments(testTable1,"Sus")
#print(table_f)
"""
+--------+-----+------+
| T1A   | T1B | T1C  |
+========+=====+======+
| Carlos | 23  | male |
+--------+-----+------+
| Pepe   | 12  | male |
+--------+-----+------+
"""
#7.- Añade un nuevo campo (columna) a la tabla con un valor ya determinado
table_g = etl.addfield(testTable2, "CC","2500CC")
#print(table_g)
"""
+-------------+----------+------+--------+
| T2A        | T2B      | T2C  | CC     |
+=============+==========+======+========+
| Toyota      | Yaris    | 1998 | 2500CC |
+-------------+----------+------+--------+
| Chevrolette | Corvette | 2002 | 2500CC |
+-------------+----------+------+--------+
| Ford        | Focus    | 2005 | 2500CC |
+-------------+----------+------+--------+
"""
#8.- Añade el numero de fila en cada registro
table_h = etl.addrownumbers(testTable2)
#print(table_h)
"""
+-----+-------------+----------+------+
| row | T2A        | T2B      | T2C  |
+=====+=============+==========+======+
|   1 | Toyota      | Yaris    | 1998 |
+-----+-------------+----------+------+
|   2 | Chevrolette | Corvette | 2002 |
+-----+-------------+----------+------+
|   3 | Ford        | Focus    | 2005 |
+-----+-------------+----------+------+
"""
#9.- renombra nombre de la columna
table_i = etl.rename(testTable2,"T2B","Model")
#print(table_i)
"""
+-------------+----------+------+
| T2A        | Model    | T2C  |
+=============+==========+======+
| Toyota      | Yaris    | 1998 |
+-------------+----------+------+
| Chevrolette | Corvette | 2002 |
+-------------+----------+------+
| Ford        | Focus    | 2005 |
+-------------+----------+------+
"""
#10.- Salta filas incluyendo el header
table_j = etl.skip(testTable1,1)
#print(table_j)
"""
+--------+----+--------+
| Carlos | 23 | male   |
+========+====+========+
| Susana | 33 | female |
+--------+----+--------+
| Pepe   | 12 | male   |
+--------+----+--------+
"""