from datetime import date
import re
import conect_firebase
from firebase_admin import auth
from firebase_admin import credentials
import firebase_admin



db=conect_firebase.connect().database()

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
def tenkhoa(makhoa):
    data=db.child("Khoa").get()
    a=''
    try:
        for i in data.each():
            if(i.val()["MaKhoa"]==str(makhoa)):
                a=i.val()["TenKhoa"]
    except:a=''
    return a

def bangkhoa():
    a=[]
    stt=1
    data=db.child("Khoa").get()
    try:
        for i in data.each():
            e=[str(stt),i.val()["MaKhoa"],i.val()["TenKhoa"]]
            a.append(e)
            stt=stt+1
    except:a=[]
    return a

def sl_khoa():
    a=""
    data = db.child("Khoa").get()
    try:
        for i in data.each():
            e=[i.val()["MaKhoa"]]
            a=str(int(max(e))+1)
    except:a=""
    return a

def themkhoa(makhoa, tenkhoa):
    data={'MaKhoa':str(makhoa),'TenKhoa':str(tenkhoa)}
    try:
        db.child('Khoa').push(data)
        return True
    except:
        return False

def suakhoa(makhoa,tenkhoa):
    data=db.child("Khoa").get()
    dl={'TenKhoa':tenkhoa}
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            try:
                db.child("Khoa").child(i.key()).update(dl)
                return True
            except:
                return False
def xoakhoa(makhoa):
    data=db.child("Khoa").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            try:
                db.child("Khoa").child(i.key()).remove()
                return True
            except:
                return False

def xoakhoa_bgv(magv):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            try:
                db.child("GiangVien").child(i.key()).remove()
                return True
            except:
                return False
def xoa_tk(email):
    cred = credentials.Certificate("nckh.json")
    firebase_admin.initialize_app(cred)
    a=auth.get_user_by_email(str(email))
    auth.delete_user(a.uid)

def kt_tenkhoa(tenkhoa):
    data=db.child("Khoa").get()
    a=[]
    for i in data.each():
        if(i.val()["TenKhoa"]==str(tenkhoa)):
            a.append(i.val())
    return a

def makhoa_ten(tenkhoa):
    data=db.child("Khoa").get()
    a=""
    for i in data.each():
        if(i.val()["TenKhoa"]==str(tenkhoa)):
            a=(i.val()["MaKhoa"])
    return a

def tenkhoa_ma(ma):
    data=db.child("Khoa").get()
    a=""
    for i in data.each():
        if(i.val()["MaKhoa"]==str(ma)):
            a=(i.val()["TenKhoa"])
    return a

def timkhoa(q):
    a=[]
    stt=1
    data=db.child("Khoa").get()
    try:
        for i in data.each():
            e=[str(stt),i.val()["MaKhoa"],i.val()["TenKhoa"]]
            if str(q) in khong_dau(i.val()["MaKhoa"].lower()) or str(khong_dau(q)) in khong_dau(i.val()["TenKhoa"].lower()):
                a.append(e)
            stt=stt+1
    except:a=[]
    return a

def tao_tk(email,matkhau):
    auth=conect_firebase.connect().auth()
    try:
        auth.create_user_with_email_and_password(email, matkhau)
        return True
    except:
        return False

def them_tk_khoa(tengv,email,makhoa):
    if tao_tk(email,"123456"):
        data={'MaGV':str(makhoa), 'TenGV':str(tengv),'Email':str(email),'LoaiTK':"1","MaKhoa":str(makhoa),'GhiChu':"",'SDT':""}
        try:
            db.child('GiangVien').push(data)
            return True
        except:
            return False
    else:
        return False


def kt_lop_in_khoa(makhoa):
    a=[]
    data=db.child("Lop").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            a.append(i.val()["MaKhoa"])
    if a != []:
        return True
    else:
        return False