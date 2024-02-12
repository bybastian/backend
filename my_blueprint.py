from MySQLdb import OperationalError
from flask import Blueprint, jsonify, request

my_blueprint = Blueprint('my_blueprint', __name__)

# Get --> Traer
# Post --> Crear
# Put --> Editar
# Delete --> Eliminar
@my_blueprint.route('/', methods=['GET'])
def get_citas_route():
    from repositories.citas_repository import CitasRepository
    from app import mysql  # Importa la conexión aquí solo para esta función
    
    try:
        cita_repository = CitasRepository(mysql.connection)
        citas = cita_repository.get_citas()

        # Formatea los datos a una lista de diccionarios
        formatted_citas = []

        for cita in citas:
            cita_dict = {
                "id": cita["id"],
                "nombre": cita["nombre"],
                "fecha": cita["fecha"].strftime("%Y-%m-%d"),
                "hora": str(cita["hora"])
            }

            formatted_citas.append(cita_dict)

        return jsonify({'citas': formatted_citas})
    except OperationalError as e:
        # Manejo de error de base de datos
        print(f"Error de base de datos: {str(e)}")
        return jsonify({'error': 'Error en la base de datos'})
    

@my_blueprint.route('/equipos', methods=['POST'])
def create_equipo_route():
    from repositories.citas_repository import EquipoRepository
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
    equipo_id = equipo_repository.create_equipo(nombre, marca, modelo, serie, propietario, fecha_fabricacion,
                                                fecha_ingreso, condicion_ingreso, riesgo, id_invima, id_area)

    if isinstance(equipo_id, int):
        return jsonify({'message': 'Equipo creado exitosamente', 'equipo_id': equipo_id}), 201
    else:
        return jsonify({'error': 'Error al crear el equipo', 'details': equipo_id}), 500

@my_blueprint.route('/equipos/<int:equipo_id>', methods=['PUT'])
def update_equipo_route(equipo_id):
    from repositories.citas_repository import EquipoRepository
    from app import mysql  # Importa la conexión aquí solo para esta función

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
    from repositories.citas_repository import EquipoRepository
    from app import mysql  # Importa la conexión aquí solo para esta función
    # Crea una instancia de EquipoRepository
    equipo_repository = EquipoRepository(mysql.connection)

    # Llama a la función para eliminar un equipo
    success = equipo_repository.delete_equipo(equipo_id)

    if success:
        return jsonify({'message': 'Equipo eliminado exitosamente'}), 200
    else:
        return jsonify({'error': 'Error al eliminar el equipo'}), 500
