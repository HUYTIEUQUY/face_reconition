from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
from tkinter import messagebox
import dangnhap
import socket
import adminlop
import admin_giangvien
import admin_thongke
import admin_monhoc
from backend.dl_giangvien import tengv_email,makhoa_email,magv_ten
import backend.dl_tkb as tkb
from backend.dl_adminlop import malop_ten
from backend.dl_monhoc import mamh_ten
import threading
import datetime

def main():
    def luong(ham):
        threading.Thread(target=ham).start()
    def loaddl():
        makhoa.set(makhoa_email(email))
        tengv.set(tengv_email(email))
        lbgv.config(text=tengv.get())
        lop=tkb.lop_khoa(makhoa.get())
        gv=tkb.gv_khoa(makhoa.get())
        mon=tkb.mh_khoa(makhoa.get())
        namhoc=tkb.namhoc()
        #set cho combobox to
        cblop.config(values=lop)
        cblop.current(0)
        cbmon.config(values=mon)
        cbgv.config(values=gv)
        cbnam.config(values=namhoc)
        cbnam.current(0)
        khoiphuc()


    def dinh_dang_ngay(ngay):
        ngay=str(ngay).replace("/"," ")
        ngay=str(ngay).replace("-"," ")
        d=ngay.split()
        if len(d[0])==1:
            d[0]="0"+d[0]
        if len(d[1])==1:
            d[1]="0"+d[1]
        if len(d[2]) ==4 :
            ngay=d[0]+"/"+d[1]+"/"+d[2]
        else:
            ngay=d[1]+"/"+d[0]+"/20"+d[2]
        return ngay

    def update(row):
        tv.delete(*tv.get_children())
        for i in row:
            tv.insert('','end',values=i)

    def capnhatbang(event):
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        row=tkb.bang_tkb(malop,namhoc,data_hocky.get())
        update(row)

    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        data_ngay.set(item['values'][3])
        data_mon.set(item['values'][1])
        data_gv.set(item['values'][0])
        data_ca.set(item['values'][4])

        ngaycu.set(item['values'][3])
        moncu.set(item['values'][1])
        pp_giangcu.set(item['values'][2])
        gvcu.set(item['values'][0])
        cacu.set(item['values'][4])
        dataca=str(item['values'][4])
        
        for i in range(5):
            if dataca.find(str(i)) != -1:
                ca[i].set(1)
            else:
                ca[i].set(0)

    def timkiem():
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        row=tkb.timkiem_dong_tkb(malop,namhoc,data_hocky.get(),ndtimkiem.get())
        update(row)

    def kt_lich_gv(magv, ngay, ca):
        data_ca1= " "
        data_ca=data_ca1.join(ca).split()
        tam=[]
        for i in data_ca:
            if tkb.kt_lichgiang(magv,ngay,i) !=[]:
                tam.append(i)
        return tam
    def kt_lich_lop(malop, ngay, ca):
        data_ca1= " "
        data_ca=data_ca1.join(ca).split()
        tam=[]
        for i in data_ca:
            if tkb.kt_lich_tkb(malop,ngay,i) !=[]:
                tam.append(i)
        return tam



    def khoiphuc():
        ngaycu.set("")
        moncu.set("")
        gvcu.set("")
        cacu.set("")
        ndtimkiem.set("")
        data_ca.set("")
        data_gv.set("")
        data_mon.set("")
        data_ngay.set("")
        for i in range(5):
            ca[i].set(0)
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        row=tkb.bang_tkb(malop,namhoc,data_hocky.get())
        update(row)

    def them():
        malop=malop_ten(data_lop.get())
        magv=magv_ten(data_gv.get())
        mamh =mamh_ten(data_mon.get())
        ngay=data_ngay.get()
        namhoc=tkb.manh_ten(data_namhoc.get())
        hki=data_hocky.get()
        pp=data_loai.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        
        if data_ca=="" or magv=="" or mamh=="" or ngay =="":
            messagebox.showerror("thông báo","Hãy chọn đầy đủ dữ liệu")
        elif tkb.ngaya_nhohon_ngayb(ngay,now) ==True:
            messagebox.showerror("thông báo","Ngày phải lớn hơn ngày hôm nay")
        elif kt_lich_gv(magv,ngay,data_ca) !=[]:
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
        elif kt_lich_lop(malop,ngay,data_ca) != []:
            messagebox.showerror("thông báo","Lớp đã có lịch học !")
        elif tkb.them_tkb(magv,mamh,pp,ngay,data_ca,malop,hki,namhoc):
            messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu ")
            luong(khoiphuc)
        else:
            messagebox.showerror("thông báo", "Thêm thời khoá biểu không thành công")
            
            
    def sua():
        #dữ liệu chưa cập nhật
        ngay_cu=ngaycu.get()
        mon_cu=mamh_ten(moncu.get())
        gv_cu=magv_ten(gvcu.get())
        ca_cu=cacu.get()
        pp_giang=pp_giangcu.get()
        
        if tkb.xoa_dong_tkb(gv_cu,mon_cu,ngay_cu,ca_cu,pp_giang):

            # 
            #du liệu cập nhật
            malop=malop_ten(data_lop.get())
            magv=magv_ten(data_gv.get())
            mamh = mamh_ten(data_mon.get())
            ngay=data_ngay.get()
            namhoc=tkb.manh_ten(data_namhoc.get())
            hki=data_hocky.get()
            pp=data_loai.get()
            data_ca=""
            for i in range(len(ca)):
                if ca[i].get() >= 1:
                    data_ca += str(i)


            
            
            if(ngaycu.get()== ""):
                messagebox.showerror("thông báo","không tìm thấy dữ liệu cần sửa ! Bạn hãy nhấn 2 lần vào dòng muốn sửa , rồi sửa dữ liệu và nhấn nút sửa")
            elif data_ca=="" or magv=="" or mamh=="" or ngay =="":
                messagebox.showerror("thông báo","Hãy chọn đầy đủ dữ liệu")
            elif tkb.ngaya_nhohon_ngayb(ngay,now) ==True:
                messagebox.showerror("thông báo","Ngày phải lớn hơn ngày hôm nay")
            elif kt_lich_gv(magv,ngay,data_ca) !=[]:
                messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
            elif kt_lich_lop(malop,ngay,data_ca) != []:
                messagebox.showerror("thông báo","Lớp đã có lịch học !")
            else:
                
                tkb.them_tkb(magv,mamh,pp,ngay,data_ca,malop,hki,namhoc)
                messagebox.showinfo("thông báo", "Đã sửa thành công")
                luong(khoiphuc)
        else: 
            messagebox.showwarning("Thông báo","Đã điểm danh không thể sửa")
               
    def xoa():
        magv=magv_ten(data_gv.get())
        mamh = mamh_ten(data_mon.get())
        ngay=data_ngay.get()
        pp=pp_giangcu.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        
        if messagebox.askyesno("Thông báo","Bạn có thật sự muốn xoá"):
            if ngay=="":
                messagebox.showerror("thông báo","Không tìm thấy dữ liệu cần xoá.\n Bạn hãy nhấn 2 lần vào dòng muốn xoá và nhấn nút 'xoá'")
            elif tkb.xoa_dong_tkb(magv,mamh,ngay,data_ca,pp) == True:
                messagebox.showinfo("thông báo","Đã xoá khỏi thời khoá biểu")
                luong(khoiphuc)
            else:
                messagebox.showerror("thông báo","Không thể xoá")
        else:
            return
  
    def chonngay(cal,btn):
        data_ngay.set(dinh_dang_ngay(cal.get_date()))
        cal.destroy()
        btn.destroy()
        lb.config(text="|")
        btnchonlich.config(command=chonlich)
    def chonlich():
        cal = Calendar(lb,selectmode="day",year=int(lich[2]),month=int(lich[1]),day=int(lich[0]),bg="white")
        cal.pack()
        btn=Button(f,image=img_btnchon,bg="white",command=lambda:chonngay(cal,btn),bd=0,highlightthickness=0)
        btn.pack()
        btnchonlich.config(command=tam)

    def tam():
        return
    
    def menuthongke():
        win.destroy()
        admin_thongke.main()
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
    win.title("Thời khoá biểu")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_chitiettkb.png")

    img_menudangxuat=ImageTk.PhotoImage(file="img_admin/btn_dangxuat.png")
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb1.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    img_btnchonlich=ImageTk.PhotoImage(file="img_admin/chonlich.png")
    img_btnchon=ImageTk.PhotoImage(file="img_admin/btn_chon.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")

    
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=StringVar()
    tengv=StringVar()
    tengv.set("")
   
    data_lop=StringVar()
    data_gv=StringVar()
    data_mon=StringVar()
    data_ngay=StringVar()
    data_namhoc=StringVar()
    data_hocky=StringVar()
    data_ngay.set("")
    data_ca=StringVar()
    data_matkb=StringVar()
    
    ndtimkiem=StringVar()
    ngaycu=StringVar()
    cacu=StringVar()
    moncu=StringVar()
    gvcu=StringVar()
    pp_giangcu=StringVar()
    data_loai=StringVar()
    hocky=[1,2]
    loai=["Lý thuyết","Thực hành"]
    x= datetime.datetime.now()
    now = dinh_dang_ngay(x.strftime("%x"))
    lich= now.replace("/"," ").split()
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menudangxuat=Button(bg,image=img_menudangxuat,bd=0,highlightthickness=0,command=menudangxuat)
    menudangxuat.place(x=248,y=44)
    menulophoc=Button(bg,image=img_menulophoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menulophoc)
    menulophoc.place(x=30,y=128)
    menugiangvien=Button(bg,image=img_menugiangvien,bd=0,highlightthickness=0,activebackground='#857EBD',command=menugiangvien)
    menugiangvien.place(x=30,y=212)
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0,activebackground='#857EBD')
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,activebackground='#857EBD',command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=30,y=461)

    lbgv=Label(bg,font=("Baloo Tamma",14),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)

    cbnam =Combobox(bg,textvariable=data_namhoc,font=("Times new roman",12), width=10,state='readonly')
    cbnam.bind('<<ComboboxSelected>>', capnhatbang)
    cbnam.place(x=410,y=5)
    Frame(bg,width=102,height=2,bg="white").place(x=410,y=5)
    Frame(bg,width=3,height=23,bg="white").place(x=410,y=5)
    Frame(bg,width=102,height=2,bg="white").place(x=410,y=28)


    cbhk =Combobox(bg,textvariable=data_hocky,font=("Times new roman",12), width=8, state='readonly', values=hocky)
    cbhk.current(0)
    cbhk.bind('<<ComboboxSelected>>', capnhatbang)
    cbhk.place(x=583,y=5)
    Frame(bg,width=87,height=2,bg="white").place(x=582,y=5)
    Frame(bg,width=3,height=23,bg="white").place(x=582,y=5)
    Frame(bg,width=87,height=2,bg="white").place(x=582,y=28)

    cbloai =Combobox(bg,textvariable=data_loai,font=("Times new roman",12),state='readonly', width=7,values=loai)
    cbloai.current(0)
    cbloai.place(x=825,y=120)
    Frame(bg,width=81,height=2,bg="white").place(x=825,y=120)
    Frame(bg,width=3,height=23,bg="white").place(x=825,y=120)
    Frame(bg,width=81,height=2,bg="white").place(x=825,y=143)

    cblop =Combobox(bg,textvariable=data_lop,font=("Times new roman",12),state='readonly', width=30)
    cblop.bind('<<ComboboxSelected>>', capnhatbang)
    cblop.place(x=730,y=5)
    Frame(bg,width=262,height=2,bg="white").place(x=730,y=5)
    Frame(bg,width=3,height=23,bg="white").place(x=730,y=5)
    Frame(bg,width=262,height=2,bg="white").place(x=730,y=28)

    Label(bg,font=("Baloo Tamma",11),bg="white",textvariable=data_ngay).place(x=616,y=155)

    cbgv =Combobox(bg,textvariable=data_gv,font=("Times new roman",11),state='readonly', width=47)
    cbgv.place(x=552,y=90)
    Frame(bg,width=353,height=2,bg="white").place(x=552,y=90)
    Frame(bg,width=3,height=23,bg="white").place(x=552,y=90)
    Frame(bg,width=353,height=2,bg="white").place(x=552,y=112)

    cbmon =Combobox(bg,textvariable=data_mon,font=("Times new roman",11),state='readonly', width=25)
    cbmon.place(x=552,y=124)
    Frame(bg,width=200,height=2,bg="white").place(x=552,y=124)
    Frame(bg,width=3,height=23,bg="white").place(x=552,y=124)
    Frame(bg,width=200,height=2,bg="white").place(x=552,y=146)
    ca=[]
    for i in range(5):
        option=IntVar()
        option.set(0)
        ca.append(option)

    Entry(bg,font=("Baloo Tamma",11),width=28,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=652,y=318)

    Checkbutton(bg,text="Ca 1",font=("Times new roman",11),variable=ca[1],bg="white").place(x=605,y=187)
    Checkbutton(bg,text="Ca 2",font=("Times new roman",11),variable=ca[2],bg="white").place(x=680,y=187)
    Checkbutton(bg,text="Ca 3",font=("Times new roman",11),variable=ca[3],bg="white").place(x=755,y=187)
    Checkbutton(bg,text="Ca 4",font=("Times new roman",11),variable=ca[4],bg="white").place(x=820,y=187)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=them)
    btnthem.place(x=487,y=247)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=247)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=247)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,command=timkiem)
    btntimkiem.place(x=881,y=313)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,command=khoiphuc)
    btnkhoiphuc.place(x=920,y=313)

    f=Frame(bg)
    f.place(x=320,y=30)
    lb=Label(f)
    lb.pack()

    btnchonlich=Button(bg,image=img_btnchonlich,bd=0,highlightthickness=0,command=chonlich)
    btnchonlich.place(x=858,y=155)

    tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    tv.column(1, width=150)
    tv.column(2, width=200)
    tv.column(3, width=50)
    tv.column(4, width=100)
    tv.column(5, width=50,anchor=CENTER)


    tv.heading(1,text="Giảng Viên")
    tv.heading(2,text="Môn học")
    tv.heading(3,text="PP Giảng")
    tv.heading(4,text="Ngày")
    tv.heading(5,text="Ca")
    
    tv.place(x=380,y=360)
    tv.bind('<Double 1>', getrow)
   
    luong(loaddl)

    win.mainloop()

if __name__ == '__main__':
    main()