import conect_firebase


db=conect_firebase.connect().database()

def loadca(soca):
    data=db.child("CaHoc").get()
    for i in data.each():
        if(i.val()["TenCa"]==str(soca)):
            a=i.val()
    return a

def load_dl_tre():
    data=db.child("TGtre").get()
    return data

def luutre(tg):
    try:
        data=db.child("TGtre").set(str(tg))
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