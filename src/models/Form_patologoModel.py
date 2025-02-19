from ..database.db import get_connection
from ..entities.Form_patologo import FormPatologo

class FormPatologoModel:

    def __init__(self, id_formulario_patologo, id_paciente, id_especialista, fecha_ingreso_muestra, fecha_lectura_patologica, num_estudio_anatomopatologico, institucion_prestadora, tipo_biopsia, lesiones_proliferativas, lesiones_fibroepiteliales, lesiones_papilares, lesiones_intraductuales, neoplasia_lobulillar, carcinoma_infiltrante, otros, conducta_sugerida_patologo, fecha_toma_examen):
        self.id = id_formulario_patologo
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.fecha_ingreso_muestra = fecha_ingreso_muestra
        self.fecha_lectura_patologica = fecha_lectura_patologica
        self.num_estudio_anatomopatologico = num_estudio_anatomopatologico
        self.institucion_prestadora = institucion_prestadora
        self.tipo_biopsia = tipo_biopsia
        self.lesiones_proliferativas = lesiones_proliferativas
        self.lesiones_fibroepiteliales = lesiones_fibroepiteliales
        self.lesiones_papilares = lesiones_papilares
        self.lesiones_intraductuales = lesiones_intraductuales
        self.neoplasia_lobulillar = neoplasia_lobulillar
        self.carcinoma_infiltrante = carcinoma_infiltrante
        self.otros = otros
        self.conducta_sugerida_patologo = conducta_sugerida_patologo
        self.fecha_toma_examen = fecha_toma_examen
    
    @staticmethod
    def get_by_patient_id(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM formulario_patologo WHERE id_paciente = %s"
            cursor.execute(query, (id,))
            forms_data = cursor.fetchall()
            cursor.close()
            conn.close()

            # Convertir los datos en una lista de objetos FormPatologo
            forms = [FormPatologo(*data) for data in forms_data]
            return forms
        except Exception as e:
            print('ERROR: al consultar la tabla formulario_patologo',e)
            return str(e), 500
    
    @staticmethod
    def add(formulario):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO formulario_patologo (id_formulario_patologo, id_paciente, id_especialista, fecha_ingreso_muestra, fecha_lectura_patologica, num_estudio_anatomopatologico, institucion_prestadora, tipo_biopsia, lesiones_proliferativas, lesiones_fibroepiteliales, lesiones_papilares, lesiones_intraductuales, neoplasia_lobulillar, carcinoma_infiltrante, otros, conducta_sugerida_patologo, fecha_toma_examen)
                VALUES (%, %, %, %, %, %, %, %, %, %, %, %, %, %, %, %, %) RETURNING id_formulario_patologo
            """, (formulario.id, formulario.id_paciente, formulario.id_especialista, formulario.fecha_ingreso_muestra, formulario.fecha_lectura_patologica, formulario.num_estudio_anatomopatologico, formulario.institucion_prestadora, formulario.tipo_biopsia, formulario.lesiones_proliferativas, formulario.lesiones_fibroepiteliales, formulario.lesiones_papilares, formulario.lesiones_intraductuales, formulario.neoplasia_lobulillar, formulario.carcinoma_infiltrante, formulario.otros, formulario.conducta_sugerida_patologo, formulario.fecha_toma_examen))
            formulario.id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return formulario.__dict__
        except Exception as e:
            return str(e), 500
    
    @staticmethod
    def get_by_id(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM formulario_patologo WHERE id_formulario_patologo = %s", (id,))
            form_data = cursor.fetchone()
            cursor.close()
            conn.close()
            if form_data:
                form = FormPatologo(*form_data)
                return form
            else:
                return None
        except Exception as e:
            return str(e), 500
        