from flask import Flask
from flask_mysqldb import MySQL
import config  # Importa el módulo de configuración desde config.py

app = Flask(__name)

# Configura la base de datos utilizando los valores del archivo de configuración
app.config['MYSQL_HOST'] = 127.0.0.1:3306
app.config['MYSQL_USER'] = root
app.config['MYSQL_PASSWORD'] = 0707MT60FZxSp35
app.config['MYSQL_DB'] = asistente

mysql = MySQL(app)

# Define las rutas y controladores aquív

if __name__ == '__main__':
    app.run(debug=True)
