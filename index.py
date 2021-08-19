import socket
# import diemdanhsv
# import dangnhap
# import csdl
# import admin_lop
import dangnhap
import  adminlop
import  diemdanh
import backend.xacthuc as xacthuc

def main():
    ten_thiet_bi = socket.gethostname()

    file=open(ten_thiet_bi+".txt","a")
    file.close()

    data=[]
    with open(ten_thiet_bi+".txt","r") as file:
        data= file.read().split("\n")
    if data[0] != "":
        if xacthuc.kt_loaitk(data[0]) == "1":
            adminlop.main()
        else:
            diemdanh.main()
    else:
        dangnhap.main()


if __name__ == '__main__':
    main()