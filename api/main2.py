from flask import Flask, request, make_response, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "nuevas_escuelas"

mysql = MySQL(app)

CORS(app)



@app.get('/')
def root():
    return "HOME"

@app.route("/escuelas-por-colonia/", methods = ["GET"])
def escuelas_por_colonia():
    cursor = mysql.connection.cursor()
    consulta = """SELECT dim_colonia.nombre, COUNT(id_escuela) as cont
                    FROM colonia_escuela
                    join dim_colonia
                    on colonia_escuela.id_colonia = dim_colonia.id_colonia
                    GROUP BY colonia_escuela.id_colonia
					limit 10;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado2 = list(resultado)
    resultado2.insert(0, ("Escuelas", "Colonia"))
    return jsonify(resultado2)

@app.route("/negocios-por-colonia/", methods = ["GET"])
def negocios_por_colonia():
    cursor = mysql.connection.cursor()
    consulta = """SELECT dim_colonia.nombre, COUNT(id_negocio) as cont
                    FROM colonia_negocio
                    join dim_colonia
                    on colonia_negocio.id_colonia = dim_colonia.id_colonia
                    GROUP BY colonia_negocio.id_colonia
					limit 10;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado2 = list(resultado)
    resultado2.insert(0, ("Negocios", "Colonia"))
    return jsonify(resultado2)

@app.route("/escuelas-num-estudiantes/", methods = ["GET"])
def escuelas_num_estudiantes():
    cursor = mysql.connection.cursor()
    consulta = """SELECT nombre, ciudad, numero_alumnos 
                    FROM dim_escuela
                    ORDER BY numero_alumnos desc
                    LIMIT 10;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado2 = list(resultado)
    resultado2.insert(0, ("Escuela - Ciudad", "Estudiantes"))
    for i in range(len(resultado2)):
        if i != 0:
            resultado2[i] = [resultado2[i][0] + " - " + resultado2[i][1], resultado2[i][2]]

    return jsonify(resultado2)

# Numero de alumnos en las escuelas segun su nivel academico en guadalajara
@app.route("/nivel-escuelas/", methods = ["GET"])
def nivel_escuelas():
    cursor = mysql.connection.cursor()
    consulta = """SELECT nivel, sum(numero_alumnos) AS num_alumnos 
                    FROM dim_escuela
                    WHERE ciudad='GUADALAJARA' AND numero_alumnos != 0
                    GROUP BY nivel;"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    resultado2 = list(resultado)
    resultado2.insert(0, ("Tipo de escuela", "Alumnos"))
    for i in range(len(resultado2)):
        if i != 0:
            resultado2[i] = [resultado2[i][0], int(resultado2[i][1])]
    return jsonify(resultado2)

# Porcentaje de escuelas de nivel publico contra nivel privado en el estado de jalisco
# Para esto se necesitan hacer los resultados de las dos consultas para poder sacar el porcentaje
# TOTAL = 15901 (100%)

# 12266 (77.2%)
@app.route("/numero-escuelas-publicas/", methods = ["GET"])
def numero_escuelas_publicas():
    cursor = mysql.connection.cursor()
    consulta = """SELECT count(*) 
                    FROM dim_escuela
                    WHERE control='PUBLICO';"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

#3635 (22.8%)
@app.route("/numero-escuelas-privadas/", methods = ["GET"])
def numero_escuelas_privadas():
    cursor = mysql.connection.cursor()
    consulta = """SELECT count(*) 
                    FROM dim_escuela
                    WHERE control='PRIVADO';"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.route("/porcentaje_publico_privadas/")
def porcentaje_publico_privadas():
    cursor = mysql.connection.cursor()
    consulta = """SELECT count(*) 
                    FROM dim_escuela
                    WHERE control='PRIVADO';"""
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    consulta = """SELECT count(*) 
                    FROM dim_escuela
                    WHERE control='PUBLICO';"""
    cursor.execute(consulta)
    resultado3 = cursor.fetchall()

    resultado2 = [["PRIVADO", resultado[0][0]], ["PUBLICO", resultado3[0][0]]]
    resultado2.insert(0, ("PRIVADO", "PUBLICO"))
    return jsonify(resultado2)

@app.route("/nueva_consulta/", methods = ["GET"])
def nueva_consulta():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(request.args.get("consulta"))
        resultado = cursor.fetchall()
        return jsonify(resultado)
    except:
        return "Consulta inválida"
# -------------------------------------------------------

@app.route("/colonia_negocios/<colonia>", methods = ["GET"])
def colonia_negocios(colonia):
    cursor = mysql.connection.cursor()
    consulta = """SELECT dim_colonia.nombre, dim_negocio.nombre, dim_negocio.giro FROM colonia_negocio 
    INNER JOIN dim_colonia on colonia_negocio.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_negocio on colonia_negocio.id_negocio = dim_negocio.id_negocio where dim_colonia.nombre = '{}'""".format(
        colonia)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.route("/ciudad_negocios/<ciudad>", methods = ["GET"])
def ciudad_negocios(ciudad):
    cursor = mysql.connection.cursor()
    consulta = """SELECT dim_colonia.nombre, dim_negocio.nombre, dim_negocio.giro FROM colonia_negocio 
    INNER JOIN dim_colonia on colonia_negocio.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_negocio on colonia_negocio.id_negocio = dim_negocio.id_negocio where dim_colonia.ciudad = '{}'""".format(
        ciudad)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.route("/colonia_escuelas/<colonia>", methods = ["GET"])
def colonia_escuelas(colonia):
    cursor = mysql.connection.cursor()
    consulta = """SELECT dim_colonia.nombre, dim_escuela.nombre, dim_escuela.nivel, dim_escuela.control FROM colonia_escuela 
    INNER JOIN dim_colonia on colonia_escuela.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_escuela on colonia_escuela.id_escuela = dim_escuela.id_escuela where dim_colonia.nombre = '{}'""".format(
        colonia)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

@app.route("/ciudad_escuelas/<ciudad>", methods = ["GET"])
def ciudad_escuelas(ciudad):
    cursor = mysql.connection.cursor()
    consulta = """SELECT dim_colonia.nombre, dim_escuela.nombre, dim_escuela.nivel, dim_escuela.control FROM colonia_escuela
    INNER JOIN dim_colonia on colonia_escuela.id_colonia = dim_colonia.id_colonia 
    inner JOIN dim_escuela on colonia_escuela.id_escuela = dim_escuela.id_escuela where dim_colonia.ciudad = '{}'""".format(
        ciudad)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

if __name__ == "__main__":
    app.run(port = 5000, debug = True)