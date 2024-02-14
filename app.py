from flask import Flask, jsonify
from flask_mysqldb import MySQL
from my_blueprint import my_blueprint  # Importa el Blueprint desde my_blueprint.py
from flask_cors import CORS

app = Flask(__name__)

# Configura la base de datos utilizando las credenciales
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0000'
app.config['MYSQL_DB'] = 'barbercite'

app.register_blueprint(my_blueprint)  # Registra el Blueprint en la aplicación

# Configura la extensión MySQL
mysql = MySQL(app)

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)