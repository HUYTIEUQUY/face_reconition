from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import quantrivien_khoa
from backend.dl_giangvien import tengv_email,makhoa_email
from backend.dl_khoa import sl_khoa, tenkhoa
import backend.dl_khoa as khoa
import quantrivien_thongke
import quantrivien_khoa


def main():

    

    def menuthietlap():
        win.destroy()
        main()
    def menukhoa():
        win.destroy()
        quantrivien_khoa.main()

    def menuthongke():
        win.destroy()
        quantrivien_thongke.main()

    def menudangxuat():
        ten_thiet_bi = socket.gethostname()
        file=open(ten_thiet_bi+".txt","w")
        file.write("")
        file.close()
        win.destroy()
        dangnhap.main()

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img_qtv/bg_khoa.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_qtv/btn_dangxuat.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_qtv/menu_thongke.png")
    img_menuthietlap=ImageTk.PhotoImage(file="img_qtv/menu_thietlap1.png")
    img_menukhoa=ImageTk.PhotoImage(file="img_qtv/menu_khoa.png")
    img_btnthem=ImageTk.PhotoImage(file="img_qtv/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_qtv/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_qtv/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_qtv/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_qtv/btn_khoiphuc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    tenkhoa=StringVar()
    ndtimkiem=StringVar()
    makhoa = StringVar()
    tengv=tengv_email(d[0])
    row=khoa.bangkhoa()
        
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=30,y=212)
    menukhoa=Button(bg,image=img_menukhoa,bd=0,highlightthickness=0,command=menukhoa)
    menukhoa.place(x=30,y=128)
    menuthietlap=Button(bg,image=img_menuthietlap,bd=0,highlightthickness=0,command=menuthietlap)
    menuthietlap.place(x=30,y=296)

    
    win.mainloop()

if __name__ == '__main__':
    main()