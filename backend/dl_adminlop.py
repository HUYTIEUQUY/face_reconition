import conect_firebase

db=conect_firebase.connect().database()


def banglop(makhoa):
    a=[]
    stt=1
    data=db.child("Lop").get()
    for i in data.each():
        if(i.val()["MaKhoa"]==str(makhoa)):
            e=[str(stt),i.val()["MaLop"],i.val()["TenLop"]]
            a.append(e)
            stt=stt+1
        
    return a

def themlop(malop,tenlop,makhoa):
    data={'MaLop':str(malop),'TenLop':tenlop,'MaKhoa':str(makhoa)}
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
    a=[]
    for i in data.each():
        if(i.val()["TenLop"]==str(tenlop)):
            a.append(i.val())
    return a


def malop_ten(tenlop):
    data=db.child("Lop").get()
    a=""
    for i in data.each():
        if(i.val()["TenLop"]==str(tenlop)):
            a=(i.val()["MaLop"])
    return a

# def timlop(makhoa,q):
#     a=banglop(makhoa)
#     b=[]
#     for i in a: 
#         for j in i:
#             if j.find(str(q)) != -1:
#                 if i not in b:
#                     b.append(i)
#     return b


