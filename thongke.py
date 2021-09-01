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
from backend.dl_giangvien import tengv_email,makhoa_email,magv_email
import backend.dl_thongke as tk
import os
import xlsxwriter
import threading
from tkinter import filedialog

def main():
    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        tengv.set(tengv_email(d[0]))
        makhoa.set(makhoa_email(d[0]))
        magv.set(magv_email(d[0]))
        data_lop=tk.tenlop_dd(magv.get())
        cb_lop.config(values=data_lop,state='readonly')
        cb_lop.current(0)
        lbgv.config(text=tengv.get())

        if data_lop==[]:
            anhnen=bg.create_image(500,300,image=img_erorr)
        else:
            # f=Frame(bg,bg="green")
            # f.place(x=367,y=270)
            tv.place(x=367,y=280)



    def dongluu(row,ma,ten,tt,TG,ghichu):

        for i in row:
            ma.append(i[0]) 
            ten.append(i[1]) 
            tt.append(i[2]) 
            TG.append(i[3]) 
            ghichu.append(i[4])  

    def xuat_excel():
        row=tk.thongke(magv.get(),lop.get(),mamh.get(),ngay.get(),ca.get())
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
            tenlop=tk.tenlop_ma(lop.get())
            tenmh=tk.tenmh_ma(mamh.get())
            outsheet.write("A1",tenlop)
            outsheet.write("B1",tenmh)
            outsheet.write("C1",ngay.get())

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
    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def timkiem():
        return
    def chon3(cb_ca):
        Label(bg,text=ca.get(),font=("Baloo Tamma",12),bg="white").place(x=762,y=142)
        cb_ca.destroy()
        row=tk.thongke(magv.get(),lop.get(),mamh.get(),ngay.get(),ca.get())
        update(row)
    def chon2(cb_ngay):
        ngay.set(cb_ngay.get())
        data_ca = tk.ca_dd(magv.get(),lop.get(),mamh.get(),cb_ngay.get())
        Label(bg,text=cb_ngay.get(),font=("Baloo Tamma",12),bg="white").place(x=762,y=97)
        cb_ngay.destroy()
        cb_ca=Combobox(bg,textvariable=ca,font=("Baloo Tamma",12),state='readonly',values=data_ca,width=10)
        cb_ca.place(x=762,y=145)
        btnchon.config(image=ing_btnxemthongke,command=lambda:chon3(cb_ca))

    def chon1(cb_mh):
        mamh.set(tk.mamh_ten(cb_mh.get()))
        data_ngay = tk.ngay_dd(magv.get(),lop.get(),mamh.get())
        Label(bg,text=cb_mh.get(),font=("Baloo Tamma",12),bg="white").place(x=468,y=145)
        cb_mh.destroy()
        cb_ngay=Combobox(bg,textvariable=ngay,font=("Baloo Tamma",12),state='readonly',values=data_ngay,width=10)
        cb_ngay.place(x=762,y=95)
        btnchon.config(command=lambda:chon2(cb_ngay))

    def chon():
        mlop=tk.malop_ten(lop.get())
        data_mh = tk.monhoc_dd(magv.get(),mlop)
        Label(bg,text=lop.get(),font=("Baloo Tamma",12),bg="white").place(x=468,y=97)
        cb_lop.destroy()
        cb_mh=Combobox(bg,textvariable=mh,font=("Baloo Tamma",12),state='readonly',values=data_mh,width=20)
        cb_mh.place(x=468,y=142)
        lop.set(mlop)
        btnchon.config(command=lambda:chon1(cb_mh))
        btnchonlai=Button(bg,image=ing_chonlai,bd=0,highlightthickness=0,command=reset)
        btnchonlai.place(x=869,y=207)

    def reset():
        win.destroy()
        main()
   
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
    img_bg=ImageTk.PhotoImage(file="img/bg_thongke.png")
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
    img_btnexcel_xuat=ImageTk.PhotoImage(file="img_admin/xuat_excel.png")

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

    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()

    mamh=StringVar()
    ngay=StringVar()
    ca=StringVar()
    lop=StringVar()
    tengv=StringVar()
    makhoa=StringVar()
    magv=StringVar()
    mh=StringVar()
    row=''
    lbgv=Label(bg,font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    cb_lop=Combobox(bg,textvariable=lop,font=("Baloo Tamma",12),width=20)
    cb_lop.place(x=468,y=95)


    btnchon=Button(bg,image=ing_chon,bd=0,highlightthickness=0, activebackground="white",command=chon)
    btnchon.place(x=881,y=176)
    btntimkiem=Button(bg,image=ing_timkiem,highlightthickness=0,bd=0,command=timkiem)
    btntimkiem.place(x=880,y=248)
    btnexcelxuat=Button(bg,image=img_btnexcel_xuat,bd=0,highlightthickness=0,command=xuat_excel)
    btnexcelxuat.place(x=948,y=2)
 
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


    luong(loaddl)
    win.mainloop()
    

if __name__ == '__main__':
    main()