from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk
# import csdl
from tkinter import messagebox
import socket
# import diemdanhsv
import mysql.connector
# import admin_lop
import hashlib
import backend.xacthuc as xacthuc
import adminlop
import diemdanh
import quantrivien_khoa



def main():
    
    def hien():
        if txtPass["show"]=="*":
            txtPass["show"]=""
        else:
            txtPass["show"]="*"


    def kt_dangnhap(email,passw):
        if email=="" or passw=="":
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
            return False
        elif len(passw)<6:
            messagebox.showwarning("thông báo","Vui lòng kiểm tra lại mật khẩu")
            return False
        elif xacthuc.xacthuc(email,passw)==False:
             messagebox.showerror("Thông báo","Đăng nhập không thành công")
             return False
        else:
            return True


    def dangnhap():
        email=data_e.get()
        passw=data_p.get()

        if kt_dangnhap(email, passw) == True:
            ten_thiet_bi = socket.gethostname()
            with open(ten_thiet_bi+".txt","w") as file:
                file.write(email+"\n")
                file.write(passw)

            if xacthuc.kt_loaitk(email) == "1":
                win.destroy()
                adminlop.main()
            if xacthuc.kt_loaitk(email) == "2":
                win.destroy()
                quantrivien_khoa.main()
            else:
                win.destroy()
                diemdanh.main()
        else: return
        if xacthuc.xacthuc(email,passw)== True:
            return
        else:
            messagebox.showinfo("thông báo","Đăng nhập thất bại")
        

    win=Tk()
    win.geometry("600x600+400+100")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img/bg_dagnhap.png")

    img_btn=ImageTk.PhotoImage(file=f"img/buttonDN.png")

    img_btnhien=ImageTk.PhotoImage(file="img/img_btnhien.png")

    bg=Canvas(win,width=600,height=600,bg="green")
    bg.pack(side="left",padx=0)


    anhnen=bg.create_image(300,300,image=img_bg)
    data_e=StringVar()
    txtEmail=Entry(bg,width=22,font=("Baloo Tamma",12),bd=0,textvariable=data_e)
    txtEmail.place(x=200,y=248)

    data_p=StringVar()
    txtPass=Entry(bg,width=22,font=("Baloo Tamma",12), bd=0, show="*", textvariable=data_p)
    txtPass.place(x=200,y=346)


    btn=Button(bg,image=img_btn,bd=0,borderwidth=0, highlightthickness=0,relief="flat",command=dangnhap)
    btn.place(x=231,y=494)
    btnhien=Button(bg,image=img_btnhien,bd=0,highlightthickness=0,command=hien)
    btnhien.place(x=428,y=345)
    win.mainloop()

if __name__ == '__main__':
    main()