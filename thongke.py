from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import sinhvien
import diemdanh
import taikhoan


def main():
    # def timkiem():
    #     q=data.get()
    #     mamh1 = csdl.tenmon_thanh_ma(str(mamh.get()))
    #     ngay1=str(ngay.get())
    #     ca1=str(ca.get())
    #     row=csdl.timkiem_diemdanh(magv,ngay1,mamh1,malop,ca.get(),q)
    #     update(row)
    # def reset():
    #     win.destroy()
    #     main()
    # def chon3(cbngay,mamh):
    #     ngay=cbngay.get()
    #     cbngay.destroy()
    #     Label(f3,text=ngay,font=("Baloo Tamma",12),bg="white").pack()
    #     anhnen=bg.create_image(500,300,image=img_bg3)
    #     data_ca=csdl.tim_ca_trong_diemdanh(magv,malop,mamh,ngay)
    #     cb_ca=Combobox(f4,width=2,values=data_ca, font=("Baloo Tamma",12),textvariable=ca)
    #     cb_ca.current(0)
    #     cb_ca.pack()
    #     btnchon.config(image=ing_btnxemthongke, command=lambda:batdauthongke(cb_ca))
    # def chon2(cbmon):
    #     tenmon=cbmon.get()
    #     cbmon.destroy()
    #     Label(f2,text=tenmon,font=("Baloo Tamma",12),bg="white").pack()
    #     anhnen=bg.create_image(500,300,image=img_bg2)
    #     mamh1 = csdl.tenmon_thanh_ma(str(mamh.get()))
    #     data_ngay=csdl.tim_ngay_trong_diemdanh(magv,malop,mamh1)
    #     cb_ngay=Combobox(f3,width=9,values=data_ngay, font=("Baloo Tamma",12),textvariable=ngay)
    #     cb_ngay.current(0)
    #     cb_ngay.pack()
    #     btnchon.config(command=lambda:chon3(cb_ngay,mamh1))
    # def chon1():
    #     tenlop=cb_lop.get()
    #     cb_lop.destroy()
    #     Label(f1,text=tenlop,font=("Baloo Tamma",12),bg="white").pack()
    #     anhnen=bg.create_image(500,300,image=img_bg1)
    #     data_mon=csdl.tim_mon_trong_diemdanh(magv,malop)
    #     cb_mon=Combobox(f2,width=20,values=data_mon, font=("Baloo Tamma",12),textvariable=mamh)
    #     cb_mon.current(0)
    #     cb_mon.pack()
        
    #     btnchon.config(command=lambda:chon2(cb_mon))
    #     btnchonlai=Button(bg,image=ing_chonlai,bd=0,highlightthickness=0,command=reset)
    #     btnchonlai.place(x=869,y=207)
    # def update(row):
    #     tv.delete(*tv.get_children())
    #     for i in row:
    #         tv.insert('','end',values=i)

    # def batdauthongke(cbca):
    #     cbca.destroy()
    #     Label(f4,text=ca.get(),font=("Baloo Tamma",12),bg="white").pack()
    #     mamh1 = csdl.tenmon_thanh_ma(str(mamh.get()))
    #     ngay1=str(ngay.get())
    #     ca1=str(ca.get())
    #     row = csdl.thongke(magv,ngay1,mamh1, malop ,ca1)
    #     update(row)
        
    #     btntimkiem=Button(bg,image=ing_timkiem,bd=0,highlightthickness=0,command=timkiem)
    #     btntimkiem.place(x=800,y=520)
    #     Entry(bg,font=("Baloo Tamma",12),width=35,bd=0,highlightthickness=0,textvariable=data).place(x=474,y=515)
    def menutaikhoan():
        win.destroy()
        taikhoan.main()

    def menudiemdanh():
        win.destroy()
        diemdanh.main()

    def menuthemsv():
        win.destroy()
        sinhvien.main()
    def dangxuat():
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
    img_bg=ImageTk.PhotoImage(file="img/thongke1.png")
    img_bg1=ImageTk.PhotoImage(file="img/thongke2.png")
    img_bg2=ImageTk.PhotoImage(file="img/thongke3.png")
    img_bg3=ImageTk.PhotoImage(file="img/thongke4.png")
    img_erorr=ImageTk.PhotoImage(file="img/bg_thongke_erorr.png")
    
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke1.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btnxemthongke=ImageTk.PhotoImage(file="img/btn_xemthongke.png")
    ing_chon=ImageTk.PhotoImage(file="img/btnchon.png")
    ing_chonlai=ImageTk.PhotoImage(file="img/chonlai.png")
    ing_timkiem=ImageTk.PhotoImage(file="img/btn_timkiem.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    # tengv=csdl.tim_tengv_tu_email()
    # Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)
    # magv=csdl.tim_magv_tu_email()
    

    # a=csdl.tim_lop_trong_diemdanh(magv)
    
    # if csdl.tim_lop_trong_diemdanh(magv)==[]:
    #     anhnen=bg.create_image(500,300,image=img_erorr)
    # else:
    #     f=Frame(bg,bg="green")
    #     f.place(x=367,y=270)
    #     tv = ttk.Treeview(f, columns=(1,2,3), show="headings")
    #     tv.column(1, width=150 ,anchor=CENTER)
    #     tv.column(2, width=240)
    #     tv.column(3, width=150,anchor=CENTER)
    #     tv.heading(1,text="Mã số sinh viên")
    #     tv.heading(2,text="Họ và tên")
    #     tv.heading(3,text="Điểm danh")
    #     tv.pack()

    #     f1=Frame(bg)
    #     f1.place(x=462,y=109)
    #     f2=Frame(bg)
    #     f2.place(x=462,y=155)
    #     f3=Frame(bg)
    #     f3.place(x=747,y=109)
    #     f4=Frame(bg)
    #     f4.place(x=747,y=155)

        
    #     data_lop=csdl.tim_lop_trong_diemdanh(magv)
    #     cb_lop=Combobox(f1,width=20,values=data_lop, font=("Baloo Tamma",12))
    #     cb_lop.current(0)
    #     cb_lop.pack()
    #     malop=csdl.tenlop_thanh_ma(str(cb_lop.get()))
    #     mamh=StringVar()
    #     ngay=StringVar()
    #     ca=StringVar()
    #     data=StringVar()
    #     btnchon=Button(bg,image=ing_chon,bd=0,highlightthickness=0,command=chon1)
    #     btnchon.place(x=881,y=176)

    # btnxemthongke=Button(bg,image=ing_btnxemthongke,bd=0,highlightthickness=0,command=batdauthongke)
    # btnxemthongke.place(x=866,y=176)
    win.mainloop()

if __name__ == '__main__':
    main()