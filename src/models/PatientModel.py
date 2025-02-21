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
    
    @staticmethod
    def add(new_patient):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario_pat (id_paciente, nombres, apellidos, fecha_nacimiento, edad, tipo_documento, num_identificacion, eapb, regimen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (new_patient.id_paciente, new_patient.nombres, new_patient.apellidos, new_patient.fecha_nacimiento, new_patient.edad, new_patient.tipo_documento, new_patient.num_identificacion, new_patient.eapb, new_patient.regimen))
            conn.commit()
            cursor.close()
            conn.close()
            return "Paciente creado correctamente"
        except Exception as e:
            return str(e), 500
    
    @staticmethod
    def get_by_id(num_identificacion):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario_pat WHERE num_identificacion = %s", (num_identificacion,))
            patient_data = cursor.fetchone()
            cursor.close()
            conn.close()

            if patient_data:
                return Patient(*patient_data)
            else:
                return None
        except Exception as e:
            return str(e), 500
    
    @staticmethod
    def update_patient(patient):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuario_pat SET nombres = %s, apellidos = %s, fecha_nacimiento = %s, edad = %s, tipo_documento = %s, eapb = %s, regimen = %s WHERE num_identificacion = %s", (patient.nombres, patient.apellidos, patient.fecha_nacimiento, patient.edad, patient.tipo_documento, patient.eapb, patient.regimen, patient.num_identificacion))
            conn.commit()
            cursor.close()
            conn.close()
            return "Paciente actualizado correctamente"
        except Exception as e:
            return str(e), 500