import conect_firebase

auth=conect_firebase.connect().auth()
db=conect_firebase.connect().database()
from datetime import datetime

def gv_dd(magv,ngay):
    a=[]
    data=db.child("ThoiKhoaBieu").get()
    try:
        for i in data.each():
            if(i.val()["MaGV"]==str(magv) and i.val()["Ngay"] < str(ngay) and i.val()["TrangThaiDD"] =='0' ):
                e = [i.val()['MaLop'],i.val()['MaMH'],i.val()['Ngay'],i.val()['Ca']]
                a.append(e)
    except: a=[]
    return a

# print(gv_dd('222222','03/09/2021'))



def sosanhngay(a,b):
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

