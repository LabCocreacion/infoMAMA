from ..database.db import get_connection
from ..entities.Instituto import Instituto

class InstitutoModel:

    def __init__(self, id, nombre, nombre_ips, codigo_ips, direccion, tipo_servicio, caracter_juridico, telefono_gerencia, telefono_enlace_tecnico, zona, fecha_creacion, creation_user, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.nombre_ips = nombre_ips
        self.codigo_ips = codigo_ips
        self.direccion = direccion
        self.tipo_servicio = tipo_servicio
        self.caracter_juridico = caracter_juridico
        self.telefono_gerencia = telefono_gerencia
        self.telefono_enlace_tecnico = telefono_enlace_tecnico
        self.zona = zona
        self.fecha_creacion = fecha_creacion
        self.creation_user = creation_user
        self.latitud = latitud
        self.longitud = longitud

    @staticmethod
    def get_all():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM institucion")
            instituciones_data = cursor.fetchall()
            cursor.close()
            conn.close()

            # Convertir los datos en una lista de objetos Instituto
            instituciones = [Instituto(*data) for data in instituciones_data]
            return instituciones
        except Exception as e:
            return str(e), 500
    
    @staticmethod
    def add(institucion):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO institucion (id, nombre, nombre_ips, codigo_ips, direccion, tipo_servicio, caracter_juridico, telefono_gerencia, telefono_enlace_tecnico, zona, fecha_creacion, creation_user, latitud, longitud)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, (institucion.id, institucion.nombre, institucion.nombre_ips, institucion.codigo_ips, institucion.direccion, institucion.tipo_servicio, institucion.caracter_juridico, institucion.telefono_gerencia, institucion.telefono_enlace_tecnico, institucion.zona, institucion.fecha_creacion, institucion.creation_user, institucion.latitud, institucion.longitud))
            institucion.id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return institucion.__dict__
        except Exception as e:
            return str(e), 500

    @staticmethod
    def get_by_id(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM institucion WHERE id = %s", (id,))
            data = cursor.fetchone()
            cursor.close()
            conn.close()
            if data:
                return Instituto(*data)
            return None
        except Exception as e:
            return str(e), 500
    
    @staticmethod
    def get_by_name(name):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM institucion WHERE nombre = %s", (name,))
            data = cursor.fetchone()
            cursor.close()
            conn.close()
            if data:
                return Instituto(*data)
            return None
        except Exception as e:
            return str(e), 500