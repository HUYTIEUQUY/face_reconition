import conect_firebase
import re
db=conect_firebase.connect().database()

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

def kt_ma_tt(ma):
    data=db.child("MonHoc").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["MaMH"]==str(ma)):
                a.append(i.val())
    except:
        a=[]
    return a

def kt_ten_tt(ten):
    data=db.child("MonHoc").get()
    a=[]
    try:
        for i in data.each():
            if(i.val()["TenMH"].lower()==str(ten).lower()):
                a.append(i.val()["MaMH"])
    except:
        a=[]
    return a


def themmh(mamh,tenmh,lt,th,makhoa):
    data={'MaMH':str(mamh),'TenMH':str(tenmh),'SoTietLyThuyet':str(lt),'SoTietThucHanh':str(th),'MaKhoa':str(makhoa)}
    try:
        db.child('MonHoc').push(data)
        return True
    except:
        return False
   

def bangmh(makhoa):
    a=[]
    stt=1
    try:
        data=db.child("MonHoc").get()
        for i in data.each():
            if(i.val()["MaKhoa"]==str(makhoa)):
                e=[str(stt),i.val()["MaMH"],i.val()["TenMH"],i.val()["SoTietLyThuyet"],i.val()["SoTietThucHanh"]]
                a.append(e)
                stt=stt+1
    except:a=[]
    return a

def suamh(mamh,tenmh,lt,th):
    data=db.child("MonHoc").get()
    dl={'TenMH':str(tenmh),'SoTietLyThuyet':str(lt),'SoTietThucHanh':str(th)}
    for i in data.each():
        if(i.val()["MaMH"]==str(mamh)):
            try:
                db.child("MonHoc").child(i.key()).update(dl)
                return True
            except:
                return False

def xoamh(mamh):
    try:
        data=db.child("MonHoc").order_by_child("MaMH").equal_to(str(mamh)).get()
        for i in data.each():
            if(i.val()["MaMH"]==str(mamh)):
                db.child("MonHoc").child(i.key()).remove()
                return True
    except:
        return False

def mamh_ten(ten):
    data=db.child("MonHoc").get()
    a=""
    for i in data.each():
        if(i.val()["TenMH"]==str(ten)):
            a=(i.val()["MaMH"])
    return a


def tenmh_ma(ma):
    data=db.child("MonHoc").order_by_child('MaMH').equal_to(str(ma)).get()
    a=""
    for i in data.each():
        if(i.val()["MaMH"]==str(ma)):
            a=(i.val()["TenMH"])
    return a

def tim_mh(makhoa,q):
    a=[]
    stt=1
    data=db.child("MonHoc").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            e=[str(stt),i.val()["MaMH"],i.val()["TenMH"],i.val()["SoTietLyThuyet"],i.val()["SoTietThucHanh"]]
            if str(q) in khong_dau(i.val()["MaMH"].lower()) or str(q) in khong_dau(i.val()["TenMH"].lower()) or str(q) in khong_dau(i.val()["SoTietLyThuyet"].lower()) or str(q) in khong_dau(i.val()["SoTietThucHanh"].lower()):
                a.append(e)
            stt=stt+1
    return a

def kt_monhoc_tontai_diemdanh(ma):
    data=db.child("DiemDanh").get()
    a=[]
    for i in data.each():
        if(i.val()["MaMH"]==str(ma)):
            a.append(i.val()['MaMH'])
    return a
def kt_monhoc_tontai_tkb(ma):
    data=db.child("ThoiKhoaBieu").get()
    a=[]
    for i in data.each():
        if(i.val()["MaMH"]==str(ma)):
            a.append(i.val()['MaMH'])
    return a