
import pickle

f=open("mahoa/Cong_nghe_thong_tin_K24_.pkl","rb")
tensv=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
f.close()

print(tensv)

# from backend.dl_diemdanh import test
# from backend.dl_tkb import ngaya_nhohon_ngayb

# # test(5)
# test()

# a=ngaya_nhohon_ngayb("24/12/2021","11/12/2021")
# print(a)
# print("11:00:00" < "10:59:00") 