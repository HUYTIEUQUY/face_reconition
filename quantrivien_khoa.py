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
import threading
import kt_nhap as kt


def main():
    def loaddl():
        tengv.set(tengv_email(d[0]))
        row=khoa.bangkhoa()
        lbgv.config(text=tengv.get())
        update(row)

    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)

    def kt_email(email):
        if email[len(email)-11:len(email)] == '@mku.edu.vn' and email[0] != '@':
            return True
        else:
            return False

    def them():
        makhoa=khoa.sl_khoa()
        e=email.get()
        ten=kt.xoa_khoangcach(tenkhoa.get())
        em=e.strip()
        tenemail= str(em)[0:em.index("@")]

        if ten=="" or e=="":
            messagebox.showwarning("thông báo","Hãy nhập dữ liệu đầy đủ")
        elif kt.kt_dau_khoangcach(ten) == False or kt.kt_dau_khoangcach(e)== False or kt.kt_kitudacbiet(ten) !="" or kt.kt_kitudacbiet(tenemail) !="":
            messagebox.showwarning("thông báo","Dữ liệu không hợp lệ")
        elif kt_email(email.get()) == False or kt.kt_dau_khoangcach(e)== False or kt.kt_dau_khoangcach_email(e) != -1 :
            messagebox.showwarning("thông báo","email không hợp lệ\n\nVí dụ email hợp lệ 'khoacntt@mku.edu.vn'")
        elif khoa.kt_tenkhoa(ten)!= []:
            messagebox.showerror("thông báo",ten +" đã tồn tại")
        elif messagebox.askyesno("thông báo","Hãy kiểm tra kỹ email vì không thể sửa đổi khi đã tạo tài khoản."):
            e=e.strip()
            tenemail= str(e)[0:e.index("@")]
            khoa.themkhoa(makhoa,ten,email.get())
            khoa.them_tk_khoa("admin"+tenemail, email.get(), makhoa)
            messagebox.showinfo("thông báo","Thêm '"+ten+"' thành công")
            khoiphuc()
        else: return

    def xoa():
        ten=tenkhoa.get()
        ma=makhoa.get()
        
        if ten=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu xoá. Bạn hãy click 2 lần vào dòng muốn xoá !")
        elif messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            if khoa.kt_lop_in_khoa(ma) == False:
                if khoa.xoakhoa(ma)==True and khoa.xoakhoa_bgv(ma)==True:
                    khoa.xoa_tk(email.get())
                    messagebox.showinfo("thông báo","Xoá '"+ten+"' thành công")
                    khoiphuc()
                else: 
                    messagebox.showerror("thông báo","Lỗi")
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
        elif email.get() != emailcu.get():
            messagebox.showwarning("thông báo","Không thể đổi tài khoản")
        elif kt_email(email.get())==False:
            messagebox.showwarning("thông báo","Email không hợp lệ\nVí dụ email hợp lệ 'khoacntt@mku.edu.vn' ")
        elif kt.kt_dau_khoangcach(tenmoi)== False or kt.kt_kitudacbiet(tenmoi) != "":
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
        email.set(item['values'][3])
        emailcu.set(item['values'][3])

    def khoiphuc():
        ndtimkiem.set("")
        tenkhoa.set("")
        email.set("")
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
    win.title("Quản lý khoa")
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
    tengv=StringVar()
    email=StringVar()
    emailcu=StringVar()

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

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=200)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=200)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=200)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=292)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc,bg="white")
    btnkhoiphuc.place(x=920,y=292)
    
    lbgv=Label(bg,font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    
    Label(bg,text="Đại Học Cửu Long",font=("Baloo Tamma",11),fg="black",bg="white").place(x=578,y=90)
    
    Entry(bg,font=("Baloo Tamma",11),width=37,textvariable=tenkhoa,bd=0,highlightthickness=0).place(x=576,y=129)
    Entry(bg,font=("Baloo Tamma",11),width=37,textvariable=email,bd=0,highlightthickness=0).place(x=576,y=163)
    
    Entry(bg,font=("Baloo Tamma",11),width=27,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=656,y=294)

    tv = ttk.Treeview(bg, columns=(1,2,3,4), show="headings")
    tv.column(1, width=80,anchor=CENTER)
    tv.column(2, width=80,anchor=CENTER)
    tv.column(3, width=200)
    tv.column(4, width=250)

    tv.heading(1,text="Số thứ tự")
    tv.heading(2,text="Mã khoa")
    tv.heading(3,text="Tên Khoa")
    tv.heading(4,text="Email khoa")
    tv.place(x=350,y=340)
    tv.bind('<Double 1>', getrow)
    
    threading.Thread(target=loaddl).start()

    win.mainloop()

if __name__ == '__main__':
    main()