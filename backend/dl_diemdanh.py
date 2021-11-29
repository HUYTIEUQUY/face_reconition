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

def catkb(matkb):
    a=0
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("MaTKB").equal_to(str(matkb)).get()
        for i in data.each():
            if(i.val()["MaTKB"]==str(matkb)):
                a=i.val()["Ca"]
    except:a=0
    return a


def cong_them_gio(now):
    d1 = datetime.datetime.strptime(now, "%H:%M:%S")
    d=d1 + datetime.timedelta(hours=5)
    d=str(d).split()
    return d[1]
def tru_gio(now):
    d1 = datetime.datetime.strptime(now, "%H:%M:%S")
    d=d1 - datetime.timedelta(hours=1)
    d=str(d).split()
    return d[1]

def cong_ngay(ngay):
    d1 = datetime.datetime.strptime(ngay, "%d/%m/%Y")
    d=d1 + datetime.timedelta(days=180)
    d=str(d).split()
    return d[0]



def khoang_tgvao(tenca):
    time = datetime.datetime.now()
    now = time.strftime("%H:%M:%S")
    try:
        data=db.child("CaHoc").order_by_child("TenCa").equal_to(str(tenca)).get()
        for i in data.each():
            print(cong_them_gio(i.val()["TGBD"]))
            if(cong_them_gio(i.val()["TGBD"])>=str(now)):
                return True
            else:return False
    except: return True
def khoang_tgra(tenca):
    time = datetime.datetime.now()
    now = time.strftime("%H:%M:%S")
    try:
        data=db.child("CaHoc").order_by_child("TenCa").equal_to(str(tenca)).get()
        for i in data.each():
            if(tru_gio(i.val()["TGKT"])<=str(now)):
                return True
            else:return False
    except: return True


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
def hen_ngay_xoa_du_lieu(matkb,ngay):
    ngay=cong_ngay(ngay).split("-")
    a=str(ngay[2])+"/"+str(ngay[1])+"/"+str(ngay[0])
    data = {'Ma':str(matkb),'Ngay':str(a)}
    try:
        db.child('NgayXoaDL').push(data)
        return True
    except:
        return False

def xoa_dl_diemdanh(ma):
    try:
        data=db.child('DiemDanh').order_by_child('Ma').equal_to(str(ma)).get()
        for i in data.each():
            if  i.val()["Ma"] == str(ma):
                db.child('DiemDanh').child(i.key()).remove()
                return True
    except:return False
def xoa_dl_tkb(ma):
    data=db.child('ThoiKhoaBieu').order_by_child('MaTKB').equal_to(str(ma)).get()
    for i in data.each():
        if  i.val()["MaTKB"] == str(ma):
            db.child('ThoiKhoaBieu').child(i.key()).remove()
            return True


def tra_dl_diemdanh(ngay):
    data=db.child('NgayXoaDL').get()
    for i in data.each():
        date1 = datetime.datetime.strptime(str(ngay), '%d/%m/%Y')
        date2 = datetime.datetime.strptime(str(i.val()["Ngay"]), '%d/%m/%Y')
        if date1 >= date2:
            if xoa_dl_diemdanh(str(i.val()['Ma'])) ==True and  xoa_dl_tkb(str(i.val()['Ma']))==True:
                db.child('NgayXoaDL').child(i.key()).remove()
                return True

def kt_hen_ngay_xoa(matkb):
    try:
        data=db.child('NgayXoaDL').order_by_child('Ma').equal_to(str(matkb)).get()
        for i in data.each():
            if i.val()['Ma']==str(matkb):
                return True
            else:return False
    except:return False

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
# def capnhatthongtin(ma,masv):
#     data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
#     dl={'ThongTin':'vắng'}
#     for i in data.each():
#         if(i.val()["Ma"]==str(ma) and i.val()["MaSV"] == str(masv)):
#             try:
#                 db.child("DiemDanh").child(i.key()).update(dl)
#             except:
#                 print('Lỗi update của hàm capnhatthongtin trong dl_diemdanh')

def kiemtrathongtin(ma):
    dl={'ThongTin':'Vắng'}
    try:
        data = db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if i.val()["TG_Vao"]==str("") or i.val()["TG_Ra"]==str(""):
                db.child("DiemDanh").child(i.key()).update(dl)
    except:print('Lỗi kiemtrathongtin trong dl_diemdanh')

