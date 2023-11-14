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

# Nueva ruta para tipo de historia
@app.route('/tipo_historia')
def tipo_historia():
    return render_template('tipo_historia.html')

# Nueva ruta para tipo de consulta
@app.route('/tipo_consulta')
def tipo_consulta():
    return render_template('tipo_consulta.html')

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
        vacuna_1 = request.form['vacuna_1']
        fecha_vacuna_1 = request.form['fecha_vacuna_1'] if request.form['fecha_vacuna_1'] else None
        vacuna_2 = request.form['vacuna_2']
        fecha_vacuna_2 = request.form['fecha_vacuna_2'] if request.form['fecha_vacuna_2'] else None
        vacuna_3 = request.form['vacuna_3']
        fecha_vacuna_3 = request.form['fecha_vacuna_3'] if request.form['fecha_vacuna_3'] else None
        vacuna_4 = request.form['vacuna_4']
        fecha_vacuna_4 = request.form['fecha_vacuna_4'] if request.form['fecha_vacuna_4'] else None
        vacuna_5 = request.form['vacuna_5']
        fecha_vacuna_5 = request.form['fecha_vacuna_5'] if request.form['fecha_vacuna_5'] else None
        fecha_ultima_desparasitacion = request.form['fecha_ultima_desparasitacion'] if request.form['fecha_ultima_desparasitacion'] else None
        motivo_consulta = request.form['motivo_consulta']
        sintomatologia = request.form['sintomatologia']
        tratamiento = request.form['tratamiento']
        diagnostico_diferencial = request.form['diagnostico_diferencial']
        examenes_complementarios = request.form['examenes_complementarios']
        diagnostico_definitivo = request.form['diagnostico_definitivo']
        tratamiento_final = request.form['tratamiento_final']
        medicamento_1 = request.form['medicamento_1']
        posologia_1 = request.form['posologia_1']
        medicamento_2 = request.form['medicamento_2']
        posologia_2 = request.form['posologia_2']
        medicamento_3 = request.form['medicamento_3']
        posologia_3 = request.form['posologia_3']
        medicamento_4 = request.form['medicamento_4']
        posologia_4 = request.form['posologia_4']
        medicamento_5 = request.form['medicamento_5']
        posologia_5 = request.form['posologia_5']
        proxima_cita = request.form['proxima_cita'] if request.form['proxima_cita'] else None


        # Verifica que los campos obligatorios estén llenos
        if not (cedula and propietario and direccion and medico_responsable and fecha_creacion and telefono and
                nombre_paciente and especie and sexo):
            error_message = 'Por favor, llena todos los campos obligatorios.'
        else:
            cursor = mysql.get_db().cursor()
            cursor.execute("INSERT INTO historia (cedula, propietario, direccion, medico_responsable, fecha_creacion, telefono, nombre_paciente, fecha_nacimiento, especie, raza, sexo, color, vacuna_1, fecha_vacuna_1, vacuna_2, fecha_vacuna_2, vacuna_3, fecha_vacuna_3, vacuna_4, fecha_vacuna_4, vacuna_5, fecha_vacuna_5, fecha_ultima_desparasitacion, motivo_consulta, sintomatologia, tratamiento, diagnostico_diferencial, examenes_complementarios, diagnostico_definitivo, tratamiento_final, medicamento_1, posologia_1, medicamento_2, posologia_2, medicamento_3, posologia_3, medicamento_4, posologia_4, medicamento_5, posologia_5, proxima_cita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (cedula, propietario, direccion, medico_responsable, fecha_creacion, telefono, nombre_paciente, fecha_nacimiento, especie, raza, sexo, color, vacuna_1, fecha_vacuna_1, vacuna_2, fecha_vacuna_2, vacuna_3, fecha_vacuna_3, vacuna_4, fecha_vacuna_4, vacuna_5, fecha_vacuna_5, fecha_ultima_desparasitacion, motivo_consulta, sintomatologia, tratamiento, diagnostico_diferencial, examenes_complementarios, diagnostico_definitivo, tratamiento_final, medicamento_1, posologia_1, medicamento_2, posologia_2, medicamento_3, posologia_3, medicamento_4, posologia_4, medicamento_5, posologia_5, proxima_cita))

            mysql.get_db().commit()
            cursor.close()


            return redirect(url_for('historia_creada'))

    return render_template('nueva_historia.html', error_message=error_message)

# Nueva ruta para historia clínica dermatológica
@app.route('/nueva_historia_d', methods=['GET', 'POST'])
def nueva_historia_d():
    error_message = None

    if request.method == 'POST':
        cedula_d = request.form['cedula_d']
        propietario_d = request.form['propietario_d']
        direccion_d = request.form['direccion_d']
        medico_responsable_d = request.form['medico_responsable_d']
        fecha_creacion_d = request.form['fecha_creacion_d']
        telefono_d = request.form['telefono_d']
        nombre_paciente_d = request.form['nombre_paciente_d']
        fecha_nacimiento_d = request.form['fecha_nacimiento_d']
        especie_d = request.form['especie_d']
        raza_d = request.form['raza_d']
        sexo_d = request.form['sexo_d']
        color_d = request.form['color_d']
        vacuna_1_d = request.form['vacuna_1_d']
        fecha_vacuna_1_d = request.form['fecha_vacuna_1_d'] if request.form['fecha_vacuna_1_d'] else None
        vacuna_2_d = request.form['vacuna_2_d']
        fecha_vacuna_2_d = request.form['fecha_vacuna_2_d'] if request.form['fecha_vacuna_2_d'] else None
        vacuna_3_d = request.form['vacuna_3_d']
        fecha_vacuna_3_d = request.form['fecha_vacuna_3_d'] if request.form['fecha_vacuna_3_d'] else None
        vacuna_4_d = request.form['vacuna_4_d']
        fecha_vacuna_4_d = request.form['fecha_vacuna_4_d'] if request.form['fecha_vacuna_4_d'] else None
        vacuna_5_d = request.form['vacuna_5_d']
        fecha_vacuna_5_d = request.form['fecha_vacuna_5_d'] if request.form['fecha_vacuna_5_d'] else None
        fecha_ultima_desparasitacion_d = request.form['fecha_ultima_desparasitacion_d'] if request.form['fecha_ultima_desparasitacion_d'] else None
        motivo_consulta_d = request.form['motivo_consulta_d']
        sintomatologia_d = request.form['sintomatologia_d']
        tratamiento_d = request.form['tratamiento_d']
        diagnostico_diferencial_d = request.form['diagnostico_diferencial_d']
        otras_mascotas_d = request.form['otras_mascotas_d']
        nin_casa_d = request.form['nin_casa_d']
        familia_problema_d = request.form['familia_problema_d']
        tipo_comida_d = request.form['tipo_comida_d']
        golosinas_d = request.form['golosinas_d']
        caida_pelo_d = request.form['caida_pelo_d']
        se_rasca_d = request.form['se_rasca_d']
        ambiente_d = request.form['ambiente_d']
        pasa_sol_d = request.form['pasa_sol_d']
        pasa_tierra_d = request.form['pasa_tierra_d']
        defecacion_d = request.form['defecacion_d']
        parte_enrojecida_d = request.form['parte_enrojecida_d']
        fecha_ectoparasitos_d = request.form['fecha_ectoparasitos_d']
        descrip_ectoparasitos_d = request.form['descrip_ectoparasitos_d']
        duchas_casa_d = request.form['duchas_casa_d']
        alergia_comida_d = request.form['alergia_comida_d']
        rasp_cutaneo_d = request.form['rasp_cutaneo_d']
        tricograma_d = request.form['tricograma_d']
        lampara_wood_d = request.form['lampara_wood_d']
        reflejo_otopodal_d = request.form['reflejo_otopodal_d']
        biopsia_d = request.form['biopsia_d']
        citologia_d = request.form['citologia_d']
        antibiograma_d = request.form['antibiograma_d']

        diagnostico_definitivo_d = request.form['diagnostico_definitivo_d']
        tratamiento_final_d = request.form['tratamiento_final_d']
        medicamento_1_d = request.form['medicamento_1_d']
        posologia_medicamento_1_d = request.form['posologia_medicamento_1_d']
        medicamento_2_d = request.form['medicamento_2_d']
        posologia_medicamento_2_d = request.form['posologia_medicamento_2_d']
        medicamento_3_d = request.form['medicamento_3_d']
        posologia_medicamento_3_d = request.form['posologia_medicamento_3_d']
        medicamento_4_d = request.form['medicamento_4_d']
        posologia_medicamento_4_d = request.form['posologia_medicamento_4_d']
        medicamento_5_d = request.form['medicamento_5_d']
        posologia_medicamento_5_d = request.form['posologia_medicamento_5_d']
        proxima_cita_d = request.form['proxima_cita_d'] if request.form['proxima_cita_d'] else None

        # Verifica que los campos obligatorios estén llenos
        if not (cedula_d and propietario_d and direccion_d and medico_responsable_d and fecha_creacion_d and telefono_d and
                nombre_paciente_d and especie_d and sexo_d):
            error_message = 'Por favor, llena todos los campos obligatorios.'
        else:
            cursor = mysql.get_db().cursor()
            cursor.execute("INSERT INTO historia_derma (cedula_d, propietario_d, direccion_d, medico_responsable_d, fecha_creacion_d, telefono_d, nombre_paciente_d, fecha_nacimiento_d, especie_d, raza_d, sexo_d, color_d, vacuna_1_d, fecha_vacuna_1_d, vacuna_2_d, fecha_vacuna_2_d, vacuna_3_d, fecha_vacuna_3_d, vacuna_4_d, fecha_vacuna_4_d, vacuna_5_d, fecha_vacuna_5_d, fecha_ultima_desparasitacion_d, motivo_consulta_d, sintomatologia_d, tratamiento_d, diagnostico_diferencial_d, otras_mascotas_d, nin_casa_d, familia_problema_d, tipo_comida_d, golosinas_d,caida_pelo_d, se_rasca_d, ambiente_d, pasa_sol_d, pasa_tierra_d, defecacion_d,parte_enrojecida_d, fecha_ectoparasitos_d, descrip_ectoparasitos_d, duchas_casa_d, alergia_comida_d, rasp_cutaneo_d, tricograma_d, lampara_wood_d, reflejo_otopodal_d, biopsia_d, citologia_d, antibiograma_d, diagnostico_definitivo_d, tratamiento_final_d, medicamento_1_d, posologia_medicamento_1_d, medicamento_2_d, posologia_medicamento_2_d, medicamento_3_d, posologia_medicamento_3_d, medicamento_4_d, posologia_medicamento_4_d, medicamento_5_d, posologia_medicamento_5_d, proxima_cita_d) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (cedula_d, propietario_d, direccion_d, medico_responsable_d, fecha_creacion_d, telefono_d, nombre_paciente_d, fecha_nacimiento_d, especie_d, raza_d, sexo_d, color_d, vacuna_1_d, fecha_vacuna_1_d, vacuna_2_d, fecha_vacuna_2_d, vacuna_3_d, fecha_vacuna_3_d, vacuna_4_d, fecha_vacuna_4_d, vacuna_5_d, fecha_vacuna_5_d, fecha_ultima_desparasitacion_d, motivo_consulta_d, sintomatologia_d, tratamiento_d, diagnostico_diferencial_d, otras_mascotas_d, nin_casa_d, familia_problema_d, tipo_comida_d, golosinas_d,caida_pelo_d, se_rasca_d, ambiente_d, pasa_sol_d, pasa_tierra_d, defecacion_d,parte_enrojecida_d, fecha_ectoparasitos_d, descrip_ectoparasitos_d, duchas_casa_d, alergia_comida_d, rasp_cutaneo_d, tricograma_d, lampara_wood_d, reflejo_otopodal_d, biopsia_d, citologia_d, antibiograma_d, diagnostico_definitivo_d, tratamiento_final_d, medicamento_1_d, posologia_medicamento_1_d, medicamento_2_d, posologia_medicamento_2_d, medicamento_3_d, posologia_medicamento_3_d, medicamento_4_d, posologia_medicamento_4_d, medicamento_5_d, posologia_medicamento_5_d, proxima_cita_d))
            mysql.get_db().commit()
            cursor.close()
            return redirect(url_for('historia_creada'))

    return render_template('nueva_historia_d.html', error_message=error_message)

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

# Página para buscar historias clínicas dermatológicas por cédula
@app.route('/buscar_historia_d', methods=['GET', 'POST'])
def buscar_historia_d():
    if request.method == 'POST':
        cedula_d = request.form['cedula_d']

        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM historia_derma WHERE cedula_d = %s", (cedula_d,))
        data = cursor.fetchall()
        cursor.close()

        if data:
            return render_template('resultado_busqueda_dermatologica.html', historias_dermatologicas=data)
        else:
            return render_template('error_busqueda.html', crear_nueva=True)

    return render_template('buscar_historia_d.html')

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
        vacuna_1 = request.form['vacuna_1']
        fecha_vacuna_1 = request.form['fecha_vacuna_1'] if request.form['fecha_vacuna_1'] else None
        vacuna_2 = request.form['vacuna_2']
        fecha_vacuna_2 = request.form['fecha_vacuna_2'] if request.form['fecha_vacuna_2'] else None
        vacuna_3 = request.form['vacuna_3']
        fecha_vacuna_3 = request.form['fecha_vacuna_3'] if request.form['fecha_vacuna_3'] else None
        vacuna_4 = request.form['vacuna_4']
        fecha_vacuna_4 = request.form['fecha_vacuna_4'] if request.form['fecha_vacuna_4'] else None
        vacuna_5 = request.form['vacuna_5']
        fecha_vacuna_5 = request.form['fecha_vacuna_5'] if request.form['fecha_vacuna_5'] else None
        fecha_ultima_desparasitacion = request.form['fecha_ultima_desparasitacion'] if request.form['fecha_ultima_desparasitacion'] else None
        motivo_consulta = request.form['motivo_consulta']
        sintomatologia = request.form['sintomatologia']
        tratamiento = request.form['tratamiento']
        diagnostico_diferencial = request.form['diagnostico_diferencial']
        examenes_complementarios = request.form['examenes_complementarios']
        diagnostico_definitivo = request.form['diagnostico_definitivo']
        tratamiento_final = request.form['tratamiento_final']
        
        medicamento_1 = request.form['medicamento_1']
        posologia_1 = request.form['posologia_1']
        medicamento_2 = request.form['medicamento_2']
        posologia_2 = request.form['posologia_2']
        medicamento_3 = request.form['medicamento_3']
        posologia_3 = request.form['posologia_3']
        medicamento_4 = request.form['medicamento_4']
        posologia_4 = request.form['posologia_4']
        medicamento_5 = request.form['medicamento_5']
        posologia_5 = request.form['posologia_5']
        proxima_cita = request.form['proxima_cita'] if request.form['proxima_cita'] else None

        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE historia SET propietario = %s, direccion = %s, medico_responsable = %s, cedula = %s, fecha_creacion = %s, telefono = %s, nombre_paciente = %s, fecha_nacimiento = %s, especie = %s, raza = %s, sexo = %s, color = %s, vacuna_1 = %s, fecha_vacuna_1 = %s, vacuna_2 = %s, fecha_vacuna_2 = %s, vacuna_3 = %s, fecha_vacuna_3 = %s, vacuna_4 = %s, fecha_vacuna_4 = %s, vacuna_5 = %s, fecha_vacuna_5 = %s, fecha_ultima_desparasitacion = %s, motivo_consulta = %s, sintomatologia = %s, tratamiento = %s, diagnostico_diferencial = %s, examenes_complementarios = %s, diagnostico_definitivo = %s, tratamiento_final = %s, medicamento_1 = %s, posologia_1= %s, medicamento_2 = %s, posologia_2= %s, medicamento_3 = %s, posologia_3= %s, medicamento_4 = %s, posologia_4= %s, medicamento_5 = %s, posologia_5= %s, proxima_cita= %s WHERE id = %s",
                    (propietario, direccion, medico_responsable, cedula, fecha_creacion, telefono, nombre_paciente, fecha_nacimiento, especie, raza, sexo, color, vacuna_1, fecha_vacuna_1, vacuna_2, fecha_vacuna_2, vacuna_3, fecha_vacuna_3, vacuna_4, fecha_vacuna_4, vacuna_5, fecha_vacuna_5, fecha_ultima_desparasitacion, motivo_consulta, sintomatologia, tratamiento, diagnostico_diferencial, examenes_complementarios, diagnostico_definitivo, tratamiento_final, medicamento_1, posologia_1, medicamento_2, posologia_2, medicamento_3, posologia_3, medicamento_4, posologia_4, medicamento_5, posologia_5, proxima_cita, id))
        mysql.get_db().commit()
        cursor.close()



        return redirect(url_for('historia_actualizada'))

    return render_template('editar_historia.html', historia=historia)





# Nueva ruta para mostrar la página de historia actualizada con éxito
@app.route('/historia_actualizada')
def historia_actualizada():
    return render_template('historia_actualizada.html')


# Ruta para mostrar el reporte completo
@app.route('/reporte_completo')
def reporte_completo():
    cursor = mysql.get_db().cursor()
    
    # Consulta para obtener historias generales
    cursor.execute("SELECT * FROM historia")
    historias = cursor.fetchall()

    # Consulta para obtener historias dermatológicas
    cursor.execute("SELECT * FROM historia_derma")
    historias_derma = cursor.fetchall()

    cursor.close()

    return render_template('reporte_completo.html', historias=historias, historias_derma=historias_derma)


# Ruta para mostrar el reporte de una historia clínica
@app.route('/reporte_historia/<int:id>')
def reporte_historia(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM historia WHERE id = %s", (id,))
    historia = cursor.fetchone()
    cursor.close()

    return render_template('reporte_historia.html', historia=historia)

# Ruta para mostrar el reporte de una historia clínica dermatológica
@app.route('/reporte_historia_d/<int:id>')
def reporte_historia_d(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM historia_derma WHERE id = %s", (id,))
    historia_derma = cursor.fetchone()
    cursor.close()

    return render_template('reporte_historia_d.html', historia_derma=historia_derma)



if __name__ == '__main__':
    app.run()