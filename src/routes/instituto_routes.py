from flask import Blueprint, jsonify, request
from src.models.InstitutoModel import InstitutoModel
from src.utils.DateFormat import DateFormat
from datetime import datetime
import uuid


instituto_bp = Blueprint('instituto_bp', __name__)

@instituto_bp.route('/instituciones', methods=['GET'])
def get_instituciones():
    try:
        instituciones = InstitutoModel.get_all()
        instituciones_dict = [instituto.__dict__ for instituto in instituciones]
        return jsonify(instituciones_dict)
    except Exception as e:
        return str(e), 500

@instituto_bp.route('/addInstitucion', methods=['POST'])
def add_institucion():
    try:
        data = request.get_json()
        new_institucion = InstitutoModel(
            id=str(uuid.uuid4()),
            nombre=data['nombre'],
            nombre_ips=data['nombre_ips'],
            codigo_ips=data['codigo_ips'],
            direccion=data['direccion'],
            tipo_servicio=data['tipo_servicio'],
            caracter_juridico=data['caracter_juridico'],
            telefono_gerencia=data['telefono_gerencia'],
            telefono_enlace_tecnico=data['telefono_enlace_tecnico'],
            zona=data['zona'],
            fecha_creacion= DateFormat.convert_date(datetime.now()),
            creation_user=data['creation_user'],
            latitud=data['latitud'],
            longitud=data['longitud']
        )
        result = InstitutoModel.add(new_institucion)
        return jsonify(result), 201
    except Exception as e:
        return str(e), 500

@instituto_bp.route('/detalle-institucion/<string:name>', methods=['GET'])
# TO-DO: Cambiar en la base de datos en vez del nombre el id de la institutcion
def get_institucionbyName(name):
    try:
        institucion = InstitutoModel.get_by_name(name)
        if institucion:
            return jsonify(institucion.__dict__)
        else:
            return "Institución no encontrada", 404
    except Exception as e:
        return str(e), 500