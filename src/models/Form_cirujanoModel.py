from ..database.db import get_connection
from ..entities.Form_cirujano_mama import FormCirujano

class FormCirujanoModel:

    def __init__(self, id_formulario_cirujano, id_paciente, id_especialista, fecha_toma_examen, institucion_prestadora, motivo_remision, conducta_tomada, estadificacion_clinica, conducta_paciente, fecha_inicio_tratamiento):
        self.id = id_formulario_cirujano
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.fecha_toma_examen = fecha_toma_examen
        self.institucion_prestadora = institucion_prestadora
        self.motivo_remision = motivo_remision
        self.conducta_tomada = conducta_tomada
        self.estadificacion_clinica = estadificacion_clinica
        self.conducta_paciente = conducta_paciente
        self.fecha_inicio_tratamiento = fecha_inicio_tratamiento
    
    @staticmethod
    def get_by_patient_id(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM formulario_cirujano_mama WHERE id_paciente = %s"
            cursor.execute(query, (id,))
            forms_data = cursor.fetchall()
            cursor.close()
            conn.close()

            # Convertir los datos en una lista de objetos FormCirujano
            forms = [FormCirujano(*data) for data in forms_data]
            return forms
        except Exception as e:
            print('ERROR: al consultar la tabla formulario_cirujano',e)
            return str(e), 500
    
    @staticmethod
    def add(formulario):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO formulario_cirujano_mama (id_formulario_cirujano, id_paciente, id_especialista, fecha_toma_examen, institucion_prestadora, motivo_remision, conducta_tomada, estadificacion_clinica, conducta_paciente, fecha_inicio_tratamiento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_formulario_cirujano
            """, (formulario.id, formulario.id_paciente, formulario.id_especialista, formulario.fecha_toma_examen, formulario.institucion_prestadora, formulario.motivo_remision, formulario.conducta_tomada, formulario.estadificacion_clinica, formulario.conducta_paciente, formulario.fecha_inicio_tratamiento))
            formulario.id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return formulario.__dict__
        except Exception as e:
            return str(e), 500
