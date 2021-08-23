import conect_firebase
from backend.dl_giangvien import tengv_ma
from backend.dl_monhoc import tenmh_ma

db=conect_firebase.connect().database()


def lop_khoa(ma):
    data=db.child("Lop").get()
    a=[]
    for i in data.each():
        if(i.val()["MaKhoa"]==str(ma)):
            a.append(i.val()["TenLop"])
    return a

def gv_khoa(ma):
    data=db.child("GiangVien").get()
    a=[]
    for i in data.each():
        if(i.val()["MaKhoa"]==str(ma) and i.val()["LoaiTK"]=="0"):
            a.append(i.val()["TenGV"])
    return a

def mh_khoa(ma):
    data=db.child("MonHoc").get()
    a=[]
    for i in data.each():
        if(i.val()["MaKhoa"]==str(ma)):
            a.append(i.val()["TenMH"])
    return a

def manh_ten(ten):
    data=db.child("NamHoc").get()
    a=""
    for i in data.each():
        if(i.val()["TenNH"]==str(ten)):
            a=(i.val()["MaNH"])
    return a


def them_tkb(magv,mamh,loai,ngay,ca,malop,hki,nam):
    matkb=str(ngay).replace("/","")+str(ca)+str(malop)
    data={'MaTKB':str(matkb),'MaGV':str(magv),'MaMH':str(mamh),'PP_Giang':str(loai),'Ngay':str(ngay),'Ca':str(ca),'MaLop':str(malop),'HocKy':str(hki),'namHoc':str(nam),'TrangThaiDD':"0"}
    try:
        db.child('ThoiKhoaBieu').push(data)
        return True
    except:
        return False

def them_tkb(magv,mamh,loai,ngay,ca,malop,hki,nam):
    matkb=str(ngay).replace("/","")+str(ca)+str(malop)
    data={'MaTKB':str(matkb),'MaGV':str(magv),'MaMH':str(mamh),'PP_Giang':str(loai),'Ngay':str(ngay),'Ca':str(ca),'MaLop':str(malop),'HocKy':str(hki),'NamHoc':str(nam),'TrangThaiDD':"0"}
    try:
        db.child('ThoiKhoaBieu').push(data)
        return True
    except:
        return False



def bang_tkb(malop,namhoc,hocky):
    a=[]

    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop) and i.val()["NamHoc"]==str(namhoc) and i.val()["HocKy"]==str(hocky)):
                gv=tengv_ma(i.val()["MaGV"])
                mh=tenmh_ma(i.val()["MaMH"])
                e=[gv,mh,i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"]]
                a.append(e)
 
    except:a=[]
    return a


def kt_lichgiang(magv,ngay,ca):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and i.val()["Ca"]==str(ca) and i.val()["MaGV"]==str(magv)):
                a.append(i.val()["MaGV"])
    except: a=[]
    return a

def kt_lich_tkb(malop,ngay,ca):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and i.val()["Ca"]==str(ca) and i.val()["MaLop"]==str(malop)):
                a.append(i.val()["MaLop"])
    except:a=[]
    return a


def xoa_dong_tkb(magv,mamh,ngay,ca):
    data=db.child("ThoiKhoaBieu").get()
    for i in data.each():
        if(i.val()["MaGV"]==str(magv), i.val()["MaMH"]==str(mamh), i.val()["Ngay"]==str(ngay), i.val()["Ca"]==str(ca)):
            try:
                db.child("ThoiKhoaBieu").child(i.key()).remove()
                return True
            except:
                return False


def tenlop_ma(ma):
    data=db.child("Lop").get()
    a=""
    for i in data.each():
        if(i.val()["MaLop"]==str(ma)):
            a=(i.val()["TenLop"])
    return a



def kt_lichgiang_gv(magv,ngay):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and i.val()["MaGV"]==str(magv)):
                tenl=tenlop_ma(i.val()['MaLop'])
                tenm=tenmh_ma(i.val()['MaMH'])
                e = [tenl,tenm,i.val()['Ca']]
                a.append(e)
    except: a=[]
    return a


def gv_dd(magv,ngay):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["MaGV"]==str(magv) and i.val()["Ngay"] < str(ngay) and i.val()["TrangThaiDD"] =='0' ):
                tenl=tenlop_ma(i.val()['MaLop'])
                tenm=tenmh_ma(i.val()['MaMH'])
                e = [tenl,tenm,i.val()['Ngay'],i.val()['Ca']]
                a.append(e)
    except: a=[]
    return a