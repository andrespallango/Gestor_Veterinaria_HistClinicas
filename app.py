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
        propietario = request.form['propietario']
        direccion = request.form['direccion']
        medico_responsable = request.form['medico_responsable']
        fecha_creacion = request.form['fecha_creacion']
        telefono = request.form['telefono']
        nombre_paciente = request.form['nombre_paciente']
        fecha_nacimiento = request.form['fecha_nacimiento']
        especie = request.form['especie']
        raza = request.form['raza']
        sexo = request.form['sexo']
        color = request.form['color']

        # Verifica que los campos obligatorios estén llenos
        if not (cedula and propietario and direccion and medico_responsable and fecha_creacion and telefono and
                nombre_paciente and especie and sexo):
            error_message = 'Por favor, llena todos los campos obligatorios.'
        else:
            cursor = mysql.get_db().cursor()
            cursor.execute("INSERT INTO historia (cedula, propietario, direccion, medico_responsable, fecha_creacion, telefono, nombre_paciente, fecha_nacimiento, especie, raza, sexo, color) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (cedula, propietario, direccion, medico_responsable, fecha_creacion, telefono, nombre_paciente, fecha_nacimiento, especie, raza, sexo, color))
            mysql.get_db().commit()
            cursor.close()

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
        propietario = request.form['propietario']
        direccion = request.form['direccion']
        medico_responsable = request.form['medico_responsable']
        fecha_creacion = request.form['fecha_creacion']  
        telefono = request.form['telefono']
        nombre_paciente = request.form['nombre_paciente']
        fecha_nacimiento = request.form['fecha_nacimiento']
        especie = request.form['especie']
        raza = request.form['raza']
        sexo = request.form['sexo']
        color = request.form['color']

        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE historia SET propietario = %s, direccion = %s, medico_responsable = %s, cedula = %s, fecha_creacion = %s, telefono = %s, nombre_paciente = %s, fecha_nacimiento = %s, especie = %s, raza = %s, sexo = %s, color = %s WHERE id = %s",
                       (propietario, direccion, medico_responsable, cedula, fecha_creacion, telefono, nombre_paciente, fecha_nacimiento, especie, raza, sexo, color, id))
        mysql.get_db().commit()
        cursor.close()

        return redirect(url_for('historia_actualizada'))

    return render_template('editar_historia.html', historia=historia)






# Nueva ruta para mostrar la página de historia actualizada con éxito
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