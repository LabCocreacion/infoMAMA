class FormPatologo:
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
        