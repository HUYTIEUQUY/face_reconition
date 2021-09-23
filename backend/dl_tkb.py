import conect_firebase
from backend.dl_giangvien import tengv_ma
from backend.dl_monhoc import tenmh_ma
import re
from kt_nhap import khong_dau
import datetime
db=conect_firebase.connect().database()


def lop_khoa(ma):
    data=db.child("Lop").order_by_child("MaKhoa").equal_to(str(ma)).get()
    a=[]
    for i in data.each():
            a.append(i.val()["TenLop"])
    return a

def gv_khoa(ma):
    data=db.child("GiangVien").order_by_child("MaKhoa").equal_to(str(ma)).get()
    a=[]
    for i in data.each():
        if i.val()["LoaiTK"]=="0":
            a.append(i.val()["TenGV"])
    return a

def mh_khoa(ma):
    data=db.child("MonHoc").order_by_child("MaKhoa").equal_to(str(ma)).get()
    a=[]
    for i in data.each():
        a.append(i.val()["TenMH"])
    pass
    return a

def manh_ten(ten):
    data=db.child("NamHoc").order_by_child("TenNH").equal_to(str(ten)).get()
    a=""
    for i in data.each():
        if(i.val()["TenNH"]==str(ten)):
            a=(i.val()["MaNH"])
    return a


def them_tkb(magv,mamh,loai,ngay,ca,malop,hki,nam):
    ma=matkb()
    data={'MaTKB':str(ma),'MaGV':str(magv),'MaMH':str(mamh),'PP_Giang':str(loai),'Ngay':str(ngay),'Ca':str(ca),'MaLop':str(malop),'HocKy':str(hki),'NamHoc':str(nam),'TrangThaiDD':"0"}
    try:
        db.child('ThoiKhoaBieu').push(data)
        return True
    except:
        return False



def bang_tkb(malop,namhoc,hocky):
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("Ngay").get()
        for i in data.each():
            if(i.val()["MaLop"]==str(malop) and i.val()["NamHoc"]==str(namhoc) and i.val()["HocKy"]==str(hocky)):
                gv=tengv_ma(i.val()["MaGV"])
                mh=tenmh_ma(i.val()["MaMH"])
                e=[gv,mh,i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"]]
                a.append(e)
    except:a=[]
    return a

def timkiem_dong_tkb(malop,namhoc,hocky,q):
    a=[]

    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["MaLop"]==str(malop) and i.val()["NamHoc"]==str(namhoc) and i.val()["HocKy"]==str(hocky)):
                gv=tengv_ma(i.val()["MaGV"])
                mh=tenmh_ma(i.val()["MaMH"])
                e=[gv,mh,i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"]]
                if khong_dau(str(q.lower())) in khong_dau(gv.lower()) or khong_dau(str(q.lower())) in khong_dau(mh.lower()) or khong_dau(str(q.lower())) in khong_dau(i.val()["PP_Giang"].lower()) or khong_dau(str(q.lower())) in khong_dau(i.val()["Ngay"].lower()) or khong_dau(str(q.lower())) in khong_dau(i.val()["Ca"].lower()) :
                    a.append(e)
    except:a=[]
    return a


def kt_lichgiang(magv,ngay,ca):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and str(ca) in i.val()["Ca"] and i.val()["MaGV"]==str(magv)):
                a.append(i.val()["MaGV"])
    except: a=[]
    return a

def kt_lich_tkb(malop,ngay,ca):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and str(ca) in i.val()["Ca"] and i.val()["MaLop"]==str(malop)):
                a.append(i.val()["MaLop"])
    except:a=[]
    return a


def xoa_dong_tkb(magv,mamh,ngay,ca,pp):
    data=db.child("ThoiKhoaBieu").get()
    for i in data.each():
        if(i.val()["MaGV"]==str(magv) and  i.val()["MaMH"]==str(mamh)and i.val()["Ngay"]==str(ngay)and i.val()["Ca"]==str(ca) and i.val()["PP_Giang"]==str(pp) and i.val()["TrangThaiDD"]=="0"):
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


def ngaya_nhohon_ngayb(a,b):
    ngay_a=a.replace("/"," ").split()
    ngay_b=b.replace("/"," ").split()
    if ngay_a[2]>ngay_b[2]:
        return False
    elif ngay_a[2]==ngay_b[2] and ngay_a[1]>ngay_b[1]:
        return False
    elif ngay_a[2]==ngay_b[2] and ngay_a[1]==ngay_b[1] and ngay_a[0]>=ngay_b[0]:
        return False
    else:
        return True

def gv_dd(magv,ngay):
    a=[]
    data=db.child("ThoiKhoaBieu").order_by_child("TrangThaiDD").equal_to("0").get()
    try:
        for i in data.each():
            if(i.val()["MaGV"]==str(magv) and ngaya_nhohon_ngayb(i.val()["Ngay"] , str(ngay)) and i.val()["TrangThaiDD"] =='0' ):
                tenl=tenlop_ma(i.val()['MaLop'])
                tenm=tenmh_ma(i.val()['MaMH'])
                e = [i.val()['MaTKB'],tenl,tenm,i.val()['Ngay'],i.val()['Ca']]
                a.append(e)
                
    except: a=[]
    return a

def namhoc():
    a=""
    try:
        data=db.child("NamHoc").get()
        for i in data.each():
            a=(i.val()["TenNH"])
    except:a=""
    return a

def capnhat_namhoc():
    nam=datetime.datetime.now()
    nam=nam.strftime("%Y")
    nam2=int(nam)+1
    namhoc=str(nam)+"-"+str(nam2)
    a=[]
    dl={'TenNH':namhoc, 'MaNH':str(nam)}
    try:
        data=db.child("NamHoc").get()
        for i in data.each():
            if (i.val()['TenNH'] == str(namhoc)):
                a.append(i.val()['TenNH'])
    except:a=[]
    if a ==[]:
        db.child("NamHoc").push(dl)
    else: return


    
capnhat_namhoc()
def matkb():
    try:
        data = db.child("ThoiKhoaBieu").get()
        for i in data.each():
            e=[i.val()["MaTKB"]]
            a=str(int(max(e))+1)
    except:a=0
    return a

