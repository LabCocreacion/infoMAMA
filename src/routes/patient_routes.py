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