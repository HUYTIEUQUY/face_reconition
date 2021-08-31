
import conect_firebase
from backend.dl_sinhvien import khong_dau, tensv_ma
from backend.dl_giangvien import magv_ten, tengv_ma

db=conect_firebase.connect().database()

def tenlop_ma(ma):
    data=db.child("Lop").get()
    a=""
    for i in data.each():
        if(i.val()["MaLop"]==str(ma)):
            a=(i.val()["TenLop"])
    return a



def tenlop_dd(magv):
    data=db.child("DiemDanh").get()
    a=[]
    
    for i in data.each():
        if(i.val()["MaGV"] == str(magv)):
            tenlop=tenlop_ma(i.val()["MaLop"]) 
            if tenlop not in a:
                a.append(tenlop)
    return a

def malop_khoa(makhoa):
    data=db.child("Lop").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaKhoa"]== str(makhoa)):
                a.append(i.val()["MaLop"])
    except:a=[]
    return a


def malop_ten(tenlop):
    data=db.child("Lop").get()
    a=""
    try:
        for i in data.each():
            if(i.val()["TenLop"]== str(tenlop)):
                a= i.val()["MaLop"]
    except:a=""
    return a


def tenmh_ma(ma):
    data=db.child("MonHoc").get()
    a=""
    for i in data.each():
        if(i.val()["MaMH"]==str(ma)):
            a=(i.val()["TenMH"])
    return a

def mamh_ten(ten):
    data=db.child("MonHoc").get()
    a=""
    for i in data.each():
        if(i.val()["TenMH"]==str(ten)):
            a=(i.val()["MaMH"])
    return a

def monhoc_dd(magv,malop):
    data=db.child("DiemDanh").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop)):
                tenmh=tenmh_ma(i.val()["MaMH"]) 
                if tenmh not in a:
                    a.append(tenmh)
    except:a=[]
    return a

def ngay_dd(magv,malop,mamh):
    data=db.child("DiemDanh").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh)):
                if i.val()["Ngay"] not in a:
                    a.append(i.val()["Ngay"])
    except:a=[]
    return a

def ca_dd(magv,malop,mamh,ngay):
    data=db.child("DiemDanh").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh) and i.val()["Ngay"]==str(ngay)):
                if i.val()["Ca"] not in a:
                    a.append(i.val()["Ca"])
    except:a=[]
    return a

def tensv_ma(ma):
    data=db.child("SinhVien").get()
    a=""
    for i in data.each():
        if(i.val()["MaSV"]==str(ma)):
            a=(i.val()["TenSV"])
    return a

def thongke(magv,malop,mamh,ngay,ca):
    data=db.child("DiemDanh").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh) and i.val()["Ngay"]==str(ngay) and i.val()["Ca"]==str(ca)):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]) ,i.val()["ThongTin"],i.val()["TG_Vao"]+" - "+i.val()["TG_Ra"],i.val()["GhiChu"]]
                a.append(e)
    except:a=[]
    return a

def tengv_all():
    data=db.child("GiangVien").get()
    a=[]
    for i in data.each(): 
        tengv=(i.val()["TenGV"])
        if(len(list(magv_ten(tengv)))>=6):
            if tengv not in a:
                a.append(tengv)
    return a

def tenlop_dd1():
    data=db.child("DiemDanh").get()
    a=[]
    for i in data.each():
        tenlop=tenlop_ma(i.val()["MaLop"]) 
        if tenlop not in a:
            a.append(tenlop)
    return a

def tim_tk(magv,malop,mamh,ngay,ca,q):
    a=[]
    data=db.child("DiemDanh").get()
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh) and i.val()["Ngay"]==str(ngay) and i.val()["Ca"]==str(ca)):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]) ,i.val()["ThongTin"],i.val()["TG_Vao"]+" - "+i.val()["TG_Ra"],i.val()["GhiChu"]]
                if str(q) in khong_dau(i.val()["MaSV"].lower()) or str(q) in khong_dau(tensv_ma(i.val()["MaSV"]).lower()):
                    a.append(e)
                print(e)
    except: a=[]
    print(a)
    return a

