from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
from backend.dl_giangvien import tengv_email
from backend.dl_khoa import sl_khoa ,khoa_co_quyen_all
import backend.dl_khoa as khoa
import quantrivien_thongke
import quantrivien_thietlap
import threading
import kt_nhap as kt
from styletable import style, update

def main():
    def loadding(a):
        if a == 1:# đang load dữ liệu
            lb_loadding.place(x=904,y=4)
            menudangxuat["state"] = "disabled"
            btnkhoiphuc["state"] = "disabled"
            btntimkiem["state"] = "disabled"
        else:
            lb_loadding.place_forget()
            menudangxuat["state"] = "normal"
            btnkhoiphuc["state"] = "normal"
            btntimkiem["state"] = "normal"

    def loaddl():
        tengv.set(tengv_email(d[0]))
        row=khoa.bangkhoa()
        lbgv.config(text=tengv.get())
        update(tv,row)
        loadding(0)

    def kt_email(email):
        if (email[len(email)-11:len(email)] =='@mku.edu.vn' or email[len(email)-10:len(email)] == '@gmail.com') and email[0] != '@':
            return True
        else:
            return False

    def them():
        loadding(1)
        q = option.get()
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
        elif khoa.kt_tenkhoa(makhoa,ten)!= []:
            messagebox.showerror("thông báo",ten +" đã tồn tại")
        elif messagebox.askyesno("thông báo","Hãy kiểm tra kỹ email vì không thể sửa đổi khi đã tạo tài khoản."):
            e=e.strip()
            tenemail= str(e)[0:e.index("@")]
            khoa.themkhoa(makhoa,ten,email.get(),q)
            khoa.them_tk_khoa("admin"+tenemail, email.get(), makhoa)
            messagebox.showinfo("thông báo","Thêm '"+ten+"' thành công")
            khoiphuc()
        else: loadding(0)
        loadding(0)

    # def xoa():
    #     ten=tenkhoa.get()
    #     ma=makhoa.get()
        
    #     if ten=="":
    #         messagebox.showwarning("thông báo","Chưa có dữ liệu xoá. Bạn hãy click 2 lần vào dòng muốn xoá !")
    #     elif messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
    #         if khoa.kt_lop_in_khoa(ma) == False:
    #             if khoa.xoakhoa(ma)==True and khoa.xoakhoa_bgv(ma)==True:
    #                 khoa.xoa_tk(email.get())
    #                 messagebox.showinfo("thông báo","Xoá '"+ten+"' thành công")
    #                 khoiphuc()
    #             else: 
    #                 messagebox.showerror("thông báo","Lỗi")
    #         else:
    #             messagebox.showerror("thông báo", "không thể xoá\nCó lớp tồn tại trong khoa")
    #     else:
    #         return

    def xoa():
        loadding(1)

        if tenkhoa.get() == "":
            messagebox.showwarning("thông báo","Hãy chọn dòng trong bảng phía dưới để xoá")
        elif messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            x=tv.selection()
            listma = []
            ko_xoa=[]
            for i in x:
                listma.append(tv.item(i,'values')[1])
            for i in listma:
                quyen = khoa_co_quyen_all(makhoa.get())

                if quyen == str(1) and khoa.kt_gv_in_khoa(i) == []:
                    if khoa.xoakhoa(i)==True:
                        threading.Thread(target=khoa.xoa_tk,args=(i,)).start()
                        threading.Thread(target=khoa.xoakhoa_bgv,args=(i,)).start()
                    else: 
                        messagebox.showerror("thông báo","Lỗi")
                elif quyen != str(1) and (khoa.kt_lop_in_khoa(i) == [] or khoa.kt_gv_in_khoa(i) == []):
                    if khoa.xoakhoa(i)==True:
                        threading.Thread(target=khoa.xoa_tk,args=(i,)).start()
                        threading.Thread(target=khoa.xoakhoa_bgv,args=(i,)).start()
                    else: 
                        messagebox.showerror("thông báo","Lỗi")
                else: ko_xoa.append(i)

            
            if(ko_xoa!=[]):
                messagebox.showwarning("thông báo","Không thể xoá khoa có mã "+str(ko_xoa))
            else:
                messagebox.showinfo("thông báo","Đã xoá thành công")
                khoiphuc()
        else: loadding(0)
        loadding(0)

    def sua():
        loadding(1)
        tenmoi=tenkhoa.get()
        makhoa1=makhoa.get()
        q = option.get()
        if tenmoi=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu cập nhật")
        elif makhoa.get() == "":
            messagebox.showwarning("thông báo","Chưa có dữ liệu cập nhật, Bạn hãy click vào dòng cần cập nhật")
        elif len(x) >1:
            messagebox.showwarning("thông báo","Hãy chọn một dòng để cập nhật")
        elif email.get() != emailcu.get():
            messagebox.showwarning("thông báo","Không thể đổi tài khoản")
        elif kt_email(email.get())==False:
            messagebox.showwarning("thông báo","Email không hợp lệ\nVí dụ email hợp lệ 'khoacntt@mku.edu.vn' ")
        elif kt.kt_dau_khoangcach(tenmoi)== False or kt.kt_kitudacbiet(tenmoi) != "":
            messagebox.showwarning("thông báo","Dữ liệu tên lớp không hợp lệ")
        elif khoa.kt_tenkhoa(makhoa1,tenmoi)!= []:
            messagebox.showerror("thông báo",tenmoi+" đã tồn tại")
        else:
            khoa.suakhoa(makhoa1,tenmoi,q)
            messagebox.showinfo("thông báo","Đã cập nhật thông tin khoa thành công")
            khoiphuc()
        loadding(0)
            
    def getrow(event):
        global x
        x=tv.selection()
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        tenkhoa.set(item['values'][2])
        makhoa.set(item['values'][1])
        email.set(item['values'][3])
        emailcu.set(item['values'][3])
        if str(item['values'][4]) == str(1):
            option.set(1)
        else:
            option.set(0)

    def khoiphuc():
        ndtimkiem.set("")
        tenkhoa.set("")
        email.set("")
        row=khoa.bangkhoa()
        update(tv,row)
        option.set(0)


    def timkiem():
        row=khoa.timkhoa(ndtimkiem.get())
        update(tv,row)

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
    win.iconbitmap(r"img/iconphanmem.ico")
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
    option=IntVar()
    option.set(0)

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
    btnthem.place(x=487,y=185)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0, command=sua)
    btnsua.place(x=637,y=185)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=185)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,activebackground="white",command=timkiem)
    btntimkiem.place(x=881,y=245)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground="white",command=khoiphuc,bg="white")
    btnkhoiphuc.place(x=920,y=245)
    
    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",13),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)

    Checkbutton(bg,text="Có thể giảng dạy tất cả các lớp",font=("Baloo Tamma 2 Medium",12),variable=option,bg="#F4E1EC",fg="#5F1965").place(x=570,y=132)

    
    Label(bg,text="Đại Học Cửu Long",font=("Baloo Tamma 2 Medium",10),fg="black",bg="white").place(x=578,y=22)
    
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=33,textvariable=tenkhoa,bd=0,highlightthickness=0).place(x=576,y=58)
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=33,textvariable=email,bd=0,highlightthickness=0).place(x=576,y=92)
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=25,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=656,y=246)

    style()
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=328,y=300)

    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=50,anchor=CENTER)
    tv.column(2, width=80,anchor=CENTER)
    tv.column(3, width=250)
    tv.column(4, width=250)

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="MÃ KHOA")
    tv.heading(3,text="TÊN KHOA")
    tv.heading(4,text="EMAIL KHOA")
    tv.pack()
    tree_scroll.config(command=tv.yview)
    tv.bind('<ButtonRelease-1>', getrow)
    tv.tag_configure("ollrow" ,background="white",font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))
    lb_loadding=Label(bg,text=" Đang tải . . . ", font=("Baloo Tamma 2 Medium",12),bg="#E7DFF1",fg="#AD7B98", width=12)
    loadding(1)
    threading.Thread(target=loaddl).start()

    win.mainloop()

if __name__ == '__main__':
    main()