from flask import Blueprint, jsonify, request
from src.models.form_radiologoModel import FormRadiologoModel
from src.utils.DateFormat import DateFormat
from datetime import datetime
import uuid

forms_bp = Blueprint('forms_bp', __name__)

@forms_bp.route('/forms-patient/<int:id>', methods=['GET'])
def get_forms_by_patient_id(id):
    try:
        # TODO: Implement the logic to get all forms of a patient by its id
        forms = FormRadiologoModel.get_by_patient_id(id)
        forms_dict = [form.__dict__ for form in forms]
        return jsonify(forms_dict)
    except Exception as e:
        return str(e), 500

@forms_bp.route('/addForm', methods=['POST'])
def add_form():
    try:
        data = request.get_json()
        new_form = FormRadiologoModel(
            id=str(uuid.uuid4()),
            id_paciente=data['id_paciente'],
            id_especialista=data['id_especialista'],
            fecha_toma_examen= DateFormat.convert_date(datetime.now()),
            institucion_prestadora=data['institucion_prestadora'],
            tipo_examen=data['tipo_examen'],
            resultado_mamog_tamizacion=data['resultado_mamog_tamizacion'],
            resultado_mamog_diagnostica=data['resultado_mamog_diagnostica'],
            resultado_mamog_mamaria=data['resultado_mamog_mamaria'],
            conducta_sugerida=data['conducta_sugerida']
        )
        result = FormRadiologoModel.add(new_form)
        return jsonify(result), 201
    except Exception as e:
        return str(e), 500

@forms_bp.route('/forms/radiologo/<int:id>', methods=['GET'])
def get_formRadiologo(id):
    try:
        form = FormRadiologoModel.get_by_id(id)
        if form:
            return jsonify(form.__dict__)
        else:
            return "Formulario no encontrado", 404
    except Exception as e:
        return str(e), 500
    
