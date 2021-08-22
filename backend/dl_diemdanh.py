import conect_firebase
from backend.dl_monhoc import tenmh_ma
from backend.dl_adminlop import tenlop_ma
import datetime

db=conect_firebase.connect().database()
# https://qastack.vn/programming/2405292/how-to-check-if-text-is-empty-spaces-tabs-newlines-in-python
# kt chuooix chir cos khoangr troongs

def cahoc():
    time = datetime.datetime.now()
    now = time.strftime("%H:%M:%S")
    a=""
    data=db.child("CaHoc").get()
    for i in data.each():
        if(i.val()["TGBD"]<=str(now) and i.val()["TGKT"]>=str(now)):
            a=i.val()["TenCa"]
    return a


def thong_tin_theo_tkb(magv,ngay,ca):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["MaGV"]==str(magv) and i.val()["Ngay"]==str(ngay) and str(ca) in i.val()["Ca"]):
                a.append(tenlop_ma(str(i.val()["MaLop"])))
                a.append(tenmh_ma(str(i.val()["MaMH"])))
                a.append(str(i.val()["MaTKB"]))
    except: a=[]
    return a

def kt_TT_diemdanh(matkb):
    a=""
    data=db.child("ThoiKhoaBieu").get()
    for i in data.each():
        if(i.val()["MaTKB"]==str(matkb)):
            a=str(i.val()["TrangThaiDD"])
    return a


def diem_danh_vao_csdl(matkb,masv,thongtin,malop,mamh,magv,ngay,ca):
    data={'Ma':str(matkb),'MaSV':str(masv),'ThongTin':str(thongtin),'MaLop':str(malop),'MaMH':str(mamh),'MaGV':str(magv),'Ngay':str(ngay),'Ca':str(ca),'TG_Vao':'','TG_Ra':''}
    try:
        db.child('DiemDanh').push(data)
        return True
    except:
        return False

def update_TT_diemdanh(ma):
    data=db.child("ThoiKhoaBieu").get()
    dl={'TrangThaiDD':'1'}
    for i in data.each():
        if(i.val()["MaTKB"]==str(ma)):
            try:
                db.child("ThoiKhoaBieu").child(i.key()).update(dl)
                return True
            except:
                return False

def bangdiemdanh(ma):
    a=[]
    try:
        data=db.child("DiemDanh").get()
        for i in data.each():
            if(i.val()["Ma"]==str(ma)):
                e=[i.val()["MaSV"],i.val()["ThongTin"],i.val()["TG_Vao"],i.val()["TG_Ra"],i.val()["GhiChu"]]
                a.append(e)
    except:
        a=[]
    return a

