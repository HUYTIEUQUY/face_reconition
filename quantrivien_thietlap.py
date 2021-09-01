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
import backend.dl_thietlap as thietlap
import quantrivien_thongke
import quantrivien_khoa
import threading

def main():
    def luong(ham):
        threading.Thread(target=ham).start()
    def luu():
        tgbd=str(giobd.get())+":"+str(phutbd.get())+":"+str(giaybd.get())
        tgkt=str(giokt.get())+":"+str(phutkt.get())+":"+str(giaykt.get())
        tgtre=str(giotre.get())+":"+str(phuttre.get())+":"+str(giaytre.get())
        lca=thietlap.luuca(ca.get(),tgbd,tgkt)
        ltre=thietlap.luutre(tgtre)
        if lca==True and ltre==True:
            messagebox.showinfo("Thông báo","Đã lưu")
        else:
            messagebox.showerror("Thông báo","Lỗi")
    def load_dl_tre():
        a=thietlap.load_dl_tre().val().replace(':'," ").split()
        giotre.set(a[0])
        phuttre.set(a[1])
        giaytre.set(a[2])
    
    def capnhatca(event):
        loaddl()

    def loaddl():
        a=thietlap.loadca(ca.get())
        
        tgbd=str(a['TGBD']).replace(':'," ").split()
        giobd.set(tgbd[0])
        phutbd.set(tgbd[1])
        giaybd.set(tgbd[2])

        tgkt=str(a['TGKT']).replace(':'," ").split()
        giokt.set(tgkt[0])
        phutkt.set(tgkt[1])
        giaykt.set(tgkt[2])
        
    def mang(so):
        a=[]
        for i in range(so):
            if len(str(i))==1:
                i="0"+str(i)
            a.append(i)
        return a
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
    img_bg=ImageTk.PhotoImage(file="img_qtv/bg_thietdat.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_qtv/btn_dangxuat.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_qtv/menu_thongke.png")
    img_menuthietlap=ImageTk.PhotoImage(file="img_qtv/menu_thietlap1.png")
    img_menukhoa=ImageTk.PhotoImage(file="img_qtv/menu_khoa.png")
    img_btnthem=ImageTk.PhotoImage(file="img_qtv/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_qtv/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_qtv/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_qtv/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_qtv/btn_khoiphuc.png")
    img_btnluu=ImageTk.PhotoImage(file="img_qtv/btn_luuthietdat.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    tenkhoa=StringVar()
    ndtimkiem=StringVar()
    makhoa = StringVar()
    tengv=tengv_email(d[0])
    
    ca=StringVar()
    giobd=StringVar()
    phutbd=StringVar()
    giaybd=StringVar()
    giokt=StringVar()
    phutkt=StringVar()
    giaykt=StringVar()

    giotre=StringVar()
    phuttre=StringVar()
    giaytre=StringVar()
    vl_ca=[1,2,3,4]
    gio=mang(24)
    phut_giay=mang(60)
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

    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    
    cb_ca=Combobox(bg,textvariable=ca,values=vl_ca,font=("Baloo Tamma",12),width=2)
    cb_ca.current(0)
    cb_ca.bind('<<ComboboxSelected>>', capnhatca)
    cb_ca.place(x=430,y=135)

    cb_giobd=Combobox(bg,textvariable=giobd,values=gio,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giobd.place(x=577,y=165)
    cb_phutbd=Combobox(bg,textvariable=phutbd,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_phutbd.place(x=638,y=165)
    cb_giaybd=Combobox(bg,textvariable=giaybd,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giaybd.place(x=698,y=165)


    cb_giokt=Combobox(bg,textvariable=giokt,values=gio,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giokt.place(x=577,y=217)
    cb_phutkt=Combobox(bg,textvariable=phutkt,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_phutkt.place(x=638,y=217)
    cb_giaykt=Combobox(bg,textvariable=giaykt,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giaykt.place(x=698,y=217)


    cb_giotre=Combobox(bg,textvariable=giotre,values=gio,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giotre.place(x=577,y=347)
    cb_phuttre=Combobox(bg,textvariable=phuttre,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_phuttre.place(x=638,y=347)
    cb_giaytre=Combobox(bg,textvariable=giaytre,values=phut_giay,font=("Baloo Tamma",12),state='readonly',width=2)
    cb_giaytre.place(x=698,y=347)

    btnkhoiphuc=Button(bg,image=img_btnluu,bd=0,highlightthickness=0,command=luu,bg="white")
    btnkhoiphuc.place(x=582,y=488)



    luong(loaddl)
    luong(load_dl_tre)
    win.mainloop()

if __name__ == '__main__':
    main()