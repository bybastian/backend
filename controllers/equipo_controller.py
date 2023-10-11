from flask import jsonify, request
from app import app, mysql
from repositories import EquipoRepository

def get_equipo_repository():
    return EquipoRepository(mysql.connection)

# Rutas para gestionar equipos
@app.route('/equipos', methods=['GET'])
def get_equipos():
    equipos = equipo_repository.get_equipos()
    return jsonify({'equipos': equipos})

@app.route('/equipo', methods=['POST'])
def crear_equipo():
    if request.method == 'POST':
        try:
            equipo_data = request.get_json()
            equipo_repository.crear_equipo(equipo_data)
            return jsonify({"message": "Equipo creado exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)})

@app.route('/equipo/<int:id>', methods=['PUT'])
def actualizar_equipo(id):
    if request.method == 'PUT':
        try:
            equipo_data = request.get_json()
            equipo_repository.actualizar_equipo(id, equipo_data)
            return jsonify({"message": "Equipo actualizado exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)})

@app.route('/equipo/<int:id>', methods=['DELETE'])
def eliminar_equipo(id):
    if request.method == 'DELETE':
        try:
            equipo_repository.eliminar_equipo(id)
            return jsonify({"message": "Equipo eliminado exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)})


