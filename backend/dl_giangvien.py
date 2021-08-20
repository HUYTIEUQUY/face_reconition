import conect_firebase

db=conect_firebase.connect().database()


def tengv_email(email):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["Email"]==email):
            a=i.val()["TenGV"]
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


def tengv_ma(ma):
    data=db.child("GiangVien").get()
    a=""
    for i in data.each():
        if(i.val()["MaGV"]==str(ma)):
            a=(i.val()["TenGV"])
    return a
