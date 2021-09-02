from backend.dl_adminlop import malop_ten
import re
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from functools import partial
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import adminlop
import admin_giangvien
import admin_tkb
import admin_monhoc
import backend.dl_thongke as tk
from backend.dl_giangvien import tengv_email,makhoa_email,magv_all, magv_ten
import xlsxwriter
import os

def main():
    def dongluu(row,ma,ten,tt,TG,ghichu):

        for i in row:
            ma.append(i[0]) 
            ten.append(i[1]) 
            tt.append(i[2]) 
            TG.append(i[3]) 
            ghichu.append(i[4])  

    def xuat_excel():
        row =tk.thongke(magv.get(),lop.get(),mamh.get(),ngay.get(),ca.get())
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
        row=tk.tim_tk(magv.get(),lop.get(),mamh.get(),ngay.get(),ca.get(),ndtimkiem.get())
        update(row)

    def chon4(cb_ca):
        Label(bg,text=ca.get(),font=("Baloo Tamma",12),bg="white").place(x=762,y=142)
        cb_ca.destroy()
        row =tk.thongke(magv.get(),lop.get(),mamh.get(),ngay.get(),ca.get())
        update(row)
    def chon3(cb_ngay):
        ngay.set(cb_ngay.get())
        data_ca = tk.ca_dd(magv.get(),lop.get(),mamh.get(),cb_ngay.get())
        Label(bg,text=cb_ngay.get(),font=("Baloo Tamma",12),bg="white").place(x=762,y=95)
        cb_ngay.destroy()
        cb_ca=Combobox(bg,textvariable=ca,font=("Baloo Tamma",12),values=data_ca,width=10)
        cb_ca.place(x=762,y=145)
        btnchon.config(image=ing_btnxemthongke,command=lambda:chon4(cb_ca))
       
    def chon2(cb_mh):
        mamh.set(tk.mamh_ten(cb_mh.get()))
        data_ngay = tk.ngay_dd(magv.get(),lop.get(),mamh.get())
        Label(bg,text=cb_mh.get(),font=("Baloo Tamma",12),bg="white").place(x=468,y=189)
        cb_mh.destroy()
        cb_ngay=Combobox(bg,textvariable=ngay,font=("Baloo Tamma",12),values=data_ngay,width=10)
        cb_ngay.place(x=762,y=95)
        btnchon.config(command=lambda:chon3(cb_ngay))
        

    def chon1(cb_tengv1):
        mlop=tk.malop_ten(lop.get())
        magv.set(magv_ten(cb_tengv1.get()))
        data_mh = tk.monhoc_dd(magv_ten(cb_tengv1.get()),mlop)
        Label(bg,text=lop.get(),font=("Baloo Tamma",12),bg="white").place(x=468,y=142)
        cb_tengv1.destroy()
        cb_mh=Combobox(bg,textvariable="",font=("Baloo Tamma",12),values=data_mh,width=10)
        cb_mh.place(x=468,y=189)
        lop.set(mlop)
        btnchon.config(command=lambda:chon2(cb_mh))
        

    def chon():
        data_tengv = tk.tengv_all()
        cb_tengv1=Combobox(bg,textvariable=mh,font=("Baloo Tamma",12),values=data_tengv,width=15)
        Label(bg,text=cb_tengv.get(),font=("Baloo Tamma",12),bg="white").place(x=468, y=95)
        cb_tengv.destroy()
        cb_lop=Combobox(bg,textvariable=lop,font=("Baloo Tamma",12),values=data_lop,width=16)
        cb_lop.place(x=468,y=142)
        # lop.set(mlop)
        btnchon.config(command=lambda:chon1(cb_tengv1))
        btnchonlai=Button(bg,image=ing_chonlai,bd=0,highlightthickness=0,command=reset)
        btnchonlai.place(x=869,y=207)

    def reset():
        win.destroy()
        main()
    def menutkb():
        win.destroy()
        admin_tkb.main()
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
    
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_thongke_admin.png")
    img_erorr=ImageTk.PhotoImage(file="img/bg_thongke_erorr.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke1.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")
    ing_btnxemthongke=ImageTk.PhotoImage(file="img/btn_xemthongke.png")
    ing_chon=ImageTk.PhotoImage(file="img/btnchon.png")
    ing_chonlai=ImageTk.PhotoImage(file="img/chonlai.png")
    img_btnexcel_xuat=ImageTk.PhotoImage(file="img_admin/xuat_excel.png")
    ing_timkiem=ImageTk.PhotoImage(file="img/btn_timkiem.png")


#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    # makhoa=csdl.makhoa_tu_email(email)
    mamh=StringVar()
    ngay=StringVar()
    ca=StringVar()
    lop=StringVar()
    magv=StringVar()

    tengv=tengv_email(d[0])
    
    makhoa=makhoa_email(d[0])
    
    data_lop=tk.tenlop_dd1()
    mh=StringVar()
    ndtimkiem=StringVar()
    row=""
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
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,command=menutkb)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0)
    menuthongke.place(x=30,y=461)

    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)
    Entry(bg,font=("Baloo Tamma",11),width=27,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=630,y=250)


    data_tengv = tk.tengv_all()
    cb_tengv=Combobox(bg,textvariable=mh,font=("Baloo Tamma",12),values=data_tengv,width=15)
    cb_tengv.place(x=468, y=95)       

    btnchon=Button(bg,image=ing_chon,bd=0,highlightthickness=0, activebackground="white",command=chon)
    btnchon.place(x=881,y=176)
    btntimkiem=Button(bg,image=ing_timkiem,highlightthickness=0,bd=0,command=timkiem)
    btntimkiem.place(x=880,y=248)
    btnexcelxuat=Button(bg,image=img_btnexcel_xuat,bd=0,highlightthickness=0,command=xuat_excel)
    btnexcelxuat.place(x=948,y=2)

    if data_lop==[]:
        anhnen=bg.create_image(500,300,image=img_erorr)
    else:
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
        tv.place(x=367,y=280)

   
    win.mainloop()

if __name__ == '__main__':
    main()