import pyrebase


def connect():
    firebaseConfig = {
        'apiKey': "AIzaSyB6UhHmYJRkA4r6HCZwqVEW40kSQ3WhvqY",
        'authDomain': "nckh-d5994.firebaseapp.com",
        'databaseURL': "https://nckh-d5994-default-rtdb.firebaseio.com/",
        'projectId': "nckh-d5994",
        'storageBucket': "nckh-d5994.appspot.com",
        'messagingSenderId': "1057994457660",
        'appId': "1:1057994457660:web:e32f6f0652a09fa7c57939",
        'measurementId': "G-217NY3WN04"
        }
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase



