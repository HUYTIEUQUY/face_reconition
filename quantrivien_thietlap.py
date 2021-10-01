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
from datetime import datetime, timedelta

def main():
    def luong(ham):
        threading.Thread(target=ham).start()
    def luu():
        tgbd=str(giobd.get())+":"+str(phutbd.get())+":"+str(giaybd.get())
        tgkt=str(giokt.get())+":"+str(phutkt.get())+":"+str(giaykt.get())
        
        if str(giobd.get()) =="00" or str(giokt.get()) == "00" or str(giobd.get()) == str(giokt.get()):
            messagebox.showwarning("thông báo","Thời gian ca chưa họp lý")
        else:
            lca=thietlap.luuca(ca.get(),tgbd,tgkt)
            if lca==True:
                messagebox.showinfo("Thông báo","Đã lưu")
            else:
                messagebox.showerror("Thông báo","Lỗi lưu thời gian")

    
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
        format = '%H:%M:%S'
        stiet=datetime.strptime(a['TGKT'], format) - datetime.strptime(a['TGBD'], format)
        stiet=str(stiet).split(':')
        so=(int(stiet[0])*60+int(stiet[1]))/50
        sotiet.set(int(so))
    def mang(so):
        a=[]
        for i in range(so):
            if len(str(i))==1:
                i="0"+str(i)
            a.append(i)
        return a

    def capnhattgkt(event):
        st= int(sotiet.get())*50
        tgbd=str(giobd.get())+":"+str(phutbd.get())+":"+str(giaybd.get())
        format = '%H:%M:%S'
        d =datetime.strptime(tgbd, format)  + timedelta(minutes=int(st))
        tgkt=d.strftime('%H:%M:%S').split(":")
        giokt.set(tgkt[0])
        phutkt.set(tgkt[1])
        giaykt.set(tgkt[2])

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
    win.title("Thiết lập")
    img_bg=ImageTk.PhotoImage(file="img_qtv/bg_thietdat.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_qtv/btn_dangxuat.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_qtv/menu_thongke.png")
    img_menuthietlap=ImageTk.PhotoImage(file="img_qtv/menu_thietlap1.png")
    img_menukhoa=ImageTk.PhotoImage(file="img_qtv/menu_khoa.png")
    img_btnluu=ImageTk.PhotoImage(file="img_qtv/btn_luuthietdat.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    tengv=tengv_email(d[0])
    ca=StringVar()
    sotiet=StringVar()
    giobd=StringVar()
    phutbd=StringVar()
    giaybd=StringVar()
    giokt=StringVar()
    phutkt=StringVar()
    giaykt=StringVar()

    vl_sotiet=[2,3]
    vl_ca=[1,2,3,4,5]
    gio=["07",'08','09','10','11','12','13','14','15','16','17']
    phut_giay=mang(60)
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=30,y=212)
    menukhoa=Button(bg,image=img_menukhoa,bd=0,highlightthickness=0,activebackground='#857EBD',command=menukhoa)
    menukhoa.place(x=30,y=128)
    menuthietlap=Button(bg,image=img_menuthietlap,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthietlap)
    menuthietlap.place(x=30,y=296)

    Label(bg,text=tengv,font=("Baloo Tamma 2 Medium",13),fg="#A672BB",bg="white").place(x=45,y=38)

    
    cb_ca=Combobox(bg,textvariable=ca,values=vl_ca,font=("Digital-7",14),width=2)
    cb_ca.current(0)
    cb_ca.bind('<<ComboboxSelected>>', capnhatca)
    cb_ca.place(x=430,y=130)

    cb_sotiet=Combobox(bg,textvariable=sotiet,values=vl_sotiet,font=("Digital-7",14),width=2)
    cb_sotiet.bind('<<ComboboxSelected>>', capnhattgkt)
    cb_sotiet.current(0)
    cb_sotiet.place(x=750,y=130)

    cb_giobd=Combobox(bg,textvariable=giobd,values=gio,font=("Digital-7",14),state='readonly',width=2)
    cb_giobd.place(x=648,y=234)
    cb_giobd.bind('<<ComboboxSelected>>', capnhattgkt)
    cb_phutbd=Combobox(bg,textvariable=phutbd,values=phut_giay,font=("Digital-7",14),state='readonly',width=2)
    cb_phutbd.place(x=709,y=234)
    cb_phutbd.bind('<<ComboboxSelected>>', capnhattgkt)
    cb_giaybd=Combobox(bg,textvariable=giaybd,values=phut_giay,font=("Digital-7",14),state='readonly',width=2)
    cb_giaybd.place(x=769,y=234)
    cb_giaybd.bind('<<ComboboxSelected>>', capnhattgkt)


    cb_giokt=Combobox(bg,textvariable=giokt,font=("Digital-7",14),state='readonly',width=2)
    cb_giokt.place(x=648,y=319)
    
    cb_phutkt=Combobox(bg,textvariable=phutkt,font=("Digital-7",14),state='readonly',width=2)
    cb_phutkt.place(x=709,y=319)
    
    cb_giaykt=Combobox(bg,textvariable=giaykt,font=("Digital-7",14),state='readonly',width=2)
    cb_giaykt.place(x=769,y=319)
   

    btnkhoiphuc=Button(bg,image=img_btnluu,bd=0,highlightthickness=0,command=luu,bg="white")
    btnkhoiphuc.place(x=582,y=488)



    luong(loaddl)
    win.mainloop()

if __name__ == '__main__':
    main()