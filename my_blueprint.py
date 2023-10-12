from flask import Blueprint, jsonify, request
from repositories.equipo_repository import EquipoRepository
my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/equipos', methods=['GET'])
def get_equipos_route():
    equipos = EquipoRepository.get_equipos()

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
