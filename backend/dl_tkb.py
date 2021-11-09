import conect_firebase
from backend.dl_giangvien import tengv_ma
from backend.dl_monhoc import tenmh_ma
import re
from kt_nhap import khong_dau
import datetime
import threading
import time
db=conect_firebase.connect().database()

def lop_khoa(ma):
    data=db.child("Lop").order_by_child("MaKhoa").equal_to(str(ma)).get()
    a=[]
    for i in data.each():
            a.append(i.val()["TenLop"])
    return a
def all_lop():
    data=db.child("Lop").get()
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

def lop_matkb(ma):
    data=db.child("ThoiKhoaBieu").order_by_child("MaTKB").equal_to(str(ma)).get()
    a=[]
    for i in data.each():
        tenlop=tenlop_ma(i.val()["MaLop"])
        a.append(tenlop)
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
        threading.Thread(target=cong_so_tiet,args=(malop,mamh,loai,ca,)).start()
        return True
    except:
        return False


def sotiet_cahoc(ca):
    sotiet=0
    try:
        for i in ca:
            k=db.child('CaHoc').order_by_child("TenCa").equal_to(str(i)).get()
            tgbd=k[0].val()['TGBD']
            tgkt=k[0].val()['TGKT']
            format = '%H:%M:%S'
            stiet=datetime.datetime.strptime(tgkt, format) - datetime.datetime.strptime(tgbd, format)
            stiet=str(stiet).split(':')
            so = (int(stiet[0])*60+int(stiet[1])) / 50
            sotiet +=int(so)
        return sotiet
    except:return 0

def sotietdahoc(malop,mamh,loai):
    if loai=="Lý thuyết":
        l="LT"
    else:
        l="TH"
    try:
        data=db.child('SoTietDaHoc').order_by_child("Ma").equal_to(str(malop)+str(mamh)+str(l)).get()
        return data[0].val()['SoTiet']
    except:return 0
        

def cong_so_tiet(malop,mamh,loai,ca):
    sotietdahoc=0
    sotietthem=sotiet_cahoc(ca)
    
    if loai=="Lý thuyết":
        l="LT"
    else:
        l="TH"

    data=db.child('SoTietDaHoc').order_by_child("Ma").equal_to(str(malop)+str(mamh)+str(l)).get()
    if data.val()!=[]:
        sotietdahoc=int(data[0].val()['SoTiet'])+sotietthem
        info={'MaLop':str(malop),'MaMH':str(mamh),'PP_Giang':str(loai),'SoTiet':str(sotietdahoc)}
        db.child('SoTietDaHoc').child(data[0].key()).update(info)
    else:
        info={'Ma':str(malop)+str(mamh)+l,'MaMH':str(mamh),'MaLop':str(malop),'MaMH':str(mamh),'PP_Giang':str(loai),'SoTiet':str(sotietthem)}
        db.child('SoTietDaHoc').push(info)

def tru_so_tiet(malop,mamh,loai,ca):
    sotietdahoc=0
    sotiettru=sotiet_cahoc(ca)
    
    if loai=="Lý thuyết":
        l="LT"
    else:
        l="TH"

    data=db.child('SoTietDaHoc').order_by_child("Ma").equal_to(str(malop)+str(mamh)+str(l)).get()
    if data.val()!=[]:
        sotietdahoc=int(data[0].val()['SoTiet'])-sotiettru
        if sotietdahoc != str("0"):
            info={'MaLop':str(malop),'MaMH':str(mamh),'PP_Giang':str(loai),'SoTiet':str(sotietdahoc)}
            db.child('SoTietDaHoc').child(data[0].key()).update(info)
        else:
            db.child('SoTietDaHoc').child(data[0].key()).remove()



def SoTietCuaMH(mamh,loai):
    data=db.child('MonHoc').order_by_child("MaMH").equal_to(str(mamh)).get()
    for i in data.each():
        if i.val()["MaMH"] == str(mamh) and loai=="Lý thuyết":
            sotiet=int(i.val()['SoTietLyThuyet'])
            return sotiet
        else:
            sotiet=int(i.val()['SoTietThucHanh'])
            return sotiet



