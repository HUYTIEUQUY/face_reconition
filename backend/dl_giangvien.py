import conect_firebase
import re
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from kt_nhap import khong_dau
import backend.dl_khoa 
db=conect_firebase.connect().database()



def magv_all():
    data=db.child("GiangVien").get()
    a=[]
    for i in data.each():
        magv= i.val()["MaGV"]
        if magv not in a:
            a.append(magv)
    return a

def tengv_email(email):
    a=""
    data=db.child("GiangVien").order_by_child("Email").equal_to(str(email)).get()
    for i in data.each():
        a=i.val()["TenGV"]
    return a


def sdt_email(email):
    data=db.child("GiangVien").order_by_child("Email").equal_to(str(email)).get()
    a=""
    for i in data.each():
        a=str(i.val()["SDT"])
    return a

def makhoa_email(email):
    ma=""
    data=db.child("GiangVien").order_by_child("Email").equal_to(str(email)).get()
    for i in data.each():
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
    if tao_tk(email,str(magv)):
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
    data=db.child("GiangVien").order_by_child("MaKhoa").equal_to(str(makhoa)).get()
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
    a=auth.get_user_by_email(str(email))
    auth.delete_user(a.uid)

def xoagv(magv):
    data=db.child("GiangVien").order_by_child("MaGV").equal_to(str(magv)).get()
    for i in data.each():
        if(i.val()["MaGV"]==str(magv)):
            try:
                db.child("GiangVien").child(i.key()).remove()
                return True
            except:
                return False

def magv_ten(ten):
    data=db.child("GiangVien").order_by_child("TenGV").equal_to(str(ten)).get()
    a = ""
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

def luughichu(magv,ghichu):
    try:
        data=db.child("GiangVien").order_by_child("MaGV").equal_to(str(magv)).get()
        dl={'GhiChu':str(ghichu)}
        for i in data.each():
            if(i.val()["MaGV"]==str(magv)):
                    db.child("GiangVien").child(i.key()).update(dl)
                    return True
    except:
        return False

def kt_gv_tontai_tkb(magv):
    data=db.child("ThoiKhoaBieu").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]==str(magv)):
                a.append(i.val()["MaGV"])
    except:a=[]
    return a

def kt_gv_tontai_diemdanh(magv):
    data=db.child("DiemDanh").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]==str(magv)):
                a.append(i.val()["MaGV"])
    except:a=[]
    return a



