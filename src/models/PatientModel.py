from ..database.db import get_connection
from ..entities.Patient import Patient


class PatientModel:

    def __init__(self, id_paciente, nombres, apellidos, fecha_nacimiento, edad, tipo_documento, num_identificacion, eapb, regimen):
        self.id_paciente = id_paciente
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.tipo_documento = tipo_documento
        self.num_identificacion = num_identificacion
        self.eapb = eapb
        self.regimen = regimen

    
    @staticmethod
    def get_all():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario_pat")
            pacientes_data = cursor.fetchall()
            cursor.close()
            conn.close()

            # Convertir los datos en una lista de objetos Patient
            pacientes = [Patient(*data) for data in pacientes_data]
            return pacientes
        except Exception as e:
            return str(e), 500
    