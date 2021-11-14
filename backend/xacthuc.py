import conect_firebase
try:
    auth=conect_firebase.connect().auth()
    db=conect_firebase.connect().database()
except: print("Không có kết nối mạng")
def xacthuc(email,matkhau):
    try:
        tk=auth.sign_in_with_email_and_password(email, matkhau)
        return True
    except:
        return False


def kt_loaitk(email):
    a=3
    try:
        data=db.child("GiangVien").order_by_child("Email").equal_to(str(email)).get()
        for i in data.each():
            if i.val()['Email'] == str(email):
                a=i.val()['LoaiTK']
    except:a=3
    return a

def them_ma_xacnhan(email,ma):
    try:
        data={'Email':str(email), 'MaXN':str(ma)}
        db.child('MaXacNhan').push(data)
        return True
    except:
        return False
def kt_ma_xacnhan(email,ma):
    a=""

    data=db.child("MaXacNhan").order_by_child("MaXN").equal_to(str(ma)).get()
    for i in data.each():
        if i.val()['MaXN'] == str(ma) and i.val()['Email'] == str(email):
            a = i.val()['Email']
    return a


def xoa_ma_xacnhan(e):
    data=db.child("MaXacNhan").order_by_child("Email").equal_to(str(e)).get()
    for i in data.each():
        if(i.val()["Email"]==str(e)):
            try:
                db.child("MaXacNhan").child(i.key()).remove()
                return True
            except:
                return False

