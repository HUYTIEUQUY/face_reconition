from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
# import csdl
# import csdl_admin
from tkinter import messagebox
import dangnhap
import socket
import admin_giangvien
import admin_thongke
import admin_tkb
import admin_monhoc
from backend.dl_giangvien import tengv_email,makhoa_email
from backend.dl_khoa import tenkhoa
import backend.dl_adminlop as lop
import kt_nhap as kt
import threading
from styletable import style, update

def main():
    def loaddl():
        tengv.set(tengv_email(email))
        makhoa.set(makhoa_email(email))
        tenk.set(tenkhoa(makhoa.get()))
        lbgv.config(text=tengv.get())
        lbtk.config(text=tenk.get())
        luong(khoiphuc())
        

    def luong(ham):
        threading.Thread(target=ham).start()



    def them():
        ma=lop.malop()
        ten=tenlop.get()
        ten=kt.xoa_khoangcach(ten)
        if ten=="":
            messagebox.showwarning("thông báo","Hãy nhập dữ liệu đầy đủ")
        # else:
            
        elif kt.kt_dau_khoangcach(ten)== False or kt.kt_kitudacbiet(ten) != "":
            messagebox.showwarning("thông báo","Dữ liệu tên lớp không hợp lệ")
        elif lop.kt_tenlop(ten)!= []:
            messagebox.showerror("thông báo",ten +" đã tồn tại")
        else:
            lop.themlop(ma,ten,makhoa.get())
            messagebox.showinfo("thông báo","Thêm '"+ten+"' thành công")
            khoiphuc()



    def xoa():
        if messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            x=tv.selection()
            listma = []
            ko_xoa=[]
            for i in x:
                listma.append(tv.item(i,'values')[1])
            for i in listma:
                if lop.kt_lop_tontai_diemdanh(i) == [] and lop.kt_lop_tontai_tkb(i)==[] and lop.kt_sv_tontai_lop(i)==[]:
                    if lop.xoalop(i)==True:
                        luong(khoiphuc)
                    else:
                        ko_xoa.append(i)

                else:ko_xoa.append(i)
                    
            if(ko_xoa!=[]):
                messagebox.showwarning("thông báo","Không thể xoá lớp có mã "+str(ko_xoa))
                luong(khoiphuc)
            else:
                messagebox.showinfo("thông báo","Đã xoá thành công")
                luong(khoiphuc)
        else: return

    def sua():
        tenmoi=tenlop.get()
        tenmoi= kt.xoa_khoangcach(tenmoi)
        malop1=malop.get()
        if tenmoi=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu cập nhật")
        elif malop.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu cập nhật, Bạn hãy click 2 lần vào dòng cần cập nhật")
        elif kt.kt_dau_khoangcach(tenmoi)== False or kt.kt_kitudacbiet(tenmoi)!= "":
            messagebox.showwarning("thông báo","Dữ liệu tên lớp không hợp lệ")
        elif lop.kt_tenlop(tenmoi)!= []:
            messagebox.showerror("thông báo",tenmoi+" đã tồn tại")
        else:
            lop.sualop(malop1,tenmoi)
            messagebox.showinfo("thông báo","Đã đổi tên lớp thành công")
            khoiphuc()
            
    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        tenlop.set(item['values'][2])
        malop.set(item['values'][1])
        
    def khoiphuc():
        ndtimkiem.set("")
        tenlop.set("")
        row=lop.banglop(makhoa.get())
        update(tv,row)

    def timkiem():
        row=lop.timlop(makhoa.get(),ndtimkiem.get())
        update(tv,row)

    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menutkb():
        win.destroy()
        admin_tkb.main()
    def menugiangvien():
        win.destroy()
        admin_giangvien.main()
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
    win.title("Lớp học")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_lop.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc1.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=StringVar()
    tengv=StringVar()
    tenlop=StringVar()
    malop=StringVar()
    ndtimkiem=StringVar()

    tenk=StringVar()


        
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,activebackground='#857EBD')
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,activebackground='#857EBD',command=menugiangvien)
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,activebackground='#857EBD',command=menutkb)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=30,y=461)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=181)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=181)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=181)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,activebackground='white',command=timkiem)
    btntimkiem.place(x=881,y=250)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground='white',command=khoiphuc,bg="white")
    btnkhoiphuc.place(x=920,y=250)

 
    
    lbgv=Label(bg,font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)
    
    lbtk=Label(bg,font=("Baloo Tamma",11),fg="black",bg="white")
    lbtk.place(x=580,y=62)
    
    Entry(bg,font=("Baloo Tamma",11),width=37,textvariable=tenlop,bd=0,highlightthickness=0).place(x=585,y=100)
    
    Entry(bg,font=("Baloo Tamma",11),width=27,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=656,y=253)

    # tạo stype cho bảng
    style()
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=368,y=300)

    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
    tv = ttk.Treeview(fr_tb, columns=(1,2,3),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=120,anchor=CENTER)
    tv.column(2, width=120,anchor=CENTER)
    tv.column(3, width=300)

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="SỐ THỨ TỰ")
    tv.heading(2,text="MÃ lỚP")
    tv.heading(3,text="TÊN LỚP")
    tv.pack()
    tv.bind('<Double 1>', getrow)
    tv.tag_configure("ollrow" ,background="white")
    tv.tag_configure("evenrow" ,background="#ECECEC")
    
    luong(loaddl)
    
    win.mainloop()

if __name__ == '__main__':
    main()