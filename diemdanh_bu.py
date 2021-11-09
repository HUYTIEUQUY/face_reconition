from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import numpy as np
import threading
import os
import pandas as pd
from backend.dl_giangvien import tengv_email, magv_email
from backend.dl_adminlop import malop_ten
from backend.dl_monhoc import mamh_ten
from backend.dl_sinhvien import ds_masv_lop
import backend.dl_diemdanh as dd
from backend.dl_tkb import gv_dd
from styletable import style,update
import datetime
import sinhvien
import diemdanh
import taikhoan
import thongke



def main(gvdd):
    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        tengv.set(tengv_email(email))

    def trolai():
        win.destroy()
        diemdanh.main()

    def kttg(tgvao,tgra,ca):
        e=[]
        data_ca1= " "
        data_ca=data_ca1.join(ca).split()

        for i in data_ca:
            dd.tgca(i,e)
        if min(e) <= str(tgvao) and max(e) >=str(tgra):
            return True
        else: return False



    def diemdanhexcel():
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Mở file excel ",filetypes=(("XLSX file","*.xlsx"),("All file","*.*")))
        ko_luu=0
        malop=malop_ten(datalop.get())
        mamon= mamh_ten(datamon.get())
        magv= magv_email(email)
        xl = pd.ExcelFile(fln)
        df = pd.read_excel(xl, 0) 
        dssv=ds_masv_lop(malop)

        for i in range(df.shape[0]):
            masv=df['Mã sinh viên'][i]
            thongtin=df['Thông tin'][i]
            tgvao=df['Thời gian vào'][i]
            tgra=df['Thời gian ra'][i]

            if masv in dssv == False:
                messagebox.showerror("Thông báo","Điểm danh không thành công.\n"+str(masv)+" không thuộc lớp.")
                dd.xoadd(matkb.get())
                ko_luu=1
                break
            elif kttg(tgvao,tgra,dataca.get())== False and str(tgvao) != "nan" and str(tgra) != "nan":
                messagebox.showerror("Thông báo","Điểm danh không thành công.\nThời gian không hợp lý.")
                dd.xoadd(matkb.get())
                ko_luu=1
                break
            else:
                if str(tgvao) == "nan" :
                    tgvao=""
                if str(tgra) == "nan":
                    tgra=""
                dd.diemdanhbangexcel(matkb.get(),masv,thongtin,malop,mamon,magv,datangay.get(),dataca.get(),tgvao,tgra)
        if ko_luu != 1:
            dd.update_TT_diemdanh(matkb.get())
            messagebox.showinfo("thông báo","Đã điểm danh")
            row=gv_dd(magv,ngay)
            if row !=[]:
                update(tv,row)
            else:
                anhnen=bg.create_image(500,300,image=img_bg1)
            
    

#___________________________________________________________________________________________
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        matkb.set(item['values'][0])
        datangay.set(item['values'][3])
        datalop.set(item['values'][1])
        datamon.set(item['values'][2])
        dataca.set(item['values'][4])

    def menuthongke():
        win.destroy()
        thongke.main()

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
    win.iconbitmap(r"img/iconphanmem.ico")
    win.config(bg="green")
    win.title("Điểm danh")
    img_bg=ImageTk.PhotoImage(file="img/bg_diemdanhbu.png")
    img_bg1=ImageTk.PhotoImage(file="img/bg_thongke_erorr.png")
    
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh1.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btndiemdanh=ImageTk.PhotoImage(file="img/btndiemdanhexcel.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/btn_trolai.png")


    #-----------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    email=d[0]
    datalop=StringVar()
    datamon=StringVar()
    datangay=StringVar()
    dataca=StringVar()
    tengv=StringVar()
    matkb=StringVar()
    now=datetime.datetime.now()
    ngay=now.strftime("%x")
    #----------------------------------------------------------------------------

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)


    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,activebackground='#857EBD',command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD',command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,activebackground='#857EBD',command=dangxuat)
    btndangxuat.place(x=248,y=44)

    
    Label(bg,textvariable=tengv,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white").place(x=45,y=35)

    # tạo stype cho bảng
    style()
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=350,y=160)
    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")

    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=120,anchor=CENTER )
    tv.column(2, width=180)
    tv.column(3, width=180)
    tv.column(4, width=100,anchor=CENTER)
    tv.column(5, width=50)
    tv.heading(1,text="MaTKB")
    tv.heading(2,text="Lớp")
    tv.heading(3,text="Môn học")
    tv.heading(4,text="Ngày")
    tv.heading(5,text="Ca")
    tv.pack()
    tree_scroll.config(command=tv.yview)
    tv.tag_configure("ollrow_ghichu" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow_ghichu" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))
    tv.bind('<Double 1>', getrow)
    update(tv,gvdd)
    


    btntrolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=trolai)
    btntrolai.place(x=948,y=2)
    btn_diemdanh=Button(bg,image=ing_btndiemdanh,bd=0,highlightthickness=0,command=diemdanhexcel)
    btn_diemdanh.place(x=550,y=480)
    luong(loaddl)

    win.mainloop()

if __name__ == '__main__':
    main()