def bangdiemdanh(ma):
    a=[]
    try:
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if(i.val()["Ma"]==str(ma)):
                e=[i.val()["MaSV"],i.val()["MaSV"] ,i.val()["ThongTin"],i.val()["TG_Vao"],i.val()["TG_Ra"],i.val()["GhiChu"]]
                a.append(e)
    except:
        a=[]
    sx_ma = sorted(a, key=lambda item: (item[0]))
    return sx_ma
def bangdiemdanh1(ma,malop):
    a=[]

    data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
    for i in data.each():
        if(i.val()["Ma"]==str(ma) and i.val()["MaLop"] ==str(malop)):
            e=[i.val()["MaSV"],i.val()["MaSV"] ,i.val()["ThongTin"],i.val()["TG_Vao"],i.val()["TG_Ra"],i.val()["GhiChu"]]
            a.append(e)
    sx_ma = sorted(a, key=lambda item: (item[0]))
    return sx_ma

def dd_sv_vao(ma):
    a=[]
    try:
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if i.val()["Ma"]==str(ma):
                a.append(i.val()["MaSV"])
                
    except:
        a=[]
    return a
def dd_sv_ra(ma):
    a=[]
    try:
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if i.val()["Ma"]==str(ma) and i.val()["TG_Ra"] != "":
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

def sv_da_dd_vao(ma):
    a=[]
    try:
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if i.val()["Ma"]==str(ma) and i.val()["TG_Vao"] != "":
                a.append(i.val()["MaSV"])
    except:
        a=[]
    return a
def sv_da_dd_vao1(ma,malop):
    a=[]
    try:
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if i.val()["Ma"]==str(ma) and i.val()["TG_Vao"] != "" and i.val()['MaLop']==str(malop):
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
        data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(ma)).get()
        for i in data.each():
            if(i.val()["Ma"]==str(ma)):
                e=[i.val()["MaSV"],tensv_ma(i.val()["MaSV"]) ,i.val()["ThongTin"],i.val()["TG_Vao"],i.val()["TG_Ra"],i.val()["GhiChu"]]
                if khong_dau(str(q)) in khong_dau(i.val()["MaSV"]) or khong_dau(str(q)) in khong_dau(tensv_ma(i.val()["MaSV"])) or khong_dau(str(q)) in khong_dau(i.val()["ThongTin"])or khong_dau(str(q)) in khong_dau(i.val()["TG_Vao"])or khong_dau(str(q)) in khong_dau(i.val()["TG_Ra"])or khong_dau(str(q)) in khong_dau(i.val()["GhiChu"]):
                    a.append(e)
    except:
        a=[]
    sx_ma = sorted(a, key=lambda item: (item[0]))
    return a

def capnhat_tgra(matkb,masv,tgra):
    data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(matkb)).get()
    dl_ktt={'TG_Ra':str(tgra)}
    dl1={'TG_Ra':str(tgra),'ThongTin':str('Vắng')}
    for i in data.each():
        if(i.val()["Ma"] == str(matkb) and i.val()["MaSV"] == str(masv) and str(i.val()["TG_Vao"]) == str("")):
            try:
                db.child("DiemDanh").child(i.key()).update(dl1)
            except:
                print('Lỗi do capnhat_tgra trong dl_diemdanh')
        elif i.val()["Ma"] == str(matkb) and i.val()["MaSV"] == str(masv):
            try:
                db.child("DiemDanh").child(i.key()).update(dl_ktt)
            except:
                print('Lỗi do capnhat_tgra trong dl_diemdanh')
        

def capnhat_tgvao(matkb,masv,tgvao,tt):
    data=db.child("DiemDanh").order_by_child("Ma").equal_to(str(matkb)).get()
    dl={'TG_Vao':str(tgvao), 'ThongTin':str(tt)}
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
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("MaTKB").equal_to(str(matkb)).get()
        for i in data.each():
            e=i.val()["Ca"]
        a=e[0]
        root=db.child("CaHoc").order_by_child("TenCa").equal_to(str(a)).get()
        for i in root.each():
            tgbd=i.val()["TGBD"]
        return tgbd
    except:
        print("Error")

