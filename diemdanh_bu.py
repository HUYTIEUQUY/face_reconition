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
from backend.dl_adminlop import malop_ten,tenlop_ma
from backend.dl_monhoc import mamh_ten, tenmh_ma
from backend.dl_sinhvien import ds_masv_lop
import backend.dl_diemdanh as dd
from backend.dl_tkb import gv_dd
from styletable import style
from kt_nhap import dinh_dang_ngay
import datetime
import sinhvien
import diemdanh
import taikhoan
import thongke



def main(trang):
    def loadding(a):
        if a==1:# đang load dữ liệu
            btn_diemdanh["state"] = "disabled"
            btntrolai["state"] = "disabled"
        else:
            btn_diemdanh["state"] = "normal"
            btntrolai["state"] = "normal"
    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        loadding(1)
        try:
            tengv.set(tengv_email(email))
            gvdd=gv_dd(magv,ngay)
            if gvdd==[]:
                messagebox.showinfo("Thông báo","Đã điểm danh đầy đủ")
            else:
                update(gvdd)
            loadding(0)
        except:loadding(0)

    def update(row):
        tv.delete(*tv.get_children())
        global dem
        dem=0
        for i in row:
            i.insert(0,dem+1)
            i[2]= tenlop_ma(i[2])
            i[3]= tenmh_ma(i[3])
            if dem%2==0:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
            else:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
            dem += 1

    def trolai():
        win.destroy()
        diemdanh.main()

    def kttg(tgvao,tgra,ca):
        e=[]
        data_ca1= " "
        data_ca=data_ca1.join(ca).split()

        for i in data_ca:
            a=dd.tgca(i)
            e.append(a[0])
            e.append(a[1])
        if str(tgvao) == "" or str(tgvao) == "nan" or str(tgra) == "" or str(tgra) == "nan":
            return True
        else:
            if min(e) <= str(tgvao) and max(e) >=str(tgra):
                return True
            else: return False
        



    def diemdanhexcel():
        loadding(1)
        try:
            if matkb.get()=="":
                messagebox.showerror("Thông báo","Hãy chọn thông tin để điểm danh ...")
            else:
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

                    if str(masv) not in dssv:
                        messagebox.showerror("Thông báo","Điểm danh không thành công.\nSinh viên có mã "+str(masv)+" không thuộc lớp.")
                        threading.Thread(target=dd.xoadd,args=(matkb.get(),)).start()
                        ko_luu=1
                        break
                    else:
                        if str(tgvao) == "nan" :
                            tgvao=""
                        if str(tgra) == "nan":
                            tgra=""
                        threading.Thread(target=dd.diemdanhbangexcel,args=(matkb.get(),masv,thongtin,malop,mamon,magv,datangay.get(),dataca.get(),tgvao,tgra,)).start()
                if ko_luu != 1:
                    dd.update_TT_diemdanh(matkb.get())
                    row=gv_dd(magv,ngay)
                    messagebox.showinfo("thông báo","Đã điểm danh")
                    loadding(0)
                    if row !=[]:
                        update(row)
                    elif trang == 1:
                        win.destroy()
                        taikhoan.main()
                    elif trang ==0:
                        win.destroy()
                        diemdanh.main()
            loadding(0)
        except:loadding(0)
                
    

#___________________________________________________________________________________________
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        matkb.set(item['values'][1])
        datangay.set(item['values'][4])
        datalop.set(item['values'][2])
        datamon.set(item['values'][3])
        dataca.set(item['values'][5])

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
    win.config(bg="white")
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
    time = datetime.datetime.now()
    now = time.strftime("%x")
    ngay=dinh_dang_ngay(now)
    magv=magv_email(email)
    


    
    #----------------------------------------------------------------------------

    bg=Canvas(win,width=1000,height=600,bg="white")
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
    fr_tb.place(x=330,y=160)
    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")

    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5,6),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=30,anchor=CENTER )
    tv.column(2, width=60,anchor=CENTER )
    tv.column(3, width=200)
    tv.column(4, width=200)
    tv.column(5, width=100,anchor=CENTER)
    tv.column(6, width=50)
    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="Mã TKB")
    tv.heading(3,text="Lớp")
    tv.heading(4,text="Môn học")
    tv.heading(5,text="Ngày")
    tv.heading(6,text="Ca")
    tv.pack()
    tree_scroll.config(command=tv.yview)
    tv.tag_configure("ollrow" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))
    tv.bind('<ButtonRelease-1>', getrow)
    
    


    btntrolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=trolai)
    btntrolai.place(x=948,y=2)
    btn_diemdanh=Button(bg,image=ing_btndiemdanh,bd=0,highlightthickness=0,command=diemdanhexcel)
    btn_diemdanh.place(x=550,y=480)
    luong(loaddl)
    win.mainloop()

if __name__ == '__main__':
    main()