class EventoRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_eventos(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM eventos")
            eventos = cursor.fetchall()
            cursor.close()
            return eventos
        except Exception as e:
            return {"error": str(e)}

    def crear_evento(self, evento_data):
        try:
            cursor = self.connection.cursor(dictionary=True)
            insert_query = (
                "INSERT INTO eventos "
                "(tipo_evento, estado_evento, fecha, evidencia_fotografica, evidencia_textual, evidencia_documento, id_equipo) "
                "VALUES (%(tipo_evento)s, %(estado_evento)s, %(fecha)s, %(evidencia_fotografica)s, %(evidencia_textual)s, %(evidencia_documento)s, %(id_equipo)s)"
            )
            cursor.execute(insert_query, evento_data)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            return {"error": str(e)}

    def actualizar_evento(self, id, evento_data):
        try:
            cursor = self.connection.cursor(dictionary=True)
            update_query = (
                "UPDATE eventos "
                "SET tipo_evento = %(tipo_evento)s, estado_evento = %(estado_evento)s, fecha = %(fecha)s, "
                "evidencia_fotografica = %(evidencia_fotografica)s, evidencia_textual = %(evidencia_textual)s, "
                "evidencia_documento = %(evidencia_documento)s, id_equipo = %(id_equipo)s "
                "WHERE id = %(id)s"
            )
            evento_data["id"] = id
            cursor.execute(update_query, evento_data)
            if cursor.rowcount > 0:
                self.connection.commit()
            cursor.close()
        except Exception as e:
            return {"error": str(e)}

    def eliminar_evento(self, id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            delete_query = "DELETE FROM eventos WHERE id = %(id)s"
            cursor.execute(delete_query, {"id": id})
            if cursor.rowcount > 0:
                self.connection.commit()
            cursor.close()
        except Exception as e:
            return {"error": str(e)}
