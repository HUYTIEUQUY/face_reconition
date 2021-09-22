import conect_firebase
import re

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

def lop_khoa(ma):
    data=db.child("Lop").get()
    a=[]
    for i in data.each():
        if(i.val()["MaKhoa"]==str(ma)):
            a.append(i.val()["TenLop"])
    return a

def kt_masv_tontai(ma):
    a=[]
    data=db.child("SinhVien").get()
    try:
        for i in data.each():
            if(i.val()["MaSV"]==str(ma)):
                a.append(i.val()["MaSV"])
    except: a=[]
    return a

def themsv(masv,tensv,malop,anh):
    data={'MaSV':str(masv),'TenSV':str(tensv),'MaLop':str(malop),'Anh':str(anh)}
    try:
        db.child('SinhVien').push(data)
        return True
    except:
        return False

def bangsv(malop):
    a=[]
    stt=1
    data=db.child("SinhVien").order_by_child("MaLop").equal_to(str(malop)).get()
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                e=[str(stt),i.val()["MaSV"],i.val()["TenSV"]]
                a.append(e)
                stt=stt+1
    except: a=[]
    return a


def ds_ma_sv(malop):
    a=[]
    data=db.child("SinhVien").get()
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                e=i.val()["MaSV"]
                a.append(e)
    except: a=[]
    return a

def anh(masv):
    a=""
    data=db.child("SinhVien").get()
    for i in data.each():
        if(i.val()["MaSV"]==str(masv)):
            a=str(i.val()["Anh"])
    return a

def xoasv(masv):
    data=db.child("SinhVien").get()
    for i in data.each():
        if(i.val()["MaSV"]==str(masv)):
            try:
                db.child("SinhVien").child(i.key()).remove()
                return True
            except:
                return False

def suasv(masv,tensv):
    data=db.child("SinhVien").get()
    dl={'TenSV':str(tensv)}
    for i in data.each():
        if(i.val()["MaSV"]==str(masv)):
            try:
                db.child("SinhVien").child(i.key()).update(dl)
                return True
            except:
                return False

def timsv(malop,q):
    a=[]
    stt=1
    data=db.child("SinhVien").get()
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                e=[str(stt),i.val()["MaSV"],i.val()["TenSV"]]

                if khong_dau(str(q).lower()) in khong_dau(i.val()["MaSV"].lower()) or khong_dau(str(q).lower()) in khong_dau(i.val()["TenSV"].lower()):
                    a.append(e)
                stt=stt+1
    except: a=[]
    return a

def tensv_ma(ma):
    data=db.child("SinhVien").get()
    a=""
    for i in data.each():
        if(i.val()["MaSV"]==str(ma)):
            a=(i.val()["TenSV"])
    return a


def dong_ma_sv(malop):

    data=db.child("SinhVien").get()
    e=[]
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                e.append(i.val()["MaSV"])
    except: e=[]
    return e

def dong_ten_sv(malop):
    
    data=db.child("SinhVien").get()
    e=[]
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                e.append(i.val()["TenSV"])
    except: e=[]
    return e

def ds_masv_lop(malop):
    data=db.child("SinhVien").get()
    a=[]
    for i in data.each():
        if(i.val()["MaLop"]==str(malop)):
            a.append(i.val()['MaSV'])
    return a