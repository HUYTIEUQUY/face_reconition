import conect_firebase

db=conect_firebase.connect().database()


def banglop(makhoa):
    a=[]
    stt=1
    data=db.child("Lop").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==makhoa):
            e=[stt,i.val()["MaLop"],i.val()["TenLop"]]
            a.append(e)
        stt=stt+1
    return a

def themlop(malop,tenlop,makhoa):
    data={'MaLop':malop,'TenLop':tenlop,'MaKhoa':makhoa}
    try:
        db.child('Lop').push(data)
        return True
    except:
        return False

def sualop(malop,tenlop):
    data=db.child("Lop").get()
    dl={'TenLop':tenlop}
    for i in data.each():
        if(i.val()["MaLop"]==str(malop)):
            try:
                db.child("Lop").child(i.key()).update(dl)
                return True
            except:
                return False

def xoalop(malop):
    data=db.child("Lop").get()
    for i in data.each():
        if(i.val()["MaLop"]==str(malop)):
            try:
                db.child("Lop").child(i.key()).remove()
                return True
            except:
                return False
    
def kt_tenlop(tenlop):
    data=db.child("Lop").get()
    for i in data.each():
        if(i.val()["TenLop"]==str(tenlop)):
            return True
        else:
            return False


