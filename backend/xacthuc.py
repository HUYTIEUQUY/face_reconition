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
    data=db.child("GiangVien").get()
    for i in data.each():
        if(i.val()["Email"]==email):
            a=i.val()["LoaiTK"]
    return a

