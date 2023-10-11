from flask import jsonify, request
from repositories import EquipoRepository

equipo_repository = EquipoRepository(app.config['MYSQL'])


# Ruta POST para crear un nuevo equipo
@app.route('/equipo', methods=['POST'])
def crear_equipo_route():
    return crear_equipo(request)

# Ruta PUT para actualizar un equipo por su ID
@app.route('/equipo/<int:id>', methods=['PUT'])
def actualizar_equipo_route(id):
    return actualizar_equipo(id, request)

# Ruta DELETE para eliminar un equipo por su ID
@app.route('/equipo/<int:id>', methods=['DELETE'])
def eliminar_equipo_route(id):
    return eliminar_equipo(id)


@app.route('/eventos', methods=['GET'])
def get_eventos():
    return eventos_controller.get_eventos()

@app.route('/eventos', methods=['POST'])
def crear_evento():
    return eventos_controller.crear_evento()

@app.route('/eventos/<int:id>', methods=['PUT'])
def actualizar_evento(id):
    return eventos_controller.actualizar_evento(id)

@app.route('/eventos/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    return eventos_controller.eliminar_evento(id)