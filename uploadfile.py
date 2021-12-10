import pyrebase
import urllib
import os
import pickle
from time import sleep


firebaseConfig = {
"apiKey": "AIzaSyC18JzwOtmxacPea2wH6V7epsMTCS1R7G0",
"authDomain": "facerecognition-30da4.firebaseapp.com",
"databaseURL": "https://facerecognition-30da4-default-rtdb.firebaseio.com",
"projectId": "facerecognition-30da4",
"storageBucket": "facerecognition-30da4.appspot.com",
"messagingSenderId": "207559290047",
"appId": "1:207559290047:web:577197cfe03736a9a86a0a",
"measurementId": "G-LREFTPNQ1E",
"serviceAccount": "facerecognition.json"
}
    
firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()





# storage.child("mahoa/Cong_nghe_thong_tin_K19_.pkl").download("mahoa/Cong_nghe_thong_tin_K19_.pkl","mahoa/Cong_nghe_thong_tin_K19_.pkl")




def upload_anh(masv):
    for i in range(5):
        pathlound=str(masv)+str(i+1)+".png"
        path = "img_anhsv/"+str(masv)+str(i+1)+".png"
        storage.child(pathlound).put(path)
    sleep(2)
    for i in range(5):
        pat=str(masv)+str(i+1)+".png"
        os.remove("img_anhsv/"+pat)

def upload_filemahoa(path):
    try:
        storage.child(path).put(path)
    except: print("Lỗi upload file mahoa" + path)

def download_filemahoa(tenlop):
    tenlop=tenlop.replace(" ","_")
    pathten="mahoa/"+tenlop+".pkl"
    path="mahoa/"+tenlop+"mahoa.pkl"
    
    storage.child(pathten).download(pathten,pathten)
    storage.child(path).download(path,path)
    


# def capnhatanh(makhoa):
#     all_files = storage.list_files()
#     foder = "khoa"+str(makhoa)
#     for file in all_files:
#         if foder in file.name:
#             tenanh = str(file.name).replace("khoa"+str(makhoa)+"/","")
#             file.download_to_filename("img_anhsv/"+tenanh)

def deleteanh(masv):
    for i in range(5):
        pathlound=str(masv)+str(i+1)+".png"
        try:
            a=storage.child(pathlound).get_url(None)
            storage.delete(pathlound,a)
        except: return


def load(tenfile_loud):
    a=storage.child(tenfile_loud).get_url(None)
    f = urllib.request.urlopen(a)
    return f

# pathten="mahoa/Cong_nghe_thong_tin_K22_.pkl"
# a=storage.child(pathten).get_url(None)
# storage.child(pathten).download(pathten,pathten,None)
# # # f = urllib.request.urlopen(a).read()
# f=open("mahoa/Cong_nghe_thong_tin_K20_mahoa.pkl","rb")
# ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
# f.close()
# print(ref_dictt)






# all_files = storage.list_files()

