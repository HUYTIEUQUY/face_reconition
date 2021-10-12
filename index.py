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

def main():
    def taifilemahoa(makhoa):
        lop=lop_khoa(makhoa)
        for i in lop:
            tenlop=khong_dau(i)
            download_filemahoa(tenlop)
    
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