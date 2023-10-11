from flask import jsonify, request
from controllers.equipo_controller import get_equipo_repository

# Esto debe estar dentro de una vista de Flask
def some_view():
    equipo_repository = get_equipo_repository()

# Ruta POST para crear un nuevo equipo
@app.route('/equipos', methods=['GET'])
def get_equipos_route():
    equipos = get_equipos()  # Invoca la función para obtener los equipos desde tu controlador
    return jsonify({'equipos': equipos})

# Ruta PUT para actualizar un equipo por su ID
@app.route('/equipo/<int:id>', methods=['PUT'])
def actualizar_equipo_route(id):
    # Llama a la función actualizar_equipo o el método correspondiente de EquipoRepository
    return actualizar_equipo(id, request)

# Ruta DELETE para eliminar un equipo por su ID
@app.route('/equipo/<int:id>', methods=['DELETE'])
def eliminar_equipo_route(id):
    # Llama a la función eliminar_equipo o el método correspondiente de EquipoRepository
    return eliminar_equipo(id)