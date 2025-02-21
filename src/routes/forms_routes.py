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
            id_formulario_radiologo=str(uuid.uuid4()),
            id_paciente=data['numIdentificacionPaciente'],
            id_especialista=data['id_especialista'],
            fecha_toma_examen= DateFormat.convert_date(datetime.now()),
            institucion_prestadora=data['institucionPrestadora'],
            tipo_examen=data['tipoExamen'],
            resultado_mamog_tamizacion=data['resultadoTamizacion'],
            resultado_mamog_diagnostica=data['resultadoDiagnostica'],
            resultado_mamog_mamaria=data['resultadoEcografia'],
            conducta_sugerida=data['conductaSugerida'],
            ciudad=data['ciudad'],
            departamento=data['departamento'],
            zona=data['zona']
        )
        result = FormRadiologoModel.add(new_form)
        return jsonify(result), 201
    except Exception as e:
        print('ERROR: al agregar el formulario',e)
        return str(e), 500

@forms_bp.route('/radiologo-form/<string:id>', methods=['GET'])
def get_formRadiologo(id):
    try:
        print('id', id)
        form = FormRadiologoModel.get_by_id(id)
        if form:
            return jsonify(form.__dict__)
        else:
            return "Formulario no encontrado", 404
    except Exception as e:
        return str(e), 500
    
