from flask import Blueprint, jsonify, request
from src.models.InstitutoModel import InstitutoModel
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

@instituto_bp.route('/instituciones', methods=['POST'])
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
            fecha_creacion=data['fecha_creacion']
        )
        result = InstitutoModel.add(new_institucion)
        return jsonify(result), 201
    except Exception as e:
        return str(e), 500

@instituto_bp.route('/instituciones/<int:id>', methods=['GET'])
def get_institucion(id):
    try:
        institucion = InstitutoModel.get_by_id(id)
        if institucion:
            return jsonify(institucion.__dict__)
        else:
            return "Institución no encontrada", 404
    except Exception as e:
        return str(e), 500