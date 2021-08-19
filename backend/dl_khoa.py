import conect_firebase

db=conect_firebase.connect().database()


def tenkhoa(makhoa):
    data=db.child("Khoa").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            ten=i.val()["TenKhoa"]
    return ten