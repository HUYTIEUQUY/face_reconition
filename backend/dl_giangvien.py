import conect_firebase
import re
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

def magv_all():
    data=db.child("GiangVien").get()
    a=[]
    for i in data.each():
        magv= i.val()["MaGV"]
        if magv not in a:
            a.append(magv)
    return a

def tengv_email(email):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["Email"]==email):
            a=i.val()["TenGV"]
    return a


def sdt_email(email):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["Email"]==email):
            a=str(i.val()["SDT"])
    return a

def makhoa_email(email):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["Email"]==str(email)):
            ma=i.val()["MaKhoa"]
    return ma

def kt_ma(ma):
    data=db.child("GiangVien").get()
    a=[]
    for i in data.each():
        if(i.val()["MaGV"]==str(ma)):
            a.append(i.val())
    return a

def tao_tk(email,matkhau):
    auth=conect_firebase.connect().auth()
    try:
        auth.create_user_with_email_and_password(email, matkhau)
        return True
    except:
        return False

def themgv(magv,tengv,email,sdt,ghichu,makhoa):
    if tao_tk(email,"123456"):
        data={'MaGV':str(magv), 'TenGV':str(tengv),'Email':str(email),'SDT':str(sdt),'GhiChu':str(ghichu),'LoaiTK':"0","MaKhoa":str(makhoa)}
        try:
            db.child('GiangVien').push(data)
            return True
        except:
            return False
    else:
        return False

def banggv(makhoa):
    a=[]
    stt=1
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa) and i.val()["LoaiTK"]==str(0)):
            e=[str(stt),i.val()["MaGV"],i.val()["TenGV"],i.val()["Email"],i.val()["SDT"],i.val()["GhiChu"]]
            a.append(e)
            stt=stt+1
    return a

def tim_gv(makhoa,q):
    a=[]
    stt=1
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa) and i.val()["LoaiTK"]==str(0)):
            e=[str(stt),i.val()["MaGV"],i.val()["TenGV"],i.val()["Email"],i.val()["SDT"],i.val()["GhiChu"]]
            if str(q) in khong_dau(i.val()["MaGV"].lower()) or str(q) in khong_dau(i.val()["TenGV"].lower()) or str(q) in khong_dau(i.val()["Email"].lower()) or str(q) in khong_dau(i.val()["SDT"].lower()):
                a.append(e)
            stt=stt+1
    return a

def suagv(magv,tengv,sdt,ghichu):
    data=db.child("GiangVien").get()
    dl={'MaGV':str(magv),'TenGV':str(tengv),'SDT':str(sdt),'GhiChu':str(ghichu)}
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            try:
                db.child("GiangVien").child(i.key()).update(dl)
                return True
            except:
                return False

def xoa_tk(email):
    cred = credentials.Certificate("nckh.json")
    firebase_admin.initialize_app(cred)
    a=auth.get_user_by_email(str(email))
    auth.delete_user(a.uid)

def xoagv(magv):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            try:
                db.child("GiangVien").child(i.key()).remove()
                return True
            except:
                return False

def magv_ten(ten):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["TenGV"]==str(ten)):
            a=(i.val()["MaGV"])
    return a

def magv_email(email):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["Email"]==str(email)):
            a=(i.val()["MaGV"])
    return a

def tengv_ma(ma):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["MaGV"]==str(ma)):
            a=(i.val()["TenGV"])
    return a

def email_ma(ma):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["MaGV"]==str(ma)):
            a=(i.val()["Email"])
    return a

def sdt_ma(ma):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["MaGV"]==str(ma)):
            a=(i.val()["SDT"])
    return a


def update_sdt(magv,sdt):
    data=db.child("GiangVien").get()
    dl={'MaGV':str(magv),'SDT':str(sdt)}
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            try:
                db.child("GiangVien").child(i.key()).update(dl)
                return True
            except:
                return False

def kt_gv_tontai_tkb(magv):
    data=db.child("ThoiKhoaBieu").get()
    a=[]
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            a.append(i.val()["MaGV"])
    return a

def kt_gv_tontai_diemdanh(magv):
    data=db.child("DiemDanh").get()
    a=[]
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            a.append(i.val()["MaGV"])
    return a

