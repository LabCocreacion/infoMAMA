# infoMAMA

## Descripción
Sistema de información para la gestión de tamización de cáncer de mama, desarrollado como una API REST con Flask y PostgreSQL. El sistema permite gestionar pacientes, instituciones y formularios especializados para radiólogos, cirujanos y patólogos.

## Características Principales
- **Gestión de Pacientes**: Registro y consulta de pacientes con datos demográficos
- **Gestión de Instituciones**: Administración de centros médicos y sus especialistas
- **Formularios Especializados**: 
  - Formularios de radiología (mamografías, ecografías)
  - Formularios de cirugía mamaria
  - Formularios de patología
- **API REST**: Endpoints completos para todas las operaciones CRUD
- **Base de Datos PostgreSQL**: Persistencia de datos robusta y escalable

## Tecnologías Utilizadas

### Backend
- **Python 3.12+**
- **Flask 3.0.0** - Framework web
- **Flask-CORS 4.0.0** - Manejo de políticas CORS
- **PostgreSQL** - Base de datos principal
- **psycopg2 2.9.9** - Conector PostgreSQL
- **python-decouple 3.8** - Gestión de variables de entorno

### Dependencias Adicionales
- **SQLAlchemy 2.0.38** - ORM (opcional)
- **gunicorn 23.0.0** - Servidor WSGI para producción
- **google-cloud-pubsub 2.26.1** - Integración con Google Cloud
- **requests 2.31.0** - Cliente HTTP

## Estructura del Proyecto

```
infoMAMA/
├── app.py                          # Aplicación principal Flask
├── config.py                       # Configuración de la aplicación
├── requirements.txt                # Dependencias del proyecto
├── dump-sisMama-202508072014.sql  # Base de datos de respaldo
├── README.md                       # Documentación del proyecto
└── src/                           # Código fuente principal
    ├── __init__.py
    ├── database/                   # Módulo de conexión a BD
    │   ├── __init__.py
    │   └── db.py                  # Configuración PostgreSQL
    ├── entities/                   # Entidades de dominio
    │   ├── __init__.py
    │   ├── Form_cirujano_mama.py  # Entidad formulario cirujano
    │   ├── Form_patologo.py       # Entidad formulario patólogo
    │   ├── Form_radiologo.py      # Entidad formulario radiólogo
    │   ├── Instituto.py           # Entidad institución médica
    │   └── Patient.py             # Entidad paciente
    ├── models/                     # Modelos de acceso a datos
    │   ├── __init__.py
    │   ├── Form_cirujanoModel.py  # Modelo formulario cirujano
    │   ├── Form_patologoModel.py  # Modelo formulario patólogo
    │   ├── Form_radiologoModel.py # Modelo formulario radiólogo
    │   ├── InstitutoModel.py      # Modelo institución
    │   └── PatientModel.py        # Modelo paciente
    ├── routes/                     # Controladores REST
    │   ├── __init__.py
    │   ├── forms_routes.py        # Endpoints formularios
    │   ├── instituto_routes.py    # Endpoints instituciones
    │   └── patient_routes.py      # Endpoints pacientes
    ├── services/                   # Servicios de negocio
    │   └── __init__.py
    ├── tests/                      # Pruebas unitarias
    │   └── __init__.py
    └── utils/                      # Utilidades
        └── DateFormat.py          # Formateo de fechas
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.12 o superior
- PostgreSQL 12+ instalado y configurado
- Git

### 1. Clonar el Repositorio
```bash
git clone https://github.com/LabCocreacion/infoMAMA.git
cd infoMAMA
```

### 2. Crear Entorno Virtual
```bash
# Windows
py -m virtualenv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración de Variables de Entorno
Crear un archivo `.env` en la raíz del proyecto:

```env
# Base de datos PostgreSQL
PGSQL_HOST=localhost
PGSQL_USER=tu_usuario
PGSQL_PASSWORD=tu_password
PGSQL_DATABASE=sisMAMA

# Configuración Flask
SECRET_KEY=tu_clave_secreta_aqui
FLASK_ENV=development
```

### 5. Configurar Base de Datos
```bash
# Restaurar base de datos desde dump
psql -U tu_usuario -d sisMAMA -f dump-sisMama-202508072014.sql
```

