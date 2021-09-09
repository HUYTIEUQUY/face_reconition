from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import quantrivien_khoa
from backend.dl_giangvien import tengv_email
from backend.dl_adminlop import malop_ten
from backend.dl_monhoc import mamh_ten
from backend.dl_khoa import tenkhoa_ma
import backend.dl_thongke as tk
import quantrivien_khoa
import quantrivien_thietlap
import threading
import xlsxwriter
import os

def main():
    
    def luong(ham):
        threading.Thread(target=ham).start()

    def chongiatridau(data,cb):
        if data==[]:
            cb.set("")
            cb_lop.config(text="",values=[])
            cb_mh.config(text="",values=[])
            cb_ngay.config(text="",values=[])
            cb_ca.config(text="",values=[])
            magv.set("")
        else:
            cb.current(0)

    def loaddl():
        tengv.set(tengv_email(d[0]))
        lbgv.config(text=tengv.get())
        data_khoa = tk.ds_khoa()
        cb_khoa.config(values=data_khoa)
        chongiatridau(data_khoa,cb_khoa)
        cb_khoa.bind('<<ComboboxSelected>>', chongv)
        luong(khoiphuc)

    def chongv(event):
        # lb_khoa=Label(bg,text=cb_khoa.get(),font=("Baloo Tamma",12),bg="white")
        # lb_khoa.place(x=468,y=100)
        # cb_khoa.destroy()
        makhoa.set(tk.makhoa_ten(cb_khoa.get()))
        data_gv = tk.ds_gv(makhoa.get())
        cb_gv.config(values=data_gv)
        chongiatridau(data_gv,cb_gv)
        if cb_gv.get() !="":
            tachma=str(cb_gv.get()).replace(" ","").replace("-"," ").split()
            magv.set(str(tachma[0]))
        cb_gv.bind('<<ComboboxSelected>>', chonlop)
        luong(khoiphuc)

    def chonlop(event):
        # lb_gv=Label(bg,text=cb_gv.get(),font=("Baloo Tamma",12),bg="white")
        # lb_gv.place(x=468,y=125)
        
        tachma=str(cb_gv.get()).replace(" ","").replace("-"," ").split()
        magv.set(str(tachma[0]))
        # cb_gv.destroy()
        data_lop = tk.tenlop_dd(magv.get())
        cb_lop.config(values=data_lop)
        cb_lop.current(0)
        cb_lop.bind('<<ComboboxSelected>>', chonmh)
        luong(khoiphuc)

    def chonmh(event):
        # lb_lop=Label(bg,text=cb_lop.get(),font=("Baloo Tamma",12),bg="white")
        # lb_lop.place(x=468,y=150)

        malop.set(malop_ten(cb_lop.get()))
        # cb_lop.destroy()
        data_mh = tk.monhoc_dd(magv.get(),malop.get())
        cb_mh.config(values=data_mh)

        cb_mh.current(0)
        cb_mh.bind('<<ComboboxSelected>>', chonngay)
        luong(khoiphuc)

    def chonngay(event):
        # lb_mh=Label(bg,text=cb_mh.get(),font=("Baloo Tamma",12),bg="white")
        # lb_mh.place(x=468,y=175)
        mamh.set(mamh_ten(cb_mh.get()))
        # cb_mh.destroy()
        data_ngay = tk.ngay_dd(magv.get(),malop.get(),mamh.get())
        cb_ngay.config(values=data_ngay)

        cb_ngay.current(0)
        cb_ngay.bind('<<ComboboxSelected>>', chonca)
        luong(khoiphuc)

    def chonca(event):
        # lb_ngay=Label(bg,text=cb_ngay.get(),font=("Baloo Tamma",12),bg="white")
        # lb_ngay.place(x=468,y=200)
        ngay.set(cb_ngay.get())
        # cb_ngay.destroy()
        data_ca = tk.ca_dd(magv.get(),malop.get(),mamh.get(),ngay.get())
        cb_ca.config(values=data_ca)

        cb_ca.current(0)
        cb_ca.bind('<<ComboboxSelected>>', xem)
        luong(khoiphuc)

    def xem(event):
        ca.set(cb_ca.get())
        luong(khoiphuc)

    def timkiem():
        row=tk.tim_tk(magv.get(),malop.get(),mamh.get(),ngay.get(),ca.get(),ndtimkiem.get())
        update(row)
    
    def dongluu(row,ma,ten,tt,TG,ghichu):
        for i in row:
            ma.append(i[0]) 
            ten.append(i[1]) 
            tt.append(i[2]) 
            TG.append(i[3]) 
            ghichu.append(i[4])  

    def xuat_excel():
        row=tk.thongke(magv.get(),malop.get(),mamh.get(),ngay.get(),ca.get())
        ma=[]
        ten=[]
        tt=[]
        TG=[]
        ghichu=[]
        dongluu(row,ma,ten,tt,TG,ghichu)

        if len(ma)<1:
            messagebox.showwarning("thông báo","Không có dữ liệu xuất file excel !")
            return False
        else:

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Lưu file excel",filetypes=(("XLSX File","*.xlsx"),("All File","*.*")))
          

            out_workbook = xlsxwriter.Workbook(fln+".xlsx")
            outsheet = out_workbook.add_worksheet()
            tenlop=tk.tenlop_ma(malop.get())
            tenmh=tk.tenmh_ma(mamh.get())
            outsheet.write("A1","Khoa:"+tenkhoa_ma(makhoa.get()))
            outsheet.write("B1",tenlop)
            outsheet.write("C1",tenmh)
            outsheet.write("D1",ngay.get())

            outsheet.write("A3","Mã sinh viên")
            outsheet.write("B3","Tên sinh viên")
            outsheet.write("C3","Thông tin")
            outsheet.write("D3","Thời gian vào-ra")
            outsheet.write("E3","Ghi chú")
            def write_data_to_file(array,x):
                for i in range(len(array)):
                    outsheet.write(i+3,x,array[i])
            write_data_to_file(ma,0)
            write_data_to_file(ten,1)
            write_data_to_file(tt,2)
            write_data_to_file(TG,3)
            write_data_to_file(ghichu,4)
            out_workbook.close()

    def khoiphuc():
        row=tk.thongke(magv.get(),malop.get(),mamh.get(),ngay.get(),ca.get())
        update(row)
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    
    def menuthietlap():
        win.destroy()
        quantrivien_thietlap.main()

    def menukhoa():
        win.destroy()
        quantrivien_khoa.main()

    def menuthongke():
        win.destroy()
        main()

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
    img_bg=ImageTk.PhotoImage(file="img_qtv/bg_thongke.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_qtv/btn_dangxuat.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_qtv/menu_thongke1.png")
    img_menuthietlap=ImageTk.PhotoImage(file="img_qtv/menu_thietlap.png")
    img_menukhoa=ImageTk.PhotoImage(file="img_qtv/menu_khoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_qtv/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_qtv/btn_khoiphuc.png")
    img_btnexcel_xuat=ImageTk.PhotoImage(file="img_qtv/xuat_excel.png")
    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    ndtimkiem=StringVar()
    tengv=StringVar()


    khoa =StringVar()
    makhoa=StringVar()
    gv=StringVar()
    magv=StringVar()
    lop=StringVar()
    malop=StringVar()
    mh=StringVar()
    mamh=StringVar()
    ngay=StringVar()
    ca=StringVar()


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

    lbgv=Label(bg,font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    cb_khoa=Combobox(bg,textvariable=khoa,font=("Baloo Tamma",12),state='readonly',width=30)
    cb_khoa.place(x=600,y=70)
    cb_gv=Combobox(bg,textvariable=gv,font=("Baloo Tamma",12),state='readonly',width=30)
    cb_gv.place(x=600,y=100)
    cb_lop=Combobox(bg,textvariable=lop,font=("Baloo Tamma",12),state='readonly',width=30)
    cb_lop.place(x=600,y=130)
    cb_mh=Combobox(bg,textvariable=mh,font=("Baloo Tamma",12),state='readonly',width=30)
    cb_mh.place(x=600,y=160)
    cb_ngay=Combobox(bg,textvariable=ngay,font=("Baloo Tamma",12),state='readonly',width=30)
    cb_ngay.place(x=600,y=190)
    cb_ca=Combobox(bg,textvariable=ca,font=("Baloo Tamma",12),state='readonly',width=30)
    cb_ca.place(x=600,y=220)

    


    tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=80 )
    tv.column(2, width=100,anchor=CENTER)
    tv.column(3, width=80,anchor=CENTER)
    tv.column(4, width=100,anchor=CENTER)
    tv.column(5, width=180)
    tv.heading(1,text="Mã sinh viên")
    tv.heading(2,text="Tên sinh viên")
    tv.heading(3,text="Thông tin")
    tv.heading(4,text="TG vào - TG ra")
    tv.heading(5,text="Ghi chú")
    tv.place(x=367,y=350)

    Entry(bg,font=("Baloo Tamma",11),width=27,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=635,y=297)

    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=862,y=295)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc,bg="white")
    btnkhoiphuc.place(x=905,y=295)
    btnexcelxuat=Button(bg,image=img_btnexcel_xuat,bd=0,highlightthickness=0,command=xuat_excel)
    btnexcelxuat.place(x=948,y=2)


    luong(loaddl)
    win.mainloop()

    

if __name__ == '__main__':
    main()