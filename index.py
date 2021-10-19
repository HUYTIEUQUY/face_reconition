import socket
import dangnhap
import  adminlop
import  diemdanh
import quantrivien_khoa
from backend.dl_giangvien import makhoa_email
import backend.xacthuc as xacthuc
from uploadfile import download_filemahoa
from backend.dl_sinhvien import lop_khoa
from kt_nhap import khong_dau
from backend.dl_giangvien import makhoa_email
from backend.dl_khoa import khoa_co_quyen_all
from backend.dl_tkb import all_lop
from backend.dl_diemdanh import tra_dl_diemdanh
import datetime
import threading

def main():
    def taifilemahoa(makhoa):
        quyen = khoa_co_quyen_all(makhoa)
        if quyen == str(1):
            lop=all_lop()
        else:
            lop=lop_khoa(makhoa)
        for i in lop:
                tenlop=khong_dau(i)
                threading.Thread(target=download_filemahoa,args=(tenlop,)).start()
    #Ngày hiện tại
    day = str(datetime.date.today()).split("-")
    ngayhientai = str(day[2])+"/"+str(day[1])+"/"+str(day[0])
    threading.Thread(target=tra_dl_diemdanh,args=(ngayhientai,)).start()


    ten_thiet_bi = socket.gethostname()
    file=open(ten_thiet_bi+".txt","a")
    file.close()
    data=[]
    with open(ten_thiet_bi+".txt","r") as file:
        data= file.read().split("\n")
    if data[0] != "":
        if xacthuc.kt_loaitk(data[0]) == "1":
            adminlop.main()
        elif xacthuc.kt_loaitk(data[0]) == "0":
            makhoa=makhoa_email(data[0])
            taifilemahoa(makhoa)
            diemdanh.main()
        else:
            quantrivien_khoa.main()
    else:
        dangnhap.main()


if __name__ == '__main__':
    main()