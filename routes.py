from flask import Flask, request, render_template, redirect, url_for
from models import Record, records

app = Flask(__name)

# Ruta para listar registros
@app.route('/')
def index():
    return "Lista de registros"

# Ruta para crear un nuevo registro
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Procesar los datos del formulario y agregar un nuevo registro
        new_record = Record(
            id=len(records) + 1,
            name=request.form['name'],
            description=request.form['description']
        )
        records.append(new_record)
        return redirect(url_for('index'))
    return "Formulario para crear un registro"

# Ruta para actualizar un registro
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    # Lógica para actualizar un registro
    return "Formulario para actualizar un registro"

# Ruta para eliminar un registro
@app.route('/delete/<int:id>')
def delete(id):
    # Lógica para eliminar un registro
    return "Eliminando registro"

if __name__ == '__main__':
    app.run(debug=True)
