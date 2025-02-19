# filepath: /c:/INC/infoMAMA/app.py
from flask import Flask, Response
from flask_cors import CORS
from src.routes.instituto_routes import instituto_bp
from src.routes.forms_routes import forms_bp
from src.routes.patient_routes import patient_bp

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)

@app.route('/api/tamizacion-mama', methods=['OPTIONS'])
def options():
    return Response({'Allow': 'GET, POST'}, status=200, mimetype='application/json; charset=utf-8')

if __name__ == '__main__':
    app.register_blueprint(instituto_bp, url_prefix='/api/tamizacion-mama')
    app.register_blueprint(forms_bp, url_prefix='/api/tamizacion-mama/forms')
    app.register_blueprint(patient_bp, url_prefix='/api/tamizacion-mama/patients')

    app.run(debug=True, port=5001)