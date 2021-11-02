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
import admin_tkb1
import admin_thongke
import admin_monhoc
from backend.dl_khoa import khoa_co_quyen_all
import backend.dl_giangvien as gv
from backend.dl_giangvien import email_ma, tengv_email,makhoa_email
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
            btnthem["state"] = "disabled"
            btnsua["state"] = "disabled"
            btnxoa["state"] = "disabled"
            btnghichu["state"] = "disabled"
        else:
            lb_loadding.place_forget()
            menudangxuat["state"] = "normal"
            btnkhoiphuc["state"] = "normal"
            btntimkiem["state"] = "normal"
            btnthem["state"] = "normal"
            btnsua["state"] = "normal"
            btnxoa["state"] = "normal"
            btnghichu["state"] = "normal"
    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        makhoa.set(makhoa_email(d[0]))
        tengv.set(tengv_email(d[0]))
        lbgv.config(text=tengv.get())
        khoiphuc()    

    def khoiphuc():
        loadding(1)
        ndtimkiem.set("")
        data_email.set("")
        data_ma.set("")
        data_magv.set("")
        data_ten.set("")
        data_sdt.set("")
        data_ghichu.set("")
        row=gv.banggv(makhoa.get())
        update(tv,row)
        try:
            trolai()
        except:return
        loadding(0)

    def kt_email(email):
        if (email[len(email)-11:len(email)] == '@mku.edu.vn' or email[len(email)-10:len(email)] == '@gmail.com') and email[0] != '@':
            return True
        else:
            return False

    def them():
        loadding(1)
        ma=data_ma.get()
        ten=data_ten.get()
        ten=kt.xoa_khoangcach(ten)
        sdt=data_sdt.get()
        ghichu=data_ghichu.get()
        emailgv=data_email.get()
        if ma =="" or ten == "" or sdt=="" or emailgv=="":
            messagebox.showwarning("thông báo","Bạn hãy nhập đầy đủ dữ liệu")
        elif len(ma) != 8 or ma.isnumeric()== False:
            messagebox.showwarning("thông báo","Mã giảng viên phải 8 kí tự và là số")
        elif len(sdt) !=10 or sdt.isnumeric()== False:
            messagebox.showwarning("thông báo","Số điện thoại không đúng")
        elif kt.kt_dau_khoangcach(ten)==False or kt.kt_kitudacbiet(ten) != "":
            messagebox.showwarning("thông báo","Dữ liệu tên giảng viên không hợp lệ")
        elif kt_email(emailgv) == False or kt.kt_dau_khoangcach(emailgv)== False or kt.kt_dau_khoangcach_email(emailgv) != -1 :
            messagebox.showwarning("thông báo","email không hợp lệ\n\nVí dụ email hợp lệ 'nguyenhuuthe@mku.edu.vn'")
        elif messagebox.askyesno("thông báo","Hãy kiểm tra kỹ email vì không thể sửa đổi khi đã tạo tài khoản."):
            if gv.kt_ma(ma) == []:
                gv.themgv(ma,ten,emailgv,sdt,ghichu,makhoa.get())
                messagebox.showinfo("thông báo","Đã thêm giảng viên vào danh sách")
                khoiphuc()
            else:
                messagebox.showerror("thông báo","Mã giảng viên đã tồn tại trong danh sách")
        loadding(0)
                
    def sua():
        loadding(1)
        
        if data_ma.get() != data_magv.get():
            messagebox.showwarning("thông báo","khổng thể sửa mã")
            data_ma.set(data_magv.get())
        elif data_magv.get()=="":
            messagebox.showwarning("thông báo","Chưa có dữ liệu sửa. Bạn hãy click vào dòng muốn sửa !")
        elif len(x) > 1:
            messagebox.showwarning("Thồng báo","Hãy chọn một dòng để cập nhật")
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
        loadding(0)

    def xoa():
        loadding(1)
        if data_magv.get()=="":
            messagebox.showwarning("thông báo","Hãy chọn dòng trong bảng phía dưới để xoá")
        elif messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            x=tv.selection()
            listma = []
            ko_xoa=[]
            for i in x:
                listma.append(tv.item(i,'values')[1])
            for i in listma:
                if gv.kt_gv_tontai_tkb(i) ==[] and gv.kt_gv_tontai_diemdanh(i)==[]:
                    tenemail=email_ma(i)
                    threading.Thread(target=gv.xoa_tk, args=(tenemail,)).start()
                    threading.Thread(target=gv.xoagv, args=(i,)).start()
                    luong(khoiphuc)
                
                else: ko_xoa.append(i)

            if(ko_xoa!=[]):
                messagebox.showwarning("thông báo","Không thể xoá giảng viên có mã "+str(ko_xoa))
            else:
                messagebox.showinfo("thông báo","Đã xoá thành công")
                khoiphuc()
        else: loadding(0)
        loadding(0)

    def getrow(event):
        global x
        x = tv.selection()
        rowid=tv.identify_row(event.y)
        txt_ghichu.delete(1.0,END)
        item=tv.item(tv.focus())
        data_ma.set(item['values'][1])
        data_magv.set(item['values'][1])
        data_ten.set(item['values'][2])
        data_email.set(item['values'][3])
        data_sdt.set(str(item['values'][4]))
        data_ghichu.set(item['values'][5])
        txt_ghichu.insert(END,item['values'][5])
        sdt=gv.sdt_ma(data_ma.get())
        data_sdt.set(sdt)
    
    def timkiem():
        loadding(1)
        row=gv.tim_gv(makhoa.get(),ndtimkiem.get())
        if row == []:
            messagebox.showinfo("thông báo","Không tìm thấy kết quả")
            update(tv,row)
        else:
            update(tv,row)
        loadding(0)

    def xem_ghichu():
        if data_magv.get() != "":
            frame_ghichu.config(bg="white")
            lb_ghichu.config(text="Ghi chú",background="white")
            txt_ghichu.pack(padx=20)
            btn_trolai.pack(side="right",padx=10,pady=10)
            btn_luu.pack(side="right",padx=10,pady=10)
        else: messagebox.showwarning("thông báo","Giảng viên không có ghi chú")
    
    def trolai():
        frame_ghichu.config(bg="#E8DFF1")
        lb_ghichu.config(text=".",fg="#A672BB",bg="#E8DFF1")
        txt_ghichu.pack_forget()
        btn_trolai.pack_forget()
        btn_luu.pack_forget()

    def luu_ghichu():
        if gv.luughichu(data_magv.get(),txt_ghichu.get("1.0",END)):
            luong(khoiphuc)
            messagebox.showinfo("thông báo","Đã lưu ghi chú")

        else: 
             messagebox.showerror("thông báo","Lưu không thành công")
    def menuthongke():
        win.destroy()
        admin_thongke.main()
    def menulophoc():
        win.destroy()
        adminlop.main()
    def menutkb():
        quyen = khoa_co_quyen_all(makhoa.get())
        win.destroy()
        if quyen== str(1):
            admin_tkb1.main()
        else:
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
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    img_btnghichu = ImageTk.PhotoImage(file="img_admin/btn_ghichu.png")
    img_btnluu = ImageTk.PhotoImage(file="img_admin/btnluu.png")
    img_btntrove = ImageTk.PhotoImage(file="img_admin/btn_trolai1.png")

    
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

    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=31,textvariable=data_ma,bd=0,highlightthickness=0).place(x=575,y=17)
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=31,textvariable=data_ten,bd=0,highlightthickness=0).place(x=575,y=51)
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=31,textvariable=data_sdt,bd=0,highlightthickness=0).place(x=575,y=84)
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=31,textvariable=data_email,bd=0,highlightthickness=0).place(x=575,y=119)
    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=21,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=251)

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
    btnghichu=Button(bg,image=img_btnghichu,bd=0,highlightthickness=0,activebackground='white',command=xem_ghichu)
    btnghichu.place(x=948,y=4)

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
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5,6),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=30,anchor=CENTER)
    tv.column(2, width=90,anchor=CENTER)
    tv.column(3, width=140)
    tv.column(4, width=240)
    tv.column(5, width=110,anchor=CENTER)
    tv.column(6, width=0,stretch='no')

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="MÃ GV")
    tv.heading(3,text="TÊN GIẢNG VIÊN")
    tv.heading(4,text="EMAIL")
    tv.heading(5,text="SỐ ĐIỆN THOẠI")
    tv.heading(6,text="Ghi chú")
    tv.pack()
    tree_scroll.config(command=tv.yview)
    tv.bind('<ButtonRelease-1>', getrow)
    tv.tag_configure("evenrow" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("ollrow" ,background="#ECECEC",foreground="red",font=("Baloo Tamma 2 Medium",10))
    
    frame_ghichu=Frame(bg,background="#E8DFF1")
    frame_ghichu.place(x=357,y=5)
    lb_ghichu=Label(frame_ghichu,font=("Baloo Tamma 2 Medium",14),fg="#A672BB")
    lb_ghichu.pack()
    txt_ghichu=Text(frame_ghichu,width=60,height=6,bd=1,background="#F1F1F1",font=("Baloo Tamma 2 Medium",10))
    btn_trolai= Button(frame_ghichu,image=img_btntrove,bd=0,highlightthickness=0,activebackground="white",command=trolai)
    btn_luu= Button(frame_ghichu,image=img_btnluu,bd=0,highlightthickness=0,activebackground="white",command=luu_ghichu)
    
    lb_loadding=Label(bg,text=" Đang tải . . . ", font=("Baloo Tamma 2 Medium",11),bg="#FFF4FF",fg="#AD7B98", width=14)
    loadding(1)
    luong(loaddl)
    win.mainloop()
   
if __name__ == '__main__':
    main()