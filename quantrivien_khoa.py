from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import quantrivien_khoa
from backend.dl_giangvien import tengv_email
from backend.dl_khoa import sl_khoa 
import backend.dl_khoa as khoa
import quantrivien_thongke
import quantrivien_thietlap


def main():

    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)
    def kt_dau_khoangcach(s):
        return bool(s and s.strip())
    def them():
        makhoa=khoa.sl_khoa()
        emailgv=makhoa+"@mku.edu.vn"
        ten=tenkhoa.get()
        if ten=="":
            messagebox.showwarning("thông báo","Hãy nhập dữ liệu đầy đủ")
        elif kt_dau_khoangcach(ten)== False:
            messagebox.showwarning("thông báo","Dữ liệu tên khoa không hợp lệ")
        elif khoa.kt_tenkhoa(ten)!= []:
            messagebox.showerror("thông báo",ten +" đã tồn tại")
        else:
            khoa.themkhoa(makhoa,ten)
            khoa.them_tk_khoa("admin"+makhoa, emailgv, sl_khoa)
            messagebox.showinfo("thông báo","Thêm '"+ten+"' thành công")
            khoiphuc()
    

    def xoa():
        ten=tenkhoa.get()
        ma=makhoa.get()
        if ten=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu xoá. Bạn hãy click 2 lần vào dòng muốn xoá !")
        elif messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            if khoa.kt_lop_in_khoa(ma) == False:
                khoa.xoakhoa(ma)
                messagebox.showinfo("thông báo","Xoá '"+ten+"' thành công")
                khoiphuc()
            else:
                messagebox.showerror("thông báo", "không thể xoá\nCó lớp tồn tại trong khoa")
        else:
            return

    def sua():
        tenmoi=tenkhoa.get()
        makhoa1=makhoa.get()

        if tenmoi=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu cập nhật")
        elif makhoa.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu cập nhật, Bạn hãy click 2 lần vào dòng cần cập nhật")
        elif kt_dau_khoangcach(tenmoi)== False:
            messagebox.showwarning("thông báo","Dữ liệu tên lớp không hợp lệ")
        elif khoa.kt_tenkhoa(tenmoi)!= []:
            messagebox.showerror("thông báo",tenmoi+" đã tồn tại")
        else:
            khoa.suakhoa(makhoa1,tenmoi)
            messagebox.showinfo("thông báo","Đã đổi tên khoa thành công")
            khoiphuc()
            
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        tenkhoa.set(item['values'][2])
        makhoa.set(item['values'][1])

    def khoiphuc():
        ndtimkiem.set("")
        tenkhoa.set("")
        row=khoa.bangkhoa()
        update(row)

    def timkiem():
        row=khoa.timkhoa(ndtimkiem.get())
        update(row)

    def menuthietlap():
        win.destroy()
        quantrivien_thietlap.main()

    def menukhoa():
        win.destroy()
        main()

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
    img_bg=ImageTk.PhotoImage(file="img_qtv/bg_khoa.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_qtv/btn_dangxuat.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_qtv/menu_thongke.png")
    img_menuthietlap=ImageTk.PhotoImage(file="img_qtv/menu_thietlap.png")
    img_menukhoa=ImageTk.PhotoImage(file="img_qtv/menu_khoa1.png")
    img_btnthem=ImageTk.PhotoImage(file="img_qtv/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_qtv/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_qtv/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_qtv/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_qtv/btn_khoiphuc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    
    tenkhoa=StringVar()
    ndtimkiem=StringVar()
    makhoa = StringVar()
    tengv=tengv_email(d[0])
    row=khoa.bangkhoa()
        
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

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=181)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=181)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=181)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=292)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc,bg="white")
    btnkhoiphuc.place(x=920,y=292)

 
    
    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)
    
    Label(bg,text="Trường Đại Học Cửu Long",font=("Baloo Tamma",11),fg="black",bg="white").place(x=578,y=90)
    
    Entry(bg,font=("Baloo Tamma",11),width=37,textvariable=tenkhoa,bd=0,highlightthickness=0).place(x=576,y=129)
    
    Entry(bg,font=("Baloo Tamma",11),width=27,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=656,y=292)

    tv = ttk.Treeview(bg, columns=(1,2,3), show="headings")
    tv.column(1, width=120,anchor=CENTER)
    tv.column(2, width=120,anchor=CENTER)
    tv.column(3, width=300)

    tv.heading(1,text="Số thứ tự")
    tv.heading(2,text="Mã khoa")
    tv.heading(3,text="Tên Khoa")
    tv.place(x=390,y=340)

    tv.bind('<Double 1>', getrow)
    
    update(row)
    win.mainloop()

if __name__ == '__main__':
    main()