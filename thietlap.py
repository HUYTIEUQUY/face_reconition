from tkinter import *
from tkinter.ttk import Combobox
from tkinter import PhotoImage
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import sinhvien
import thongke
import taikhoan
import diemdanh
from backend.dl_giangvien import tengv_email,magv_email
import threading
import backend.dl_thietlap as thietlap


def main():

    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        tengv.set(tengv_email(d[0]))
        magv.set(magv_email(d[0]))
        a=thietlap.load_dl_tre(magv.get())
        print(a)
        if a== "":
            phuttre.set("00")
            giaytre.set("00")
        else:
            a=a.replace(':'," ").split()
            phuttre.set(a[0])
            giaytre.set(a[1])


    def luu():
        tgtre=str(phuttre.get())+":"+str(giaytre.get())
        ltre=thietlap.luutre(magv.get(),tgtre)
        if ltre==True:
            messagebox.showinfo("Thông báo","Đã lưu")
        else:
            messagebox.showerror("Thông báo","Lỗi")

    def mang(so):
        a=[]
        for i in range(so):
            if len(str(i))==1:
                i="0"+str(i)
            a.append(i)
        return a
            
    def menutaikhoan():
        win.destroy()
        taikhoan.main()
    def menudiemdanh():
        win.destroy()
        diemdanh.main()

    def menuthongke():
        win.destroy()
        thongke.main()

    def menuthemsv():
        win.destroy()
        sinhvien.main()

    def dangxuat():
        if messagebox.askyesno("Thông báo","Bạn có thực sự muốn đăng xuất ?"):
            ten_thiet_bi = socket.gethostname()
            file=open(ten_thiet_bi+".txt","w")
            file.write("")
            file.close()
            win.destroy()
            dangnhap.main()
        else: return

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Điểm danh sinh viên")
    img_bg=ImageTk.PhotoImage(file="img/bg_thietlaptre.png")
    
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh1.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/btn_trolai.png")
    img_btnluu=ImageTk.PhotoImage(file="img_qtv/btn_luuthietdat.png")
    
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudd=Button(bg,image=ing_menudiemdanh,bd=0,activebackground='#857EBD',highlightthickness=0)
    menudd.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD', command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD', command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)
#_______________________________________________________________________________________________________________________________
    
    #dữ liệu hiện lớp, môn
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=StringVar()
    tengv=StringVar()
    magv=StringVar()
    phuttre=StringVar()
    giaytre=StringVar()
    phut_giay=mang(60)

    lbgv=Label(bg,textvariable=tengv, font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    btntrolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=menudiemdanh)
    btntrolai.place(x=948,y=2)


    cb_phuttre=Combobox(bg,textvariable=phuttre,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_phuttre.place(x=594,y=153)
    cb_giaytre=Combobox(bg,textvariable=giaytre,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giaytre.place(x=681,y=151)

    btnluu=Button(bg,image=img_btnluu,bd=0,highlightthickness=0,command=luu,bg="white")
    btnluu.place(x=582,y=488)

    luong(loaddl)
    win.mainloop()

if __name__ == '__main__':
    main()