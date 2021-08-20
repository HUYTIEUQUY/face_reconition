import conect_firebase

db=conect_firebase.connect().database()



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
            if(i.val()["TenMH"]==str(ten)):
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
    data=db.child("MonHoc").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            e=[str(stt),i.val()["MaMH"],i.val()["TenMH"],i.val()["SoTietLyThuyet"],i.val()["SoTietThucHanh"]]
            a.append(e)
            stt=stt+1
        
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
    data=db.child("MonHoc").get()
    for i in data.each():
        if(i.val()["MaMH"]==str(mamh)):
            try:
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
    data=db.child("MonHoc").get()
    a=""
    for i in data.each():
        if(i.val()["MaMH"]==str(ma)):
            a=(i.val()["TenMH"])
    return a