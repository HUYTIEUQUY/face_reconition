import conect_firebase

db=conect_firebase.connect().database()




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
    data=db.child("SinhVien").get()
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop)):
                e=[str(stt),i.val()["MaSV"],i.val()["TenSV"]]
                a.append(e)
                stt=stt+1
    except: a=[]
    return a

def anh(masv):
    a=""
    data=db.child("SinhVien").get()
    for i in data.each():
        if(i.val()["MaSV"]==str(masv)):
            a=i.val()["Anh"]
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

# def suasv(masv,anh):
#     data=db.child("SinhVien").get()
#     dl={'Anh':str(anh)}
#     for i in data.each():
#         if(i.val()["MaSV"]==str(masv)):
#             try:
#                 db.child("SinhVien").child(i.key()).update(dl)
#                 return True
#             except:
#                 return False