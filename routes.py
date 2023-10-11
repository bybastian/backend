from flask import request, jsonify
from app import mysql

def create_equipo():
    data = request.get_json()
    cursor = mysql.connection.cursor()
    query = "INSERT INTO equipo (nombre, marca, modelo, serie, propietario, fecha_fabricacion, fecha_ingreso, condicion_ingreso, riesgo, id_invima, id_area) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        data['nombre'], data['marca'], data['modelo'], data['serie'], data['propietario'], data['fecha_fabricacion'],
        data['fecha_ingreso'], data['condicion_ingreso'], data['riesgo'], data['id_invima'], data['id_area']
    )
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Equipo creado'}), 201

@app.route('/equipos', methods=['GET'])
def get_equipos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM equipo")
    equipos = cursor.fetchall()
    cursor.close()
    return jsonify(equipos)

@app.route('/equipos/<int:id>', methods=['GET'])
def get_equipo(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM equipo WHERE id = %s", (id,))
    equipo = cursor.fetchone()
    cursor.close()
    return jsonify(equipo)

@app.route('/equipos/<int:id>', methods=['PUT'])
def update_equipo(id):
    data = request.get_json()
    cursor = mysql.connection.cursor()
    query = "UPDATE equipo SET nombre = %s, marca = %s, modelo = %s, serie = %s, propietario = %s, fecha_fabricacion = %s, fecha_ingreso = %s, condicion_ingreso = %s, riesgo = %s, id_invima = %s, id_area = %s WHERE id = %s"
    values = (
        data['nombre'], data['marca'], data['modelo'], data['serie'], data['propietario'], data['fecha_fabricacion'],
        data['fecha_ingreso'], data['condicion_ingreso'], data['riesgo'], data['id_invima'], data['id_area'], id
    )
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Equipo actualizado'}), 200

@app.route('/equipos/<int:id>', methods=['DELETE'])
def delete_equipo(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM equipo WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Equipo eliminado'}), 200
