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
import doimatkhau



def main():

    def doimk():
        win.destroy()
        doimatkhau.main(0)
    
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
            if xacthuc.xacthuc(email,passw)== True:
                if xacthuc.kt_loaitk(email) == "1":
                    win.destroy()
                    adminlop.main()
                elif xacthuc.kt_loaitk(email) == "0":
                    win.destroy()
                    diemdanh.main()
                elif xacthuc.kt_loaitk(email) == "3":
                    messagebox.showinfo("thông báo","Tài khoản không tồn tại")
                else:
                    win.destroy()
                    quantrivien_khoa.main()
            else:
                messagebox.showinfo("thông báo","Đăng nhập thất bại")
        
        
        

    win=Tk()
    win.geometry("600x600+400+100")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img/bg_dagnhap.png")

    img_btn=ImageTk.PhotoImage(file=f"img/buttonDN.png")

    img_btnhien=ImageTk.PhotoImage(file="img/img_btnhienmk.png")
    img_lb_doimatkhau=ImageTk.PhotoImage(file="img/lb_doimatkhau.png")

    bg=Canvas(win,width=600,height=600,bg="green")
    bg.pack(side="left",padx=0)


    anhnen=bg.create_image(300,300,image=img_bg)
    data_e=StringVar()
    txtEmail=Entry(bg,width=23,font=("Baloo Tamma",12),bd=0,textvariable=data_e)
    txtEmail.place(x=234,y=233)

    data_p=StringVar()
    txtPass=Entry(bg,width=22,font=("Baloo Tamma",12), bd=0, show="*", textvariable=data_p)
    txtPass.place(x=240,y=291)

    lb_doimatkhau=Button(bg,image=img_lb_doimatkhau,bd=0, highlightthickness=0,activebackground="#BCA8E6",relief=RIDGE,command=doimk)
    lb_doimatkhau.place(x=231,y=440)


    btn=Button(bg,image=img_btn,bd=0,borderwidth=0, highlightthickness=0,activebackground="#BFAAE5",command=dangnhap)
    btn.place(x=231,y=494)
    btnhien=Button(bg,image=img_btnhien,bd=0,highlightthickness=0,command=hien)
    btnhien.place(x=428,y=290)
    win.mainloop()

if __name__ == '__main__':
    main()