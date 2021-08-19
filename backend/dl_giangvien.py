import conect_firebase

db=conect_firebase.connect().database()


def tengv_email(email):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["Email"]==email):
            a=i.val()["TenGV"]
    return a

def makhoa_email(email):
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["Email"]==str(email)):
            ma=i.val()["MaKhoa"]
    return ma

