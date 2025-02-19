from ..database.db import get_connection
from ..entities.Form_radiologo import FormRadiologo

class FormRadiologoModel:

    def __init__(self, id_formulario_radiologo, id_paciente, id_especialista, fecha_toma_examen, institucion_prestadora, tipo_examen, resultado_mamog_tamizacion, resultado_mamog_diagnostica, resultado_mamog_mamaria, conducta_sugerida):
        self.id = id_formulario_radiologo
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.fecha_toma_examen = fecha_toma_examen
        self.institucion_prestadora = institucion_prestadora
        self.tipo_examen = tipo_examen
        self.resultado_mamog_tamizacion = resultado_mamog_tamizacion
        self.resultado_mamog_diagnostica = resultado_mamog_diagnostica
        self.resultado_mamog_mamaria = resultado_mamog_mamaria
        self.conducta_sugerida = conducta_sugerida
    
    @staticmethod
    def get_by_patient_id(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM formulario_radiologo WHERE id_paciente = %s"
            cursor.execute(query, (id,))
            forms_data = cursor.fetchall()
            cursor.close()
            conn.close()

            # Convertir los datos en una lista de objetos FormRadiologo
            forms = [FormRadiologo(*data) for data in forms_data]
            return forms
        except Exception as e:
            print('ERROR: al consultar la tabla formulario_radiologo',e)
            return str(e), 500
    
    @staticmethod
    def add(formulario):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO formulario_radiologo (id_formulario_radiologo, id_paciente, id_especialista, fecha_toma_examen, institucion_prestadora, tipo_examen, resultado_mamog_tamizacion, resultado_mamog_diagnostica, resultado_mamog_mamaria, conducta_sugerida)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_formulario_radiologo
            """, (formulario.id, formulario.id_paciente, formulario.id_especialista, formulario.fecha_toma_examen, formulario.institucion_prestadora, formulario.tipo_examen, formulario.resultado_mamog_tamizacion, formulario.resultado_mamog_diagnostica, formulario.resultado_mamog_mamaria, formulario.conducta_sugerida))
            formulario.id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return formulario.__dict__
        except Exception as e:
            print('ERROR: al consultar la tabla formulario_radiologo',e)
            return str(e), 500
         