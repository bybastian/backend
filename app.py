from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configura la base de datos utilizando los valores aquí
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0707MT60FZxSp35'
app.config['MYSQL_DB'] = 'asistente'

mysql = MySQL(app)  # Configura la extensión MySQL

if __name__ == '__main__':
    app.run(debug=True)

# Registra las rutas después de definir la app y configurar MySQL
from routes import create_equipo, get_equipos, get_equipo, update_equipo, delete_equipo

app.add_url_rule('/equipos', 'create_equipo', create_equipo, methods=['POST'])
app.add_url_rule('/equipos', 'get_equipos', get_equipos, methods=['GET'])
app.add_url_rule('/equipos/<int:id>', 'get_equipo', get_equipo, methods=['GET'])
app.add_url_rule('/equipos/<int:id>', 'update_equipo', update_equipo, methods=['PUT'])
app.add_url_rule('/equipos/<int:id>', 'delete_equipo', delete_equipo, methods=['DELETE'])