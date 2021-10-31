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
            a=i.val()['LoaiTK']
    except:a=3
    return a

