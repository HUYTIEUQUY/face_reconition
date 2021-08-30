import pyrebase


def connect():
    firebaseConfig = {
        'apiKey': "AIzaSyC929pJEID3mptbtseoPLf6fx1Pl7RlArA",
        'authDomain': "face-recognition-e78ae.firebaseapp.com",
        'databaseURL': "https://face-recognition-e78ae-default-rtdb.firebaseio.com",
        'projectId': "face-recognition-e78ae",
        'storageBucket': "face-recognition-e78ae.appspot.com",
        'messagingSenderId': "53435624247",
        'appId': "1:53435624247:web:71955d0d0935fdac2708b2",
        'measurementId': "G-E7RJ8ZTK5G"
        }
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase



