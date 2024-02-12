from app import mysql  # Importa la instancia de MySQL desde app.py
from repositories.citas_repository import Citas

equipo_repository = Citas(mysql.connection)