### 6. Ejecutar la Aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5001`

## API Endpoints

### Base URL
```
http://localhost:5001/api/tamizacion-mama
```

### Instituciones
- **GET** `/instituciones` - Listar todas las instituciones
- **POST** `/addInstitucion` - Crear nueva institución
- **GET** `/instituciones/<id>` - Obtener institución por ID

### Pacientes
- **GET** `/patients/list-patients` - Listar todos los pacientes
- **POST** `/patients/add-patient` - Registrar nuevo paciente

### Formularios
- **GET** `/forms/forms-patient/<patient_id>` - Obtener formularios por paciente
- **POST** `/forms/addFormRadiologo` - Crear formulario de radiología
- **GET** `/forms/radiologo/<id>` - Obtener formulario de radiología específico

### Estructura de Respuesta - Formularios por Paciente
```json
{
  "radiologoForms": [
    {
      "formularioRadiologo1": { 
        "id_formulario_radiologo": "uuid",
        "id_paciente": "string",
        "fecha_toma_examen": "date",
        "tipo_examen": "string",
        "resultado_mamog_tamizacion": "string",
        // ... otros campos
      }
    }
  ],
  "patologoForms": [...],
  "cirujanoForms": [...]
}
```

## Modelo de Datos

### Entidades Principales

#### Paciente
```python
{
  "id_paciente": "UUID",
  "nombres": "string",
  "apellidos": "string", 
  "fecha_nacimiento": "date",
  "edad": "integer",
  "tipo_documento": "string",
  "num_identificacion": "string",
  "eapb": "string",
  "regimen": "string"
}
```

#### Institución
```python
{
  "id": "integer",
  "nombre": "string",
  "nombre_ips": "string",
  "codigo_ips": "string",
  "direccion": "string",
  "tipo_servicio": "string",
  "caracter_juridico": "string",
  "telefono_gerencia": "string",
  "telefono_enlace_tecnico": "string",
  "zona": "string",
  "fecha_creacion": "datetime",
  "creation_user": "string",
  "latitud": "decimal",
  "longitud": "decimal"
}
```

#### Formulario Radiólogo
```python
{
  "id_formulario_radiologo": "UUID",
  "id_paciente": "string",
  "id_especialista": "string",
  "fecha_toma_examen": "date",
  "institucion_prestadora": "string",
  "tipo_examen": "string",
  "resultado_mamog_tamizacion": "string",
  "resultado_mamog_diagnostica": "string",
  "resultado_mamog_mamaria": "string",
  "conducta_sugerida": "string",
  "ciudad": "string",
  "departamento": "string",
  "zona": "string"
}
```

## Configuración de Desarrollo

### Estructura de Paquetes
- **entities/**: Clases de dominio (POJO)
- **models/**: Acceso a datos y lógica de persistencia
- **routes/**: Controladores REST y manejo de peticiones HTTP
- **services/**: Lógica de negocio (futuras implementaciones)
- **utils/**: Utilidades y helpers

### Patrones Implementados
- **Repository Pattern**: En los modelos para acceso a datos
- **Blueprint Pattern**: Para organización de rutas en Flask
- **DTO Pattern**: Entidades como objetos de transferencia
- **Configuration Pattern**: Centralización de configuraciones

## Despliegue en Producción

### Usando Gunicorn
```bash
gunicorn --bind 0.0.0.0:5001 --workers 4 app:app
```

### Variables de Entorno Producción
```env
FLASK_ENV=production
PGSQL_HOST=tu_servidor_bd
PGSQL_PORT=5432
# ... otras configuraciones
```

## Testing

### Ejecutar Pruebas
```bash
# Instalar dependencias de testing
pip install pytest pytest-flask

# Ejecutar pruebas
pytest src/tests/
```

## Contribución

1. Fork del proyecto
2. Crear branch para feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push al branch (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Soporte

Para reportar bugs o solicitar nuevas funcionalidades, crear un issue en:
https://github.com/LabCocreacion/infoMAMA/issues

## Contacto

**Laboratorio de Cocreación**
- Repositorio: https://github.com/LabCocreacion/infoMAMA
- Documentación: [Enlace a docs]

---
*Última actualización: Agosto 2025*