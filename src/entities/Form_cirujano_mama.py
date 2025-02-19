class FormCirujano:
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