def them_tkb1(ma,magv,mamh,loai,ngay,ca,malop,hki,nam):
    
    data={'MaTKB':str(ma),'MaGV':str(magv),'MaMH':str(mamh),'PP_Giang':str(loai),'Ngay':str(ngay),'Ca':str(ca),'MaLop':str(malop),'HocKy':str(hki),'NamHoc':str(nam),'TrangThaiDD':"0"}
    try:
        db.child('ThoiKhoaBieu').push(data)
        threading.Thread(target=cong_so_tiet,args=(malop,mamh,loai,ca,)).start()
        return True
    except:
        return False
def sua_tkb(matkb,magv,mamh,loai,ngay,ca,malop,hki,nam):
    data={'MaGV':str(magv),'MaMH':str(mamh),'PP_Giang':str(loai),'Ngay':str(ngay),'Ca':str(ca),'MaLop':str(malop),'HocKy':str(hki),'NamHoc':str(nam),'TrangThaiDD':"0"}
    try:
        root=db.child('ThoiKhoaBieu').order_by_child("MaTKB").equal_to(str(matkb)).get()
        for i in root.each():
            if i.val()["MaTKB"] == str(matkb):
                db.child('ThoiKhoaBieu').child(i.key()).update(data)
                if i.val()["PP_Giang"] == "Lý thuyết":
                    loai="LT"
                else: loai="TH"
                threading.Thread(target=capnhat_tietdahoc,args=(str(i.val()["MaLop"]),str(i.val()["MaMH"]),loai,str(i.val()["Ca"]),malop,mamh,loai,ca,)).start()
        return True
    except:
        return False


def sua_tkb1(matkb,magv,mamh,loai,ngay,ca,malop,hki,nam):
    data={'MaGV':str(magv),'MaMH':str(mamh),'PP_Giang':str(loai),'Ngay':str(ngay),'Ca':str(ca),'MaLop':str(malop),'HocKy':str(hki),'NamHoc':str(nam),'TrangThaiDD':"0"}
    try:
        root=db.child('ThoiKhoaBieu').order_by_child("MaTKB").equal_to(str(matkb)).get()
        for i in root.each():
            if i.val()["MaTKB"] == str(matkb) and i.val()["MaLop"] == str(malop):
                db.child('ThoiKhoaBieu').child(i.key()).update(data)
                if i.val()["PP_Giang"] == "Lý thuyết":
                    loai="LT"
                else: loai="TH"
                threading.Thread(target=capnhat_tietdahoc,args=(str(i.val()["MaLop"]),str(i.val()["MaMH"]),loai,str(i.val()["Ca"]),malop,mamh,loai,ca,)).start()
        return True
    except:
        return False

def capnhat_tietdahoc(malop_c,mamh_c,loai_c,ca_c, malop_m,mamh_m,loai_m,ca_m):
    mam = malop_m+mamh_m+loai_m
    mac = malop_c+mamh_c+loai_c
    

    sotiet_camoi = sotiet_cahoc(ca_m)
    sotiet_cacu = sotiet_cahoc(ca_c)
    print("So tiet ca cu"+str(sotiet_cacu))
    print("So tiet ca moi"+str(sotiet_camoi))
    if mam == mac:
        if int(sotiet_camoi) > int(sotiet_cacu):
            sotiet=sotiet_camoi-sotiet_cacu
            update_stdh(mam,sotiet,"cong")
        elif  int(sotiet_camoi) < int(sotiet_cacu):
            sotiet=sotiet_cacu-sotiet_camoi
            update_stdh(mam,sotiet,"tru")
    else :
        cong_so_tiet(malop_m,mamh_m,loai_m,ca_m)
        tru_so_tiet( malop_c,mamh_c,loai_c,ca_c)

def update_stdh(ma,sotiet,pheptinh):
    data = db.child('SoTietDaHoc').order_by_child("Ma").equal_to(ma).get()
    if data.val()!=[]:
        print(pheptinh=="cong")
        if pheptinh=="cong":
            sotietdahoc=int(data[0].val()['SoTiet'])+int(sotiet)
        else:
            sotietdahoc=int(data[0].val()['SoTiet'])-int(sotiet)
        info = {'SoTiet':str(sotietdahoc)}
        db.child('SoTietDaHoc').child(data[0].key()).update(info)



