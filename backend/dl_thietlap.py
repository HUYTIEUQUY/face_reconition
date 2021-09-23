import conect_firebase


db=conect_firebase.connect().database()

def loadca(soca):
    a={'TGBD':"00:00:00",'TGKT':"00:00:00"}
    try:
        data=db.child("CaHoc").order_by_child("TenCa").equal_to(str(soca)).get()
        for i in data.each():
            if(i.val()["TenCa"]==str(soca)):
                a=i.val()

    except:a={'TGBD':"00:00:00",'TGKT':"00:00:00"}
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
    dl={'TenCa':str(ca),'TGBD':str(tgbd),'TGKT':str(tgkt)}
    try:
        for i in data.each():
            if(i.val()["TenCa"]==str(ca)):
                    db.child("CaHoc").child(i.key()).update(dl)
                    return True
            else:
                db.child("CaHoc").push(dl)
                return True
    except:
        if db.child("CaHoc").push(dl):
            return True
        else:return False