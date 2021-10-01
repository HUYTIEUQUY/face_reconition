from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import admin_giangvien
import admin_monhoc
import adminlop
import admin_tkb
from backend.dl_giangvien import tengv_email,makhoa_email,magv_email
import backend.dl_thongke as tk
import os
import xlsxwriter
import threading
from tkinter import filedialog
from styletable import style,update

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
        makhoa.set(makhoa_email(d[0]))
        magv.set(magv_email(d[0]))
        data_gv=tk.ds_gv(makhoa.get())
        lbgv.config(text=tengv.get())

        if data_gv==[]:
            anhnen=bg.create_image(500,300,image=img_erorr)
            

        else:
            lb_gv.place(x=380,y=50)
            lb_lop.place(x=380,y=80)
            lb_mon.place(x=380,y=110)
            lb_ngay.place(x=380,y=140)
            lb_ca.place(x=380,y=170)
            cb_gv.place(x=550,y=50)
            cb_lop.place(x=550,y=80)
            cb_mh.place(x=550,y=110)
            cb_ngay.place(x=550,y=140)
            cb_ca.place(x=550,y=170)
            tv.pack()
            txttim.place(x=658,y=241)
            btnkhoiphuc.place(x=925,y=242)
            btntimkiem.place(x=885,y=242)
            btnexcelxuat.place(x=948,y=2)
            cb_gv.config(values=data_gv)
            chongiatridau(data_gv,cb_gv)
            cb_gv.bind('<<ComboboxSelected>>', chonlop)
            luong(khoiphuc)

    def chonlop(event):
        tachma=str(cb_gv.get()).replace(" ","").replace("-"," ").split()
        magv.set(str(tachma[0]))
        data_lop = tk.tenlop_dd(magv.get())
        cb_lop.config(values=data_lop)
        cb_lop.current(0)
        cb_lop.bind('<<ComboboxSelected>>', chonmh)
        luong(khoiphuc)


    def chonmh(event):
        malop.set(tk.malop_ten(cb_lop.get()))
        data_mh = tk.monhoc_dd(magv.get(),malop.get())
        cb_mh.config(values=data_mh)
        cb_mh.current(0)
        cb_mh.bind('<<ComboboxSelected>>', chonngay)
        luong(khoiphuc)

    def chonngay(event):
        mamh.set(tk.mamh_ten(cb_mh.get()))
        data_ngay = tk.ngay_dd(magv.get(),malop.get(),mamh.get())
        cb_ngay.config(values=data_ngay)
        cb_ngay.current(0)
        cb_ngay.bind('<<ComboboxSelected>>', chonca)
        luong(khoiphuc)

    def chonca(event):
        ngay.set(cb_ngay.get())
        data_ca = tk.ca_dd(magv.get(),malop.get(),mamh.get(),ngay.get())
        cb_ca.config(values=data_ca)
        cb_ca.current(0)
        cb_ca.bind('<<ComboboxSelected>>', xem)
        luong(khoiphuc)

    def xem(event):
        ca.set(cb_ca.get())
        luong(khoiphuc)


    def khoiphuc():
        ndtimkiem.set("")
        row=tk.thongke(magv.get(),malop.get(),mamh.get(),ngay.get(),ca.get())
        update(tv,row)

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
            outsheet.write("A1","Tên lớp: "+tenlop)
            outsheet.write("B1","Tên giảng viên: "+cb_gv.get())
            outsheet.write("C1","Môn học: "+tenmh)
            outsheet.write("D1","Ngày: "+ngay.get())

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

    def timkiem():
        row=tk.tim_tk(magv.get(),malop.get(),mamh.get(),ngay.get(),ca.get(),ndtimkiem.get())
        update(tv,row)
    
    def menutkb():
        win.destroy()
        admin_tkb.main()
    def menuthongke():
        win.destroy()
        main()
    def menulophoc():
        win.destroy()
        adminlop.main()
    def menugiangvien():
        win.destroy()
        admin_giangvien.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
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
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_thongke_admin.png")
    img_erorr=ImageTk.PhotoImage(file="img/bg_thongke_erorr.png")
    
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke1.png")
    img_menudangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    ing_timkiem=ImageTk.PhotoImage(file="img/btn_timkiem.png")
    img_btnexcel_xuat=ImageTk.PhotoImage(file="img_admin/xuat_excel.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=dangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menulophoc)
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,activebackground='#857EBD',command=menugiangvien)
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,activebackground='#857EBD', command=menutkb)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=30,y=461)


    btntimkiem=Button(bg,image=ing_timkiem,bd=0,highlightthickness=0,activebackground='white',command=timkiem)
    
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground='white',command=khoiphuc,bg="white")
    

    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()

    mamh=StringVar()
    ngay=StringVar()
    ca=StringVar()
    lop=StringVar()
    malop=StringVar()
    tengv=StringVar()
    makhoa=StringVar()
    magv=StringVar()
    mh=StringVar()
    ndtimkiem=StringVar()
    row=''
    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)


    btnexcelxuat=Button(bg,image=img_btnexcel_xuat,bd=0,highlightthickness=0,command=xuat_excel)
    

    cb_gv=Combobox(bg,textvariable=tengv,font=("Baloo Tamma 2 Medium",12),state='readonly',width=30)
    
    cb_lop=Combobox(bg,textvariable=lop,font=("Baloo Tamma 2 Medium",12),state='readonly',width=30)
    
    cb_mh=Combobox(bg,textvariable=mh,font=("Baloo Tamma 2 Medium",12),state='readonly',width=30)

    cb_ngay=Combobox(bg,textvariable=ngay,font=("Baloo Tamma 2 Medium",12),state='readonly',width=30)
    
    cb_ca=Combobox(bg,textvariable=ca,font=("Baloo Tamma 2 Medium",12),state='readonly',width=30)
    
    lb_gv=Label(bg,text="1.Giảng viên",font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#EBDFF0")
    lb_lop=Label(bg,text="2.Lớp học",font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#EBDFF0")
    lb_mon=Label(bg,text="3.Môn học",font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#EBDFF0")
    lb_ngay=Label(bg,text="4.Ngày học",font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#EBDFF0")
    lb_ca=Label(bg,text="5.Ca",font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#EBDFF0")
    # tạo stype cho bảng
    style()
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=318,y=300)

    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5,6),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=50 )
    tv.column(2, width=100 )
    tv.column(3, width=160)
    tv.column(4, width=100,anchor=CENTER)
    tv.column(5, width=100,anchor=CENTER)
    tv.column(6, width=100,anchor=CENTER)
    # tv.column(5, width=180)
    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT" )
    tv.heading(2,text="MÃ SINH VIÊN")
    tv.heading(3,text="HỌ TÊN")
    tv.heading(4,text="THÔNG TIN")
    tv.heading(5,text="TG Vào")
    tv.heading(6,text="TG Ra")
    # tv.heading(5,text="Ghi chú")
    tv.tag_configure("ollrow" ,background="white",font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))
    txttim=Entry(bg,font=("Baloo Tamma 2 Medium",11),width=25,textvariable=ndtimkiem,bd=0,highlightthickness=0)

    luong(loaddl)
    win.mainloop()
    

if __name__ == '__main__':
    main()