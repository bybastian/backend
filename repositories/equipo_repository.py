class EquipoRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_equipos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM equipo;")
            equipos = cursor.fetchall()

            # Convierte los resultados a una lista de diccionarios
            equipos_as_dicts = []
            column_names = [d[0] for d in cursor.description]
            for equipo in equipos:
                equipo_dict = dict(zip(column_names, equipo))
                equipos_as_dicts.append(equipo_dict)

            cursor.close()

            # Agrega mensajes de depuración aquí
            print("Equipos obtenidos de la base de datos:")
            print(equipos_as_dicts)

            return equipos_as_dicts
        except Exception as e:
            print("Error al obtener equipos de la base de datos:", str(e))
            return {"error": str(e)}

   