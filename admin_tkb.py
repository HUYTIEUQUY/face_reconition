from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import adminlop
import admin_giangvien
import admin_thongke
import admin_monhoc
from backend.dl_giangvien import tengv_email



def main():
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menulophoc():
        win.destroy()
        adminlop.main()
    def menugiangvien():
        win.destroy()
        admin_giangvien.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
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
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_tkb.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb1.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    img_btnchonlich=ImageTk.PhotoImage(file="img_admin/chonlich.png")
    img_btntrolai=ImageTk.PhotoImage(file="img_admin/btn_trolai.png")
    img_btnchon=ImageTk.PhotoImage(file="img_admin/btn_chon.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    # makhoa=csdl.makhoa_tu_email(email)
    tenlop=StringVar()
    malop=StringVar()
    ndtimkiem=StringVar()
    tengv=tengv_email(d[0])
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,compound=LEFT,command=menulophoc)
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,command=menugiangvien)
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=30,y=461)

    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    win.mainloop()

if __name__ == '__main__':
    main()