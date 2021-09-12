import conect_firebase


db=conect_firebase.connect().database()

def loadca(soca):
    data=db.child("CaHoc").get()
    for i in data.each():
        if(i.val()["TenCa"]==str(soca)):
            a=i.val()
    return a

def load_dl_tre(ma):
    a=""
    try:
        data=db.child("tgtre").child(ma).get()
        a= data.val()['thoigian']
    except: a=""
    return a

def luutre(ma,tg):
    data={'thoigian':str(tg)}
    try:
        db.child("tgtre").child(ma).set(data)
        return True
    except:
        return False

def luuca(ca,tgbd,tgkt):
    data=db.child("CaHoc").get()
    dl={'TGBD':str(tgbd),'TGKT':str(tgkt)}
    for i in data.each():
        if(i.val()["TenCa"]==str(ca)):
            try:
                db.child("CaHoc").child(i.key()).update(dl)
                return True
            except:
                return False