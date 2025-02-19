from flask import Blueprint, jsonify, request
from src.models.Form_radiologoModel import FormRadiologoModel
from src.models.Form_cirujanoModel import FormCirujanoModel
from src.models.Form_patologoModel import FormPatologoModel
from src.utils.DateFormat import DateFormat
from datetime import datetime
import uuid

forms_bp = Blueprint('forms_bp', __name__)

@forms_bp.route('/forms-patient/<string:id>', methods=['GET'])
def get_forms_by_patient_id(id):
    try:
        forms_dict = {}
        formsRadiologo = FormRadiologoModel.get_by_patient_id(id)
        formsCirujano = FormCirujanoModel.get_by_patient_id(id)
        formsPatologo = FormPatologoModel.get_by_patient_id(id)
        
        # Convertir los objetos a diccionarios
        forms_dict = {
            "radiologoForms": [{"formularioRadiologo{}".format(i+1): form.__dict__} for i, form in enumerate(formsRadiologo)],
            "patologoForms": [{"formularioPatologo{}".format(i+1): form.__dict__} for i, form in enumerate(formsPatologo)],
            "cirujanoForms": [{"formularioCirujano{}".format(i+1): form.__dict__} for i, form in enumerate(formsCirujano)]
        }
        return jsonify(forms_dict)
    except Exception as e:
        print('ERROR: al consultar los formularios',e)
        return str(e), 500

@forms_bp.route('/addFormRadiologo', methods=['POST'])
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
    
