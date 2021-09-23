import conect_firebase

auth=conect_firebase.connect().auth()
db=conect_firebase.connect().database()

def xacthuc(email,matkhau):
    try:
        auth.sign_in_with_email_and_password(email, matkhau)
        return True
    except:
        return False


def kt_loaitk(email):
    a=3
    try:
        data=db.child("GiangVien").order_by_child("Email").equal_to(str(email)).get()
        for i in data.each():
            a=i.val()['LoaiTK']
    except:a=3
    return a

