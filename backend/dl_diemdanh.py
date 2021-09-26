import conect_firebase
from backend.dl_monhoc import tenmh_ma
from backend.dl_adminlop import tenlop_ma
from backend.dl_sinhvien import tensv_ma
import datetime
import re
db=conect_firebase.connect().database()
# https://qastack.vn/programming/2405292/how-to-check-if-text-is-empty-spaces-tabs-newlines-in-python
# kt chuooix chir cos khoangr troongs

def cahoc():
    time = datetime.datetime.now()
    now = time.strftime("%H:%M:%S")
    a="0"
    data=db.child("CaHoc").get()
    for i in data.each():
        if(i.val()["TGBD"]<=str(now) and i.val()["TGKT"]>=str(now)):
            a=i.val()["TenCa"]
    return a


def thong_tin_theo_tkb(magv,ngay,ca):
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("Ngay").equal_to(str(ngay)).get()
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


def diem_danh_vao_csdl(matkb,masv,thongtin,malop,mamh,magv,ngay,ca,tgvao):
    data={'Ma':str(matkb),'MaSV':str(masv),'ThongTin':str(thongtin),'MaLop':str(malop),'MaMH':str(mamh),'MaGV':str(magv),'Ngay':str(ngay),'Ca':str(ca),'TG_Vao':str(tgvao),'TG_Ra':'','GhiChu':''}
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
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if(i.val()["Ma"]==str(ma)):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]) ,i.val()["ThongTin"],i.val()["TG_Vao"]+" - "+i.val()["TG_Ra"],i.val()["GhiChu"]]
                a.append(e)
    except:
        a=[]
    return a

def sv_da_dd_khac_vang(ma):
    a=[]
    try:
        data=db.child("DiemDanh").get()
        for i in data.each():
            if i.val()["Ma"]==str(ma) and i.val()["ThongTin"] != "không":
                a.append(i.val()["MaSV"])
    except:
        a=[]
    return a
def sv_da_dd(ma):
    a=[]
    try:
        data=db.child("DiemDanh").get()
        for i in data.each():
            if i.val()["Ma"]==str(ma):
                a.append(i.val()["MaSV"])
    except:
        a=[]
    return a

def tg_tre(magv):
    try:
        data=db.child("tgtre").child(str(magv)).get()
        tgtre=data.val()['thoigian']
    except:
        tgtre="00:00"
    
    if tgtre== None:
        tgtre="00:00"
    return tgtre


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

def timkiem_dd(ma,q):
    a=[]
    try:
        data=db.child("DiemDanh").get()
        for i in data.each():
            if(i.val()["Ma"]==str(ma)):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]) ,i.val()["ThongTin"],i.val()["TG_Vao"]+" - "+i.val()["TG_Ra"],i.val()["GhiChu"]]
                if khong_dau(str(q)) in khong_dau(i.val()["MaSV"].lower()) or khong_dau(str(q)) in khong_dau(tensv_ma(i.val()["MaSV"]).lower()) or khong_dau(str(q)) in khong_dau(i.val()["ThongTin"].lower())or khong_dau(str(q)) in khong_dau(i.val()["TG_Vao"].lower())or khong_dau(str(q)) in khong_dau(i.val()["TG_Ra"].lower())or khong_dau(str(q)) in khong_dau(i.val()["GhiChu"].lower()):
                    a.append(e)
    except:
        a=[]
    return a


def capnhat_tgra(matkb,masv,tgra):
    data=db.child("DiemDanh").get()
    dl={'TG_Ra':str(tgra)}
    for i in data.each():
        if(i.val()["Ma"]==str(matkb) and i.val()["MaSV"]==str(masv)):
            try:
                db.child("DiemDanh").child(i.key()).update(dl)
                return True
            except:
                return False
    

def xoasv_dd(matkb,masv):
    try:
        data=db.child("DiemDanh").get()
        for i in data.each():
            if(i.val()["Ma"]==str(matkb) and i.val()["MaSV"]==str(masv)):
                
                    db.child("DiemDanh").child(i.key()).remove()
                    return True
    except:
        return False

def diemdanhbangexcel(matkb,masv,thongtin,malop,mamh,magv,ngay,ca,tgvao,tgra):
    data={'Ma':str(matkb),'MaSV':str(masv),'ThongTin':str(thongtin),'MaLop':str(malop),'MaMH':str(mamh),'MaGV':str(magv),'Ngay':str(ngay),'Ca':str(ca),'TG_Vao':str(tgvao),'TG_Ra':str(tgra),'GhiChu':''}
    try:
        db.child('DiemDanh').push(data)
        return True
    except:
        return False

def xoadd(matkb):
    data=db.child("DiemDanh").get()
    for i in data.each():
        if i.val()["Ma"] == str(matkb):
            db.child("DiemDanh").child(i.key()).remove()
               

# def tgca(tgvao,tgra,ca):
#     data=db.child("CaHoc").get()
#     for i in data.each():
#         if i.val()["TenCa"]==str(ca) and i.val()["TGBD"] <= str(tgvao) and i.val()["TGKT"] >= str(tgra):
#             return True
#     return False
def tgca(ca,e):
    data=db.child("CaHoc").get()
    for i in data.each():
        if i.val()["TenCa"] == str(ca) :
            e.append(i.val()['TGBD'])
            e.append(i.val()['TGKT'])

def tgbd_dd(matkb):
    data=db.child("ThoiKhoaBieu").order_by_child("MaTKB").equal_to(str(matkb)).get()
    for i in data.each():
        e=i.val()["Ca"]
    a=e[0]
    root=db.child("CaHoc").order_by_child("TenCa").equal_to(str(a)).get()
    for i in root.each():
        tgbd=i.val()["TGBD"]
    return tgbd