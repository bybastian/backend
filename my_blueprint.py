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
