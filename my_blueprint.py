from flask import Blueprint, jsonify, request

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/equipos', methods=['GET'])
def get_equipos_route():
    from repositories.equipo_repository import EquipoRepository
    from app import mysql  # Importa la conexión aquí solo para esta función
    
    equipo_repository = EquipoRepository(mysql.connection)
    equipos = equipo_repository.get_equipos()

    for equipo in equipos:
        print(equipo)  # Imprime un ejemplo de equipo en la consola
        print(type(equipo))


    # Formatea los datos a una lista de diccionarios
    formatted_equipos = []

    for equipo in equipos:
        formatted_equipos.append({
            "id": equipo["id"],
            "nombre": equipo["nombre"],
            "marca": equipo["marca"],
            "modelo": equipo["modelo"],
            "serie": equipo["serie"],
            "propietario": equipo["propietario"],
            "fecha_fabricacion": equipo["fecha_fabricacion"].strftime("%Y-%m-%d"),
            "fecha_ingreso": equipo["fecha_ingreso"].strftime("%Y-%m-%d"),
            "condicion_ingreso": equipo["condicion_ingreso"],
            "riesgo": equipo["riesgo"],
            "id_invima": equipo["id_invima"],
            "id_area": equipo["id_area"]
        })

    return jsonify({'equipos': formatted_equipos})

@my_blueprint.route('/equipos', methods=['POST'])
def create_equipo_route():
    from repositories.equipo_repository import EquipoRepository
    from app import mysql  # Importa la conexión aquí solo para esta función

    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Datos no proporcionados en el cuerpo de la solicitud'}), 400

    nombre = data.get("nombre")
    marca = data.get("marca")
    modelo = data.get("modelo")
    serie = data.get("serie")
    propietario = data.get("propietario")
    fecha_fabricacion = data.get("fecha_fabricacion")
    fecha_ingreso = data.get("fecha_ingreso")
    condicion_ingreso = data.get("condicion_ingreso")
    riesgo = data.get("riesgo")
    id_invima = data.get("id_invima")
    id_area = data.get("id_area")

    # Crea una instancia de EquipoRepository
    equipo_repository = EquipoRepository(mysql.connection)  # Asegúrate de que `mysql` esté configurado correctamente

    # Llama a la función para crear un equipo
    equipo_id = equipo_repository.create_equipo(nombre, marca, modelo, serie, propietario, fecha_fabricacion, fecha_ingreso, condicion_ingreso, riesgo, id_invima, id_area)

    if isinstance(equipo_id, int):
        return jsonify({'message': 'Equipo creado exitosamente', 'equipo_id': equipo_id}), 201
    else:
        return jsonify({'error': 'Error al crear el equipo', 'details': equipo_id}), 500

@my_blueprint.route('/equipos/<int:equipo_id>', methods=['PUT'])
def update_equipo_route(equipo_id):
    data = request.get_json()
    nombre = data.get("nombre")
    marca = data.get("marca")
    # ... otros campos ...

    # Crea una instancia de EquipoRepository
    equipo_repository = EquipoRepository(mysql.connection)

    # Llama a la función para actualizar un equipo
    success = equipo_repository.update_equipo(equipo_id, nombre, marca, ...)  # Pasa todos los campos necesarios

    if success:
        return jsonify({'message': 'Equipo actualizado exitosamente'}), 200
    else:
        return jsonify({'error': 'Error al actualizar el equipo'}), 500


@my_blueprint.route('/equipos/<int:equipo_id>', methods=['DELETE'])
def delete_equipo_route(equipo_id):
    # Crea una instancia de EquipoRepository
    equipo_repository = EquipoRepository(mysql.connection)

    # Llama a la función para eliminar un equipo
    success = equipo_repository.delete_equipo(equipo_id)

    if success:
        return jsonify({'message': 'Equipo eliminado exitosamente'}), 200
    else:
        return jsonify({'error': 'Error al eliminar el equipo'}), 500
