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


def main():
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
        gvcu.set(item['values'][0])
        cacu.set(item['values'][4])
        dataca=str(item['values'][4])
        
        
        for i in range(5):
            if dataca.find(str(i)) != -1:
                ca[i].set(1)
            else:
                ca[i].set(0)

    def timkiem():
        return
        # malop=csdl.tenlop_thanh_ma(data_lop.get())
        # namhoc=csdl_admin.ma_namhoc(data_namhoc.get())
        
        # row=csdl_admin.timkiem_dongtkb(malop,ndtimkiem.get(),namhoc,data_hocky.get())
        # update(row)

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
        if len(data_ca)==2:
            ca1=data_ca[0:1]
            ca2=data_ca[1:2]
        else:
            ca1=ca2=data_ca

      

        if data_ca=="" or magv=="" or mamh=="" or ngay =="":
            messagebox.showerror("thông báo","Hãy chọn đầy đủ dữ liệu")
        elif(tkb.kt_lichgiang(magv,ngay,ca1) != [] or tkb.kt_lichgiang(magv,ngay,data_ca) != [] or tkb.kt_lichgiang(magv,ngay,ca2)!=[]):
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
        elif(tkb.kt_lich_tkb(malop,ngay,data_ca)!= [] or tkb.kt_lich_tkb(malop,ngay,ca1)!= [] or tkb.kt_lich_tkb(malop,ngay,ca2)!= []):
            messagebox.showerror("thông báo","Lớp đã có lịch học !")
        elif tkb.them_tkb(magv,mamh,pp,ngay,data_ca,malop,hki,namhoc):
            messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu ")
            khoiphuc()
        else:
            messagebox.showerror("thông báo", "Thêm thất bại")
            
            
    def sua():
        #dữ liệu chưa cập nhật
        ngay_cu=ngaycu.get()
        mon_cu=mamh_ten(moncu.get())
        gv_cu=magv_ten(gvcu.get())
        ca_cu=cacu.get()
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


        if len(data_ca)==2:
            ca1=data_ca[0:1]
            ca2=data_ca[1:2]
        else:
            ca1=ca2=data_ca
        
        if(ngaycu.get()== ""):
            messagebox.showerror("thông báo","không tìm thấy dữ liệu cần sửa ! Bạn hãy nhấn 2 lần vào dòng muốn sửa , rồi sửa dữ liệu và nhấn nút sửa")
        elif data_ca=="" or magv=="" or mamh=="" or ngay =="":
            messagebox.showerror("thông báo","Hãy chọn đầy đủ dữ liệu")
        elif(tkb.kt_lichgiang(magv,ngay,ca1) != [] or tkb.kt_lichgiang(magv,ngay,data_ca) != [] or tkb.kt_lichgiang(magv,ngay,ca2)!=[]):
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
        elif(tkb.kt_lich_tkb(malop,ngay,data_ca)!= [] or tkb.kt_lich_tkb(malop,ngay,ca1)!= [] or tkb.kt_lich_tkb(malop,ngay,ca2)!= []):
            messagebox.showerror("thông báo","Lớp đã có lịch học !")
        else:
            tkb.xoa_dong_tkb(ngay_cu,mon_cu,gv_cu,ca_cu)
            tkb.them_tkb(magv,mamh,pp,ngay,data_ca,malop,hki,namhoc)
            messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu")
            khoiphuc()
               
    def xoa():
        magv=magv_ten(data_gv.get())
        mamh = mamh_ten(data_mon.get())
        ngay=data_ngay.get()
        data_ca=""
        for i in range(len(ca)):
            if ca[i].get() >= 1:
                data_ca += str(i)
        if ngay=="":
            messagebox.showerror("thông báo","Không tìm thấy dữ liệu cần xoá.\n Bạn hãy nhấn 2 lần vào dòng muốn xoá và nhấn nút 'xoá'")
        elif tkb.xoa_dong_tkb(ngay,mamh,magv,data_ca) :
            messagebox.showinfo("thông báo","Đã xoá khỏi thời khoá biểu")
            khoiphuc()
        else:
            messagebox.showerror("thông báo","Lỗi")
  
    def chonngay(cal,btn):
        data_ngay.set(dinh_dang_ngay(cal.get_date()))
        cal.destroy()
        btn.destroy()
        lb.config(text="|")
        btnchonlich.config(command=chonlich)
    def chonlich():
        cal = Calendar(lb,selectmode="day",year=2021,month=8,day=16,bg="white")
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
    makhoa=makhoa_email(email)
    tengv=tengv_email(email)
   
    data_lop=StringVar()
    data_gv=StringVar()
    data_mon=StringVar()
    data_ngay=StringVar()
    data_namhoc=StringVar()
    data_hocky=StringVar()
    data_ngay.set("")
    data_ca=StringVar()
    data_matkb=StringVar()

    lop=tkb.lop_khoa(makhoa)
    gv=tkb.gv_khoa(makhoa)
    mon=tkb.mh_khoa(makhoa)
    ndtimkiem=StringVar()
    ngaycu=StringVar()
    cacu=StringVar()
    moncu=StringVar()
    gvcu=StringVar()
    data_loai=StringVar()
    hocky=[1,2]
    loai=["lý thuyết","thực hành"]
    namhoc=["2021-2022","2022-2022"]
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
    menutkb=Button(bg,image=img_menutkb,bd=0,highlightthickness=0)
    menutkb.place(x=30,y=296)
    menumonhoc=Button(bg,image=img_menumonhoc,bd=0,highlightthickness=0,command=menumonhoc)
    menumonhoc.place(x=30,y=380)
    menuthongke=Button(bg,image=img_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=30,y=461)

    Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    cbnam =Combobox(bg,textvariable=data_namhoc,font=("Times new roman",12), width=10,values=namhoc)
    cbnam.current(0)
    cbnam.bind('<<ComboboxSelected>>', capnhatbang)
    cbnam.place(x=410,y=5)


    cbhk =Combobox(bg,textvariable=data_hocky,font=("Times new roman",12), width=6, values=hocky)
    cbhk.current(0)
    cbhk.bind('<<ComboboxSelected>>', capnhatbang)
    cbhk.place(x=580,y=5)

    cbloai =Combobox(bg,textvariable=data_loai,font=("Times new roman",12), width=7,values=loai)
    cbloai.current(0)
    cbloai.place(x=825,y=120)

    cblop =Combobox(bg,textvariable=data_lop,font=("Times new roman",12), width=28,values=lop)
    cblop.current(0)
    cblop.bind('<<ComboboxSelected>>', capnhatbang)
    cblop.place(x=730,y=5)

    Label(bg,font=("Baloo Tamma",11),bg="white",textvariable=data_ngay).place(x=616,y=155)

    cbgv =Combobox(bg,textvariable=data_gv,font=("Times new roman",11), width=47,values=gv)
    cbgv.place(x=552,y=90)
    Frame(bg,width=300,height=2,bg="white").place(x=552,y=90)
    Frame(bg,width=3,height=23,bg="white").place(x=552,y=90)
    Frame(bg,width=300,height=2,bg="white").place(x=552,y=112)

    cbmon =Combobox(bg,textvariable=data_mon,font=("Times new roman",11), width=25,values=mon)
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
    tv.column(1, width=150,anchor=CENTER)
    tv.column(2, width=200,anchor=CENTER)
    tv.column(3, width=50)
    tv.column(4, width=100)
    tv.column(5, width=50,anchor=CENTER)


    tv.heading(1,text="Giảng Viên")
    tv.heading(2,text="Môn học")
    tv.heading(3,text="PP Giảng")
    tv.heading(4,text="Ngày")
    tv.heading(5,text="Ca")
    
    tv.place(x=380,y=370)
    tv.bind('<Double 1>', getrow)
   
    khoiphuc()

    win.mainloop()

if __name__ == '__main__':
    main()