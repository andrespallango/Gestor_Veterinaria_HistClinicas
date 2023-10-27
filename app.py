# Importar las bibliotecas necesarias
from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'secretkey2023'  # Clave secreta para la sesión

# Configuración de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'veterinaria'

mysql = MySQL(app)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nueva_historia', methods=['GET', 'POST'])
def nueva_historia():
    error_message = None  # Inicializa el mensaje de error como nulo

    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        tratamiento = request.form['tratamiento']

        # Verifica que los campos obligatorios estén llenos
        if not (cedula and nombre and direccion and tratamiento):
            error_message = 'Por favor, llena todos los campos obligatorios.'
        else:
            cursor = mysql.get_db().cursor()
            cursor.execute("INSERT INTO historia (cedula, nombre, direccion, tratamiento) VALUES (%s, %s, %s, %s)",
                           (cedula, nombre, direccion, tratamiento))
            mysql.get_db().commit()
            cursor.close()

            flash('Historia creada exitosamente', 'success')
            return redirect(url_for('historia_creada'))

    return render_template('nueva_historia.html', error_message=error_message)



# Nueva ruta para mostrar la página de historia creada con éxito
@app.route('/historia_creada')
def historia_creada():
    return render_template('historia_creada.html')

# Página para buscar historias clínicas por cédula
@app.route('/buscar_historia', methods=['GET', 'POST'])
def buscar_historia():
    if request.method == 'POST':
        cedula = request.form['cedula']

        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM historia WHERE cedula = %s", (cedula,))
        data = cursor.fetchall()
        cursor.close()

        if data:
            return render_template('resultado_busqueda.html', historias=data)
        else:
            return render_template('error_busqueda.html', crear_nueva=True)

    return render_template('buscar_historia.html')

# Ruta para mostrar la página de confirmación de borrado
@app.route('/confirmar_borrar_historia/<int:id>')
def confirmar_borrar_historia(id):
    historia_borrada = False  # Inicialmente, la historia no ha sido borrada
    return render_template('confirmacion_borrar_historia.html', id=id, historia_borrada=historia_borrada)


# Ruta para borrar una historia
@app.route('/borrar_historia/<int:id>')
def borrar_historia(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("DELETE FROM historia WHERE id = %s", (id,))
    mysql.get_db().commit()
    cursor.close()
    historia_borrada = True  # La historia ha sido borrada con éxito
    return render_template('confirmacion_borrar_historia.html', id=id, historia_borrada=historia_borrada)



# Ruta para mostrar la página de edición de historia clínica
@app.route('/editar_historia/<int:id>', methods=['GET', 'POST'])
def editar_historia(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM historia WHERE id = %s", (id,))
    historia = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        id = request.form['id']
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        tratamiento = request.form['tratamiento']

        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE historia SET nombre = %s, direccion = %s, tratamiento = %s, cedula = %s WHERE id = %s",
                       (nombre, direccion, tratamiento, cedula, id))
        mysql.get_db().commit()
        cursor.close()

        flash('Los datos de la historia clínica han sido actualizados con éxito', 'success')
        return redirect(url_for('historia_actualizada'))

    return render_template('editar_historia.html', historia=historia)



# Nueva ruta para mostrar la página de historia actualizada con éxitozz
@app.route('/historia_actualizada')
def historia_actualizada():
    return render_template('historia_actualizada.html')



@app.route('/reporte_completo')
def reporte_completo():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM historia")
    historias = cursor.fetchall()
    cursor.close()
    return render_template('reporte_completo.html', historias=historias)

# Ruta para mostrar el reporte de una historia clínica
@app.route('/reporte_historia/<int:id>')
def reporte_historia(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM historia WHERE id = %s", (id,))
    historia = cursor.fetchone()
    cursor.close()

    return render_template('reporte_historia.html', historia=historia)


if __name__ == '__main__':
    app.run()