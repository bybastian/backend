from flask import jsonify, request
from app import app, mysql
from repositories import EquipoRepository

# Esto debe estar dentro de una función o vista
def some_view():
    equipo_repository = EquipoRepository(mysql.connection)

class EquipoRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_equipos(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM equipo")
            equipos = cursor.fetchall()
            cursor.close()
            return equipos
        except Exception as e:
            return {"error": str(e)}

    def crear_equipo(self, equipo_data):
        try:
            cursor = self.connection.cursor(dictionary=True)
            insert_query = (
                "INSERT INTO equipo "
                "(nombre, marca, modelo, serie, propietario, fecha_fabricacion, fecha_ingreso, condicion_ingreso, riesgo, id_invima, id_area) "
                "VALUES (%(nombre)s, %(marca)s, %(modelo)s, %(serie)s, %(propietario)s, %(fecha_fabricacion)s, %(fecha_ingreso)s, %(condicion_ingreso)s, %(riesgo)s, %(id_invima)s, %(id_area)s)"
            )
            cursor.execute(insert_query, equipo_data)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            return {"error": str(e)}

    def actualizar_equipo(self, id, equipo_data):
        try:
            cursor = self.connection.cursor(dictionary=True)
            update_query = (
                "UPDATE equipo "
                "SET nombre = %(nombre)s, marca = %(marca)s, modelo = %(modelo)s, serie = %(serie)s, propietario = %(propietario)s, "
                "fecha_fabricacion = %(fecha_fabricacion)s, fecha_ingreso = %(fecha_ingreso)s, condicion_ingreso = %(condicion_ingreso)s, "
                "riesgo = %(riesgo)s, id_invima = %(id_invima)s, id_area = %(id_area)s "
                "WHERE id = %(id)s"
            )
            equipo_data["id"] = id
            cursor.execute(update_query, equipo_data)
            if cursor.rowcount > 0:
                self.connection.commit()
            cursor.close()
        except Exception as e:
            return {"error": str(e)}

    def eliminar_equipo(self, id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            delete_query = "DELETE FROM equipo WHERE id = %(id)s"
            cursor.execute(delete_query, {"id": id})
            if cursor.rowcount > 0:
                self.connection.commit()
            cursor.close()
        except Exception as e:
            return {"error": str(e)}
