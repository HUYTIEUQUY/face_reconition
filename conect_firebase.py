import pyrebase


def connect():
    firebaseConfig = {
        "apiKey": "AIzaSyC18JzwOtmxacPea2wH6V7epsMTCS1R7G0",
        "authDomain": "facerecognition-30da4.firebaseapp.com",
        "databaseURL": "https://facerecognition-30da4-default-rtdb.firebaseio.com",
        "projectId": "facerecognition-30da4",
        "storageBucket": "facerecognition-30da4.appspot.com",
        "messagingSenderId": "207559290047",
        "appId": "1:207559290047:web:577197cfe03736a9a86a0a",
        "measurementId": "G-LREFTPNQ1E"
        
        }
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase



