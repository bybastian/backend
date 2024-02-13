class CitasRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_citas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM citas;")
            equipos = cursor.fetchall()

            # Convierte los resultados a una lista de diccionarios
            equipos_as_dicts = []
            column_names = [d[0] for d in cursor.description]
            for equipo in equipos:
                equipo_dict = dict(zip(column_names, equipo))
                equipos_as_dicts.append(equipo_dict)

            cursor.close()

            return equipos_as_dicts
        except Exception as e:
            print("Error al obtener equipos de la base de datos:", str(e))
            return {"error": str(e)}

    def create_cita(self, nombre, fecha, hora):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """INSERT INTO citas (nombre, fecha, hora) VALUES (%s, %s, %s);""", 
                           (nombre, fecha, hora))
            
            self.connection.commit()
            cursor.close()
            return {"message": "Cita creada exitosamente"}
        
        except Exception as e:
            print("Error al crear cita en la base de datos:", str(e))
            return {"error": str(e)}

    def update_cita(self, cita_id, nombre, fecha, hora):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE citas SET nombre = %s, fecha = %s, hora = %s WHERE id = %s;",
                           (nombre, fecha, hora, cita_id))
            self.connection.commit()
            cursor.close()
            return {"message": "Cita actualizada exitosamente"}
        except Exception as e:
            print("Error al actualizar cita en la base de datos:", str(e))
            return {"error": str(e)}

    def delete_cita(self, cita_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM citas WHERE id = %s;", (cita_id,))
            self.connection.commit()
            cursor.close()
            return {"message": "Cita eliminada exitosamente"}
        except Exception as e:
            print("Error al eliminar cita en la base de datos:", str(e))
            return {"error": str(e)}

