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

@my_blueprint.route('/created', methods=['POST'])
def create_cita():
    from repositories.citas_repository import CitasRepository
    from app import mysql

    data = request.get_json()

    nombre = data.get("nombre")
    fecha = data.get("fecha")
    hora = data.get("hora")

    citas_repository = CitasRepository(mysql.connection)
    result = citas_repository.create_cita(nombre, fecha, hora)

    if 'message' in result:
        return jsonify({'message': result['message']})
    else:
        return jsonify({'error': 'Fallo en la creación de la cita'})


@my_blueprint.route('/updated', methods=['PUT'])
def update_cita(self, cita_id, nombre, fecha, hora):
    try:
        cursor = self.connection.cursor()
        cursor.execute("UPDATE citas SET nombre = %s, fecha = %s, hora = %s WHERE id = %s;",
                           (nombre, fecha, hora, cita_id))
        self.connection.commit()
        cursor.close()
        return {"message": "Cita actualizada exitosamente"}
    except OperationalError as e:
        print("Error al actualizar cita en la base de datos:", str(e))
        return {"error": "Error en la base de datos"}

@my_blueprint.route('/delete/<int:cita_id>', methods=['DELETE'])
def delete_cita(cita_id):
    from repositories.citas_repository import CitasRepository
    from app import mysql

    citas_repository = CitasRepository(mysql.connection)

    success = citas_repository.delete_cita(cita_id)

    if success:
        return jsonify({'message': 'Cita eliminada correctamente'}), 200
    else:
        return jsonify({'error': 'Error al eliminar la cita agendad'}), 500

    