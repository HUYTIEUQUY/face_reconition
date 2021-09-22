from logging import RootLogger
import conect_firebase


import glob
db=conect_firebase.connect().storage()

# for name in glob.glob('img_anhsv/*.png',recursive=False):
#     tenfile = str(name).replace("img_anhsv"," ")[2:]
#     thumuc = name[0:9]
#     db.child(thumuc+"/"+tenfile).put(name)
    
    # print(db.child(thumuc+"/"+tenfile).get_url(None))

allfile = db.list_files()
for i in allfile:
    print(i.name)



