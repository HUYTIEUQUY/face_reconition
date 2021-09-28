from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import adminlop
import admin_tkb
import admin_thongke
import admin_monhoc
import backend.dl_giangvien as gv
from backend.dl_giangvien import email_ma, tengv_email,makhoa_email
import threading
import kt_nhap as kt
from styletable import style,update

def main():
    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        makhoa.set(makhoa_email(d[0]))
        tengv.set(tengv_email(d[0]))
        lbgv.config(text=tengv.get())
        khoiphuc()




    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_ma.set(item['values'][1])
        data_magv.set(item['values'][1])
        data_ten.set(item['values'][2])
        data_email.set(item['values'][3])
        data_sdt.set(str(item['values'][4]))
        data_ghichu.set(item['values'][5])
        sdt=gv.sdt_ma(data_ma.get())
        data_sdt.set(sdt)

    def khoiphuc():
        ndtimkiem.set("")
        data_email.set("")
        data_ma.set("")
        data_magv.set("")
        data_ten.set("")
        data_sdt.set("")
        data_ghichu.set("")
        row=gv.banggv(makhoa.get())
        update(tv,row)



    def them():
        ma=data_ma.get()
        ten=data_ten.get()
        ten=kt.xoa_khoangcach(ten)
        sdt=data_sdt.get()
        ghichu=data_ghichu.get()
        tenemail=kt.xoa_khoangcach(kt.khong_dau(ten)).lower().replace(" ","")
        emailgv=tenemail+ma+"@mku.edu.vn"
        if ma =="" or ten == "" or sdt=="":
            messagebox.showwarning("thông báo","Bạn hãy nhập đầy đủ dữ liệu")
        elif len(ma) != 8 or ma.isnumeric()== False:
            messagebox.showwarning("thông báo","Mã giảng viên phải 8 kí tự và là số")
        elif len(sdt) !=10 or sdt.isnumeric()== False:
            messagebox.showwarning("thông báo","Số điện thoại không đúng")
        elif kt.kt_dau_khoangcach(ten)==False or kt.kt_kitudacbiet(ten) != "":
            messagebox.showwarning("thông báo","Dữ liệu tên giảng viên không hợp lệ")
        else:
            if gv.kt_ma(ma) == []:
                gv.themgv(ma,ten,emailgv,sdt,ghichu,makhoa.get())
                messagebox.showinfo("thông báo","Đã thêm giảng viên vào danh sách")
                khoiphuc()
            else:
                messagebox.showerror("thông báo","Mã giảng viên đã tồn tại trong danh sách")
                
    def sua():
        if data_ma.get() != data_magv.get():
            messagebox.showwarning("thông báo","khổng thể sửa mã")
            data_ma.set(data_magv.get())
        elif data_magv.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu sửa. Bạn hãy click 2 lần vào dòng muốn sửa !")
        elif data_ten.get()=="" or data_sdt.get()=="":
            messagebox.showwarning("thông báo","Bạn hãy nhập đầy đủ dữ liệu")
        elif kt.kt_dau_khoangcach(data_ten.get())==False or kt.kt_kitudacbiet(data_ten.get()) !="":
            messagebox.showwarning("thông báo","Dữ liệu tên giảng viên không hợp lệ")
        elif data_sdt.get().isnumeric()== False:
            messagebox.showwarning("thông báo","Số điện thoại không đúng")
        elif gv.suagv(data_magv.get(),data_ten.get(),data_sdt.get(),data_ghichu.get()):
            messagebox.showinfo("thông báo","Đã sửa thành công")
            khoiphuc()
        else:
            messagebox.showerror("thông báo","Sửa không thành công")
        
    def xoa():
        if data_ma.get()=="" or data_ten.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu xoá. Bạn hãy click 2 lần vào dòng muốn xoá !")
        elif messagebox.askyesno("thông báo","Bạn thực sự muốn xoá"):
            if gv.kt_gv_tontai_tkb(data_ma.get()) ==[] and gv.kt_gv_tontai_diemdanh(data_ma.get())==[]:
                tenemail=email_ma(data_ma.get())
                gv.xoa_tk(tenemail)
                gv.xoagv(data_ma.get())
                luong(khoiphuc)
                messagebox.showinfo("thông báo","Đã xoá giảng viên ra khỏi danh sách")
            else:
                messagebox.showerror("thông báo","Xoá thất bại")

    
    def timkiem():
        row=gv.tim_gv(makhoa.get(),ndtimkiem.get())
        update(tv,row)

    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menulophoc():
        win.destroy()
        adminlop.main()
    def menutkb():
        win.destroy()
        admin_tkb.main()
    def menumonhoc():
        win.destroy()
        admin_monhoc.main()
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
    win.title("Giảng viên")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_giangvien.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien1.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")
    img_btnchon=ImageTk.PhotoImage(file="img_admin/btn_chon.png")
    img_btnchonlich=ImageTk.PhotoImage(file="img_admin/chonlich.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    
    makhoa=StringVar()
    tengv=StringVar()
    ndtimkiem=StringVar()
    data_ma=StringVar()
    data_ten=StringVar()
    data_email=StringVar()
    ndtimkiem=StringVar()
    data_magv=StringVar()
    data_sdt=StringVar()
    data_ghichu=StringVar()
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menulophoc)
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,activebackground='#857EBD')
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,activebackground='#857EBD',command=menutkb)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=30,y=461)

    lbgv=Label(bg,font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ma,bd=0,highlightthickness=0).place(x=575,y=20)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ten,bd=0,highlightthickness=0).place(x=575,y=55)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_sdt,bd=0,highlightthickness=0).place(x=575,y=90)
    Entry(bg,font=("Baloo Tamma",11),width=36,textvariable=data_ghichu,bd=0,highlightthickness=0).place(x=575,y=125)
    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=250)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=185)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0, command=sua)
    btnsua.place(x=637,y=185)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=185)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,activebackground='white',command=timkiem)
    btntimkiem.place(x=881,y=250)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground='white',command=khoiphuc)
    btnkhoiphuc.place(x=920,y=250)


    f=Frame(bg)
    f.place(x=320,y=30)

    # tạo stype cho bảng
    style()
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=328,y=300)

    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=30,anchor=CENTER)
    tv.column(2, width=100,anchor=CENTER)
    tv.column(3, width=140)
    tv.column(4, width=260)
    tv.column(5, width=80,anchor=CENTER)
    # tv.column(6, width=80)

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="Mã GV")
    tv.heading(3,text="Tên giảng viên")
    tv.heading(4,text="Email")
    tv.heading(5,text="Số điện thoại")
    # tv.heading(6,text="Ghi chú")
    tv.pack()
    tv.bind('<Double 1>', getrow)
    tv.tag_configure("ollrow" ,background="white")
    tv.tag_configure("evenrow" ,background="#ECECEC")
    
    luong(loaddl)
    win.mainloop()

   

if __name__ == '__main__':
    main()