def bang_tkb(malop,namhoc,hocky,magv):
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("Ngay").get()
        for i in data.each():
            if(i.val()["MaLop"]==str(malop) and i.val()["NamHoc"]==str(namhoc) and i.val()["HocKy"]==str(hocky) and i.val()["MaGV"]==str(magv)) :
                if(i.val()["TrangThaiDD"]=="0"):
                    tt="Chưa điểm danh"
                else: tt="Đã điểm danh"
                e=[i.val()["MaTKB"],i.val()["MaMH"],i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"],tt]
                a.append(e)
    except:a=[]
    format = '%d/%m/%Y'
    sx_ngay = sorted(a, key=lambda item: (datetime.datetime.strptime(item[3], format), item[0]), reverse=True)
    return sx_ngay
    
def bang_tkb1(namhoc,hocky,magv):
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("Ngay").get()
        for i in data.each():
            if( i.val()["NamHoc"]==str(namhoc) and i.val()["HocKy"]==str(hocky) and i.val()["MaGV"]==str(magv)) :
                if(i.val()["TrangThaiDD"]=="0"):
                    tt="Chưa điểm danh"
                else: tt="Đã điểm danh"
                e=[i.val()["MaTKB"],i.val()["MaLop"],i.val()["MaMH"],i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"],tt]
                a.append(e)
    except:a=[]
    format = '%d/%m/%Y'
    sx_ngay = sorted(a, key=lambda item: (datetime.datetime.strptime(item[4], format), item[0]), reverse=True)
    return sx_ngay


def timkiem_dong_tkb(malop,namhoc,hocky,magv,q,loai):
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("MaLop").equal_to(str(malop)).get()
        for i in data.each():
            if(i.val()["MaLop"] == str(malop) and i.val()["NamHoc"] == str(namhoc) and i.val()["HocKy"]==str(hocky) and i.val()["MaGV"]==str(magv)):
                mh=tenmh_ma(i.val()["MaMH"])
                if(i.val()["TrangThaiDD"]=="0"):
                    tt="Chưa điểm danh"
                else: tt="Đã điểm danh"
                e=[i.val()["MaTKB"],mh,i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"],tt]
                if loai =="Mã TKB" and khong_dau(str(q.lower())) in khong_dau(i.val()["MaTKB"].lower()):
                    a.append(e)
                elif loai =="Môn học" and khong_dau(str(q.lower())) in khong_dau(mh.lower()):
                    a.append(e)
                elif loai =="LT-TH" and khong_dau(str(q.lower())) in khong_dau(tt.lower()):
                    a.append(e)
                elif loai =="Ngày" and khong_dau(str(q.lower())) in khong_dau(i.val()["Ngay"].lower()):
                    a.append(e)
                elif loai =="Ca" and khong_dau(str(q.lower())) in khong_dau(i.val()["Ca"].lower()):
                    a.append(e)
                elif loai =="Trạng Thái" and khong_dau(str(q.lower())) in khong_dau(tt.lower()):
                    a.append(e)
    except:a=[]
    format = '%d/%m/%Y'
    sx_ngay = sorted(a, key=lambda item: (datetime.datetime.strptime(item[3], format), item[0]), reverse=True)
    return sx_ngay

def timkiem_dong_tkb1(namhoc,hocky,magv,q,loai):
    global a
    a=[]

    try:
        data=db.child("ThoiKhoaBieu").order_by_child("MaGV").equal_to(str(magv)).get()
        for i in data.each():
            if(i.val()["NamHoc"] == str(namhoc) and i.val()["HocKy"]==str(hocky) and i.val()["MaGV"]==str(magv)):
                mh=tenmh_ma(i.val()["MaMH"])
                lop=tenlop_ma(i.val()['MaLop'])
                if(i.val()["TrangThaiDD"]=="0"):
                    tt="Chưa điểm danh"
                else: tt="Đã điểm danh"
                e=[i.val()["MaTKB"],lop,mh,i.val()["PP_Giang"],i.val()["Ngay"],i.val()["Ca"],tt]
                if loai =="Mã TKB" and khong_dau(str(q.lower())) in khong_dau(i.val()["MaTKB"].lower()):
                    a.append(e)
                elif loai =="Môn học" and khong_dau(str(q.lower())) in khong_dau(mh.lower()):
                    a.append(e)
                elif loai =="Lớp" and khong_dau(str(q.lower())) in khong_dau(lop.lower()):
                    a.append(e)
                elif loai =="LT-TH" and khong_dau(str(q.lower())) in khong_dau(tt.lower()):
                    a.append(e)
                elif loai =="Ngày" and khong_dau(str(q.lower())) in khong_dau(i.val()["Ngay"].lower()):
                    a.append(e)
                elif loai =="Ca" and khong_dau(str(q.lower())) in khong_dau(i.val()["Ca"].lower()):
                    a.append(e)
                elif loai =="Trạng Thái" and khong_dau(str(q.lower())) in khong_dau(tt.lower()):
                    a.append(e)
    except:a=[]
    return a

def kt_lichgiang_them(magv,ngay,ca,matkb):
    a=[]
    data=db.child("ThoiKhoaBieu").order_by_child("MaGV").equal_to(str(magv)).get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and str(ca) in i.val()["Ca"] and i.val()["MaGV"]==str(magv) and i.val()["MaTKB"] != str(matkb)):
                a.append(i.val()["MaTKB"])
    except: a=[]
    return a
def kt_lichgiang_sua(magv,mamh,ngay,ca,matkb):
    a=[]
    data=db.child("ThoiKhoaBieu").order_by_child("MaGV").equal_to(str(magv)).get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and str(ca) in i.val()["Ca"] and i.val()["MaGV"]==str(magv) and i.val()["MaTKB"] != str(matkb)) and  i.val()["MaMH"] != str(mamh):
                a.append(i.val()["MaTKB"])
    except: a=[]
    return a

def kt_lich_tkb(malop,ngay,ca,matkb):
    a=[]
    data=db.child("ThoiKhoaBieu").order_by_child("MaLop").equal_to(str(malop)).get()
    try:
        for i in data.each():
            if(i.val()["Ngay"]==str(ngay) and str(ca) in i.val()["Ca"] and i.val()["MaLop"]==str(malop) and i.val()["MaTKB"]!=str(matkb)):
                a.append(i.val()["MaLop"])
    except:a=[]
    return a

def kt_tkb_dd(matkb):
    a=[]
    try:
        data=db.child("ThoiKhoaBieu").order_by_child("MaTKB").equal_to(str(matkb)).get()
        for i in data.each():
            if  i.val()["TrangThaiDD"] == "1":
                a.append(i.val()["MaTKB"])
    except:a=[]
    return a


def xoa_dong_tkb(matkb):
    data=db.child("ThoiKhoaBieu").order_by_child("MaTKB").equal_to(str(matkb)).get()
    for i in data.each():
        if i.val()["MaTKB"] == str(matkb) and i.val()["TrangThaiDD"] == "0":
    
            threading.Thread(target = tru_so_tiet,args=(str(i.val()["MaLop"]),str(i.val()["MaMH"]) ,str(i.val()["PP_Giang"]) ,str(i.val()["Ca"]) ,)).start()
            db.child("ThoiKhoaBieu").child(i.key()).remove()
            return True



def tenlop_ma(ma):
    data=db.child("Lop").order_by_child("MaLop").equal_to(str(ma)).get()
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


# def kt_so_tiet_lt(malop,mamh,lt):
#     a=0
#     data=db.child("MonHoc").order_by_child("MaMH").equal_to(str(mamh)).get()
#     try:
#         for i in data.each():
#             if(i.val()["MaMH"]==str(mamh)):
#                 if lt== "lythuyet":
#                     a=i.val()["SoTietLiThuyet"]
#                 else:a=i.val()["SoTietThucHanh"]
#     except: a=[]
#     return a




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
def lop_maTKB(ma):
    e=""
    a=[]
    try:
        data = db.child("ThoiKhoaBieu").order_by_child('MaTKB').equal_to(str(ma)).get()
        for i in data.each():
            e=[i.val()['MaLop']]
            a.append(str(e))
    except:a=[]
    return a

