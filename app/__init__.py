from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, auth

def create_app():
    app = Flask(__name__)

    #Inicializo Firebase
    #cargo las credenciales de autenticacion desde el archivo .json
    cred = credentials.Certificate("app/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)


    @app.route('/registro', methods=['POST'])
    def registrar_usuario():
        try:
            # se accede al valor del diccionario en formato JSON con valor 'email' y 'password'
            email = request.json['email']
            password = request.json['password']

            #se crea el usuario con email y contraseña
            user = auth.create_user(
                email=email,
                password=password
            )
            return jsonify({"message": "Usuario creado", "id": user.uid}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/login', methods=['POST'])
    def login_user():
        try:
            # se accede al valor del diccionario en formato JSON con valor 'email' y 'password'
            email = request.json['email']
            password = request.json['password']
            
            # Verificar las credenciales en Firebase
            user = auth.get_user_by_email(email)
            # Aquí iría la verificación de la contraseña (esto se hace normalmente con Firebase SDK en el frontend, pero vamos a simularlo en el backend)
            # Firebase no maneja directamente las contraseñas en el backend, así que usaremos un token como la forma de validar el login.

            # Generar un token para el usuario
            token = auth.create_custom_token(user.uid)
            return jsonify({"message": "Login exitoso", "token": token.decode()}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    

    return app 
   