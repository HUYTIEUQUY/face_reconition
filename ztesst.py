import pyrebase
import re


# def giangvienjson(ma,ten,email,sdt,ghichu,loaitk):
#     data={'MaGV':ma, 'TenGV':ten,'Email':email,'SDT':sdt,'GhiChu':ghichu,'LoaiTK':loaitk}
#     return data
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



db=connect().database()
<<<<<<< HEAD
data=db.child("Khoa").get()
for i in data.each():
    if(i.val()["MaKhoa"]==str(1)):
        a=i.val()["TenKhoa"]
print(a)
=======
data=db.child("CaHoc").get()
for i in data.each():
    if(i.val()["TenCa"]==str(1)):
        a=i.val()
print(a) 

print(str(a['TGBD']))
>>>>>>> af47e32b4d94aaa6d686578dcbc70d1bf205883f

