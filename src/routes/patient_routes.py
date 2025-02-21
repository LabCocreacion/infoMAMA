from flask import Blueprint, jsonify, request
from src.models.PatientModel import PatientModel
from src.utils.DateFormat import DateFormat
from datetime import datetime
import uuid

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/list-patients', methods=['GET'])
def get_patients():
    try:
        patients = PatientModel.get_all()
        patients_dict = [patient.__dict__ for patient in patients]
        return jsonify(patients_dict)
    except Exception as e:
        return str(e), 500

@patient_bp.route('/add-patient', methods=['POST'])
def add_patient():
    try:
        data = request.get_json()
        # Convertir la fecha de nacimiento a un objeto datetime.date
        fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        new_patient = PatientModel(
            id_paciente=str(uuid.uuid4()),
            nombres=data['nombres'],
            apellidos=data['apellidos'],
            fecha_nacimiento=fecha_nacimiento,
            edad=data['edad'],
            tipo_documento=data['tipo_documento'],
            num_identificacion=data['num_identificacion'],
            eapb=data['eapb'],
            regimen=data['regimen']
        )
        result = PatientModel.add(new_patient)
        return jsonify(result), 201
    except Exception as e:
        print('ERROR: al insertar el paciente',e)
        return str(e), 500

@patient_bp.route('/patient/<string:num_identificacion>', methods=['GET'])
def get_patient(num_identificacion):
    try:
        patient = PatientModel.get_by_id(num_identificacion)
        if patient:
            return jsonify(patient.__dict__)
    except Exception as e:
        return str(e), 500


@patient_bp.route('/update-patient', methods=['PUT'])
def update_patient():
    try:
        data = request.get_json()
        # Convertir la fecha de nacimiento a un objeto datetime.date
        fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        patient = PatientModel(
            id_paciente=data['id_paciente'],
            nombres=data['nombres'],
            apellidos=data['apellidos'],
            fecha_nacimiento=fecha_nacimiento,
            edad=data['edad'],
            tipo_documento=data['tipo_documento'],
            num_identificacion=data['num_identificacion'],
            eapb=data['eapb'],
            regimen=data['regimen']
        )
        result = PatientModel.update_patient(patient)
        return jsonify(result), 200
    except Exception as e:
        print('ERROR: al actualizar el paciente',e)
        return str(e), 500