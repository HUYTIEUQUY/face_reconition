from datetime import date
import conect_firebase

db=conect_firebase.connect().database()


def tenkhoa(makhoa):
    data=db.child("Khoa").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            ten=i.val()["TenKhoa"]
    return ten

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
    a = str(len(list(data.each()))+1)
    return a

def themkhoa(makhoa, tenkhoa):
    data={'MaKhoa':str(makhoa),'TenKhoa':tenkhoa}
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
            if str(q) in khong_dau(i.val()["Khoa"].lower()) or str(q) in khong_dau(i.val()["TenKhoa"].lower()):
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

def them_tk_khoa(tengv,email,makhoa,sdt,ghichu):
    if tao_tk(email,"123456"):
        data={'MaGV':str(makhoa), 'TenGV':str(tengv),'Email':str(email),'SDT':str(sdt),'GhiChu':str(ghichu),'LoaiTK':"1","MaKhoa":str(makhoa)}
        try:
            db.child('GiangVien').push(data)
            return True
        except:
            return False
    else:
        return False
