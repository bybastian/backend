from flask import jsonify, request
from app import app, mysql
from repositories import eventos_repository

eventos_repository = evento(mysql.connection)

# Rutas para gestionar eventos
@app.route('/eventos', methods=['GET'])
def get_eventos():
    eventos = eventos_repository.get_eventos()
    return jsonify({'eventos': eventos})

@app.route('/evento', methods=['POST'])
def crear_evento():
    if request.method == 'POST':
        try:
            evento_data = request.get_json()
            eventos_repository.crear_evento(evento_data)
            return jsonify({"message": "Evento creado exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)})

@app.route('/evento/<int:id>', methods=['PUT'])
def actualizar_evento(id):
    if request.method == 'PUT':
        try:
            evento_data = request.get_json()
            eventos_repository.actualizar_evento(id, evento_data)
            return jsonify({"message": "Evento actualizado exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)})

@app.route('/evento/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    if request.method == 'DELETE':
        try:
            eventos_repository.eliminar_evento(id)
            return jsonify({"message": "Evento eliminado exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)})
