from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configura la base de datos utilizando las credenciales que proporcionaste
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0707MT60FZxSp35*'
app.config['MYSQL_DB'] = 'asistente'

# Configura la extensión MySQL
mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)

