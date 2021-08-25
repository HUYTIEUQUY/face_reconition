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

def khong_dau(s):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        return s

db=connect().database()
a=[]
stt=1
data=db.child("SinhVien").get()
try:
    for i in data.each():
        if(i.val()["MaLop"]== str(103409)):
            e=[str(stt),i.val()["MaSV"],i.val()["TenSV"]]

            if "333" in khong_dau(i.val()["MaSV"].lower()) or "333" in khong_dau(i.val()["TenSV"].lower()):
                a.append(e)
            stt=stt+1
except: a=[]
print(a)


