import pyrebase

config = {
    'apiKey': "AIzaSyDNXL9Mie17vJn1Ku358ywiHTQd61BpbeQ",
    'authDomain': "authpyflask.firebaseapp.com",
    'projectId': "authpyflask",
    'storageBucket': "authpyflask.firebasestorage.app",
    'messagingSenderId': "117906449121",
    'appId': "1:117906449121:web:fbaa489221858b8d184da0",
    'measurementId': "G-7XQYWHN05J",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'mauriciourroz10@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)

user = auth.sign_in_with_email_and_password(email, password)

info = auth.get_account_info(user['idToken'])
print(info)