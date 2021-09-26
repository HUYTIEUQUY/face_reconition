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

def banglop(makhoa):
    a=[]
    stt=1
    data=db.child("Lop").get()
    try:
        for i in data.each():
            if(i.val()["MaKhoa"]==str(makhoa)):
                e=[str(stt),i.val()["MaLop"],i.val()["TenLop"]]
                a.append(e)
                stt=stt+1
    except:a=[]
    return a

def themlop(malop,tenlop,makhoa):
    data={'MaLop':str(malop),'TenLop':tenlop,'MaKhoa':str(makhoa)}
    try:
        db.child('Lop').push(data)
        return True
    except:
        return False

def sualop(malop,tenlop):
    data=db.child("Lop").get()
    dl={'TenLop':tenlop}
    for i in data.each():
        if(i.val()["MaLop"]==str(malop)):
            try:
                db.child("Lop").child(i.key()).update(dl)
                return True
            except:
                return False

def xoalop(malop):
    data=db.child("Lop").get()
    for i in data.each():
        if(i.val()["MaLop"]==str(malop)):
            try:
                db.child("Lop").child(i.key()).remove()
                return True
            except:
                return False


def kt_tenlop(tenlop):
    a=[]
    try:
        data=db.child("Lop").get()
        for i in data.each():
            if(i.val()["TenLop"]==str(tenlop)):
                a.append(i.val())
    except: a=[]
    return a


def malop_ten(tenlop):
    data=db.child("Lop").get()
    a=""
    for i in data.each():
        if(i.val()["TenLop"]==str(tenlop)):
            a=(i.val()["MaLop"])
    return a

def tenlop_ma(ma):
    data=db.child("Lop").order_by_child("MaLop").equal_to(str(ma)).get()
    a=""
    for i in data.each():
        if(i.val()["MaLop"]==str(ma)):
            a=(i.val()["TenLop"])
    return a
def malop_masv(ma):
    data=db.child("SinhVien").order_by_child("MaSV").equal_to(str(ma)).get()
    a=""
    for i in data.each():
        if(i.val()["MaSV"]==str(ma)):
            a=(i.val()["MaLop"])
    return a

def timlop(makhoa,q):
    a=[]
    stt=1
    data=db.child("Lop").get()
    try:
        for i in data.each():
            if(i.val()["MaKhoa"]==str(makhoa)):
                e=[str(stt),i.val()["MaLop"],i.val()["TenLop"]]
                if str(q) in khong_dau(i.val()["MaLop"].lower()) or str(q) in khong_dau(i.val()["TenLop"].lower()):
                    a.append(e)
                stt=stt+1
    except:a=[]
    return a


def kt_lop_tontai_diemdanh(malop):
    
    a=[]
    try:
        data=db.child("DiemDanh").order_by_child('MaLop').equal_to('str(malop)').get()
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                a.append(i.val()['MaLop'])
    except:a=[]
    return a

def kt_lop_tontai_tkb(malop):
    
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child('MaLop').equal_to('str(malop)').get()
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                a.append(i.val()['MaLop'])
    except:a=[]
    return a

def malop():
    a="1"
    data = db.child("Lop").get()
    try:
        for i in data.each():
            e=[i.val()["MaLop"]]
            a=str(int(max(e))+1)
    except:a="1"
    return a








