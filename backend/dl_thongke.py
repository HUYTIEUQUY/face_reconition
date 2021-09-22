
import conect_firebase
from backend.dl_sinhvien import khong_dau, tensv_ma
from backend.dl_giangvien import magv_ten, tengv_ma

db=conect_firebase.connect().database()

def tenlop_ma(ma):
    data=db.child("Lop").order_by_child("MaLop").equal_to(str(ma)).get()
    a=""
    for i in data.each():
        a=(i.val()["TenLop"])
    return a



def tenlop_dd(magv):
    data=db.child("DiemDanh").order_by_child("MaGV").equal_to(str(magv)).get()
    a=[]
    b=[]
    for i in data.each():
        if i.val()["MaLop"] not in b:
            b.append(i.val()["MaLop"])
            a.append(tenlop_ma(i.val()["MaLop"]))

    return a


def malop_ten(tenlop):
    data=db.child("Lop").order_by_child("TenLop").equal_to(str(tenlop)).get()
    a=""
    try:
        for i in data.each():
            a= i.val()["MaLop"]
    except:a=""
    return a


def tenmh_ma(ma):
    data=db.child("MonHoc").order_by_child("MaMH").equal_to(str(ma)).get()
    a=""
    for i in data.each():
        a=(i.val()["TenMH"])
    return a

def mamh_ten(ten):
    data=db.child("MonHoc").order_by_child("TenMH").equal_to(str(ten)).get()
    a=""
    for i in data.each():
        a=(i.val()["MaMH"])
    return a

def monhoc_dd(magv,malop):
    data=db.child("DiemDanh").order_by_child("MaGV").equal_to(str(magv)).get()
    a=[]
    b=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop)):
                if i.val()["MaMH"] not in b:
                    tenmh=tenmh_ma(i.val()["MaMH"])
                    a.append(tenmh)
                    b.append(i.val()["MaMH"])
    except:a=[]
    return a

def ngay_dd(magv,malop,mamh):
    data=db.child("DiemDanh").order_by_child("MaGV").equal_to(str(magv)).get()
    a=[]
    try:
        for i in data.each():
            if ( i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh)):
                if i.val()["Ngay"] not in a:
                    a.append(i.val()["Ngay"])
    except:a=[]
    return a

def ca_dd(magv,malop,mamh,ngay):
    data=db.child("DiemDanh").order_by_child("Ngay").equal_to(str(ngay)).get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh)):
                if i.val()["Ca"] not in a:
                    a.append(i.val()["Ca"])
    except:a=[]
    return a

def tensv_ma(ma):
    data=db.child("SinhVien").order_by_child("MaSV").equal_to(str(ma)).get()
    a=""
    for i in data.each():
        a=(i.val()["TenSV"])
    return a

def thongke(magv,malop,mamh,ngay,ca):
    data=db.child("DiemDanh").order_by_child("Ngay").equal_to(str(ngay)).get()
    a=[]
    try:
        for i in data.each():
            if i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh) and i.val()["Ca"]==str(ca):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]), i.val()["ThongTin"], i.val()["TG_Vao"]+" - "+i.val()["TG_Ra"], i.val()["GhiChu"]]
                a.append(e)
                
    except:a=[]
    return a

def tim_tk(magv,malop,mamh,ngay,ca,q):
    a=[]
    data=db.child("DiemDanh").order_by_child("Ngay").equal_to(str(ngay)).get()
    try:
        for i in data.each():
            if(i.val()["MaGV"]== str(magv) and i.val()["MaLop"]== str(malop) and i.val()["MaMH"]==str(mamh) and i.val()["Ngay"]==str(ngay) and i.val()["Ca"]==str(ca)):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]) ,i.val()["ThongTin"],i.val()["TG_Vao"]+" - "+i.val()["TG_Ra"],i.val()["GhiChu"]]
                if khong_dau(str(q)) in khong_dau(i.val()["MaSV"].lower()) or khong_dau(str(q)) in khong_dau(tensv_ma(i.val()["MaSV"]).lower()) or khong_dau(str(q)) in khong_dau(i.val()["ThongTin"].lower())or khong_dau(str(q)) in khong_dau(i.val()["TG_Vao"].lower())or khong_dau(str(q)) in khong_dau(i.val()["TG_Ra"].lower())or khong_dau(str(q)) in khong_dau(i.val()["GhiChu"].lower()):
                    a.append(e)
    except: a=[]
    return a

def ds_khoa():
    a=[]
    data=db.child("Khoa").get()
    try:
        for i in data.each():
            a.append(i.val()["TenKhoa"])
    except:a=[]
    return a

def makhoa_ten(tenkhoa):
    a=''
    
    try:
        data=db.child("Khoa").order_by_child("TenKhoa").equal_to(str(tenkhoa)).get()
        print(data.val())
        for i in data.each():
                a=i.val()["MaKhoa"]
    except:a=''
    return a

def tengv_dd():
    data=db.child("DiemDanh").get()
    a=[]
    for i in data.each():
        a.append(i.val()['MaGV'])
    return a

def ds_gv(makhoa):
    data=db.child("GiangVien").order_by_child("MaKhoa").equal_to(str(makhoa)).get()
    a=[]
    b=tengv_dd()
    for i in data.each():
        if i.val()['MaKhoa'] == str(makhoa) and i.val()['LoaiTK']=="0" and i.val()['MaGV'] in b:
            a.append(i.val()['MaGV']+"-"+i.val()['TenGV'])
    return a




