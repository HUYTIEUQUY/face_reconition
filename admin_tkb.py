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
from backend.dl_monhoc import mamh_ten,tenmh_ma
from backend.dl_khoa import khoa_co_quyen_all
import threading
import datetime
from styletable import style, update
from time import strftime,sleep


def main():
    def loadding(a):
        if a == 1:# đang load dữ liệu
            menudangxuat["state"] = "disabled"
            btnkhoiphuc["state"] = "disabled"
            btntimkiem["state"] = "disabled"
            btnthem["state"] = "disabled"
            btnsua["state"] = "disabled"
            btnxoa["state"] = "disabled"
        else:
            menudangxuat["state"] = "normal"
            btnkhoiphuc["state"] = "normal"
            btntimkiem["state"] = "normal"
            btnthem["state"] = "normal"
            btnsua["state"] = "normal"
            btnxoa["state"] = "normal"
    def load_bang_tkb(row):
        tv.delete(*tv.get_children())
        gan.set(1)
        global dem
        dem = 0
        for i in row:
            i[2]=tenmh_ma(i[2])
            if dem%2==0:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
            else:tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
            dem += 1
            if gan.get() == str(0):break
        loadding(0)
    def luong(ham):
        threading.Thread(target=ham).start()
    def loaddl():
        makhoa.set(makhoa_email(email))
        tengv.set(tengv_email(email))
        lbgv.config(text=tengv.get())
        global Quyen
        quyen=khoa_co_quyen_all(makhoa.get())
        if quyen == str(1):
            lop = tkb.all_lop()
        else:lop=tkb.lop_khoa(makhoa.get())

        gv=tkb.gv_khoa(makhoa.get())
        mon=tkb.mh_khoa(makhoa.get())
        namhoc=tkb.namhoc()
        #set cho combobox to
        cblop.config(values=lop)
        cblop.current(0)
        cbmon.config(values=mon)
        cbgv.config(values=gv)
        cbgv.current(0)
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

    def cong_ngay(tg,songay):
        a=tg.split('/')
        b=a[0]+"/"+a[1]+"/"+str(a[2])[2:4]
        d1 = datetime.datetime.strptime(b, "%d/%m/%y")
        d=d1 + datetime.timedelta(days=songay)
        d=str(d).split()
        ngaydinhdang=str(d[0]).split("-")
        ngay=ngaydinhdang[2]+"/"+ngaydinhdang[1]+"/"+ngaydinhdang[0]
        return ngay

    def capnhatbang(event):
        gan.set(0)
        sleep(1)
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        gv=magv_ten(data_gv.get())
        row=tkb.bang_tkb(malop,namhoc,data_hocky.get(),gv)
        threading.Thread(target=load_bang_tkb,args=(row,)).start()

    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        try:
            data_ngay.set(item['values'][4])
            data_mon.set(item['values'][2])
            data_ca.set(item['values'][5])

            data_matkb.set(item['values'][1])
            ngaycu.set(item['values'][5])
            moncu.set(item['values'][2])
            pp_giangcu.set(item['values'][3])
            cacu.set(item['values'][5])
            dataca=str(item['values'][5])
            for i in range(5):
                if dataca.find(str(i)) != -1:
                    ca[i].set(1)
                else:
                    ca[i].set(0)
        except: print('click vùng trống')

    def timkiem():
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        gv= magv_ten(data_gv.get())
        row=tkb.timkiem_dong_tkb(malop,namhoc,data_hocky.get(),gv,ndtimkiem.get())
        update(tv,row)

    def kt_lich_gv(magv, ngay, ca,matkb):
        data_ca1= " "
        data_ca=data_ca1.join(ca).split()
        tam=[]
        for i in data_ca:
            t=tkb.kt_lichgiang_them(magv,ngay,i,matkb)
            if t != []:
                tam.append(t[0])
        return tam
    def kt_lich_lop(malop, ngay, ca,matkb):
        data_ca1= ""
        data_ca=data_ca1.join(ca).split()
        tam=[]
        for i in data_ca:
            if tkb.kt_lich_tkb(malop,ngay,i,matkb) !=[]:
                tam.append(i)
        return tam
    def lock():
        string=strftime("%H:%M:%S %p")
        dmy=strftime("%d/%m/%Y")
        l.configure(text=string) 
        tg.config(text=dmy)
        try:
            l.after(1000,lock)
        except: print("kết thúc đông hồ")

    def khoiphuc():
        ngaycu.set("")
        moncu.set("")
        gvcu.set("")
        cacu.set("")
        ndtimkiem.set("")
        data_ca.set("")
        data_mon.set("")
        data_ngay.set("")
        data_matkb.set("")
        for i in range(5):
            ca[i].set(0)
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        magv= magv_ten(data_gv.get())
        row=tkb.bang_tkb(malop,namhoc,data_hocky.get(),magv)
        load_bang_tkb(row)

    def kt_sotiet(malop,mamh,pp,ca):
        sotietmonhoc=tkb.SoTietCuaMH(mamh,pp)
        stmh.set(sotietmonhoc)
        sotietdahoc=tkb.sotietdahoc(malop,mamh,pp)
        stdh.set(sotietdahoc)
        sotietca=tkb.sotiet_cahoc(str(ca))
        tong=int(sotietdahoc)+int(sotietca)
        if int(tong) > int(sotietmonhoc):
            return False
        else:return True

    def them(a,ngay):
        loadding(1)
        malop=malop_ten(data_lop.get())
        magv=magv_ten(data_gv.get())
        mamh =mamh_ten(data_mon.get())
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
        elif kt_lich_gv(magv,ngay,data_ca,"") !=[]:
            messagebox.showerror("thông báo","Giảng viên đã có lịch dạy ngày"+ngay+" vào ca "+data_ca+"!")
        elif kt_lich_lop(malop,ngay,data_ca,"") != []:
            messagebox.showerror("thông báo","Lớp đã có lịch học ngày"+ngay+" vào ca "+data_ca+"!")
        elif kt_sotiet(malop,mamh,pp,data_ca)==False:
            messagebox.showerror("thông báo","Dư thừa tiết học\nHiện tại đã học "+stdh.get()+"/"+stmh.get()+" tiết.")
        elif tkb.them_tkb(magv,mamh,pp,ngay,data_ca,malop,hki,namhoc):
            if a==1:
                ngay2=cong_ngay(ngay,7)
                them(2,ngay2)
                messagebox.showinfo("thông báo", "Đã thêm 1 dòng vào thời khoá biểu ")
                luong(khoiphuc)
            else: return
        else:
            messagebox.showerror("thông báo", "Thêm thời khoá biểu không thành công")
        loadding(0)
            
    def sua():
        loadding(1)
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
        
        if(data_matkb.get()== ""):
            messagebox.showerror("thông báo","không tìm thấy dữ liệu cần sửa ! Bạn hãy nhấn 2 lần vào dòng muốn sửa , rồi sửa dữ liệu và nhấn nút sửa")
        elif tkb.kt_tkb_dd(data_matkb.get())!= []:
            messagebox.showwarning("Thông báo","Đã điểm danh không thể sửa")
        elif messagebox.askyesno("thông báo","Bạn có chắc sửa dòng thời khoá biểu với mã tkb là "+data_matkb.get()):
            if data_ca=="" or magv=="" or mamh=="" or ngay =="":
                messagebox.showerror("thông báo","Hãy chọn đầy đủ dữ liệu")
            elif tkb.ngaya_nhohon_ngayb(ngay,now) ==True:
                messagebox.showerror("thông báo","Ngày phải lớn hơn ngày hôm nay")
            elif kt_lich_gv(magv,ngay,data_ca,data_matkb.get()) !=[]:
                messagebox.showerror("thông báo","Giảng viên đã có lịch dạy !")
            elif kt_lich_lop(malop,ngay,data_ca,data_matkb.get()) != []:
                messagebox.showerror("thông báo","Lớp đã có lịch học !")
            elif  kt_sotiet(malop,mamh,pp,data_ca)==False:
                messagebox.showerror("thông báo","Dư thừa tiết học\nHiện tại đã học "+stdh.get()+"/"+stmh.get()+" tiết.")
            elif tkb.sua_tkb(data_matkb.get(),magv,mamh,pp,ngay,data_ca,malop,hki,namhoc):
                messagebox.showinfo("thông báo", "Đã sửa thành công")
                luong(khoiphuc)
            else: messagebox.showerror("thông báo", "Đã sửa thất bại")
        loadding(0)
        
        
    def xoa():
        loadding(1)
        if messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            x=tv.selection()
            listma = []
            ko_xoa=[]
            for i in x:
                listma.append(tv.item(i,'values')[1])
            for i in listma:
                if tkb.kt_tkb_dd(i) == []:
                    if  tkb.xoa_dong_tkb(i) == True:
                        luong(khoiphuc)
                    else:
                        ko_xoa.append(i)
                else:ko_xoa.append(i)
                    
            if(ko_xoa!=[]):
                messagebox.showwarning("thông báo","Không thể xoá dòng thời khoá biểu có mã "+str(ko_xoa))
                luong(khoiphuc)
            else:
                messagebox.showinfo("thông báo","Đã xoá thành công")
                luong(khoiphuc)
        loadding(0)

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
    win.geometry("1200x800+120+10")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Thời khoá biểu")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_tkb.png")

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
    style()
    gan=StringVar()
    mylistlop=[]
    stmh=StringVar()
    stdh=StringVar()
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1200,height=800,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(600,400,image=img_bg)

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

    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)

    cbnam =Combobox(bg,textvariable=data_namhoc,font=("Baloo Tamma 2 Medium",11),justify="center", width=9,state='readonly')
    cbnam.bind('<<ComboboxSelected>>', capnhatbang)
    cbnam.place(x=423,y=4)
    Frame(bg,width=100,height=2,bg="white").place(x=423,y=4)
    Frame(bg,width=3,height=30,bg="white").place(x=423,y=4)
    Frame(bg,width=100,height=2,bg="white").place(x=423,y=34)


    cbhk =Combobox(bg,textvariable=data_hocky,font=("Baloo Tamma 2 Medium",11),justify="center", width=6, state='readonly', values=hocky)
    cbhk.current(0)
    cbhk.bind('<<ComboboxSelected>>', capnhatbang)
    cbhk.place(x=609,y=4)
    Frame(bg,width=79,height=2,bg="white").place(x=609,y=4)
    Frame(bg,width=3,height=32,bg="white").place(x=609,y=4)
    Frame(bg,width=80,height=2,bg="white").place(x=609,y=34)

    cbloai =Combobox(bg,textvariable=data_loai,font=("Baloo Tamma 2 Medium",11),justify="center",state='readonly', width=26,values=loai)
    cbloai.current(0)
    cbloai.place(x=680,y=169)
    Frame(bg,width=255,height=2,bg="white").place(x=680,y=169)
    Frame(bg,width=3,height=30,bg="white").place(x=680,y=169)
    Frame(bg,width=255,height=2,bg="white").place(x=680,y=199)

    cblop = Combobox(bg,textvariable=data_lop,font=("Baloo Tamma 2 Medium",11),justify="center",state='readonly', width=33)
    cblop.bind('<<ComboboxSelected>>', capnhatbang)
    cblop.place(x=847,y=45)
    Frame(bg,width=320,height=2,bg="white").place(x=847,y=45)
    Frame(bg,width=3,height=30,bg="white").place(x=847,y=45)
    Frame(bg,width=320,height=2,bg="white").place(x=847,y=75)

    Label(bg,font=("Baloo Tamma 2 Medium",11),bg="white",textvariable=data_ngay).place(x=740,y=212)

    cbgv =Combobox(bg,textvariable=data_gv,font=("Baloo Tamma 2 Medium",11),justify="center",state='readonly', width=27)
    cbgv.place(x=420,y=45)
    cbgv.bind('<<ComboboxSelected>>', capnhatbang)
    Frame(bg,width=262,height=2,bg="white").place(x=420,y=45)
    Frame(bg,width=3,height=32,bg="white").place(x=420,y=45)
    Frame(bg,width=262,height=2,bg="white").place(x=420,y=75)

    cbmon =Combobox(bg,textvariable=data_mon,font=("Baloo Tamma 2 Medium",11),justify="center",state='readonly', width=26)
    cbmon.place(x=680,y=125)
    Frame(bg,width=255,height=2,bg="white").place(x=680,y=125)
    Frame(bg,width=3,height=30,bg="white").place(x=680,y=125)
    Frame(bg,width=255,height=2,bg="white").place(x=680,y=155)
    ca=[]
    for i in range(5):
        option=IntVar()
        option.set(0)
        ca.append(option)

    Entry(bg,font=("Baloo Tamma 2 Medium",11),width=26,textvariable=ndtimkiem,bd=0,highlightthickness=0).place(x=841,y=418)

    Checkbutton(bg,text="Ca 1",font=("Baloo Tamma 2 Medium",10),variable=ca[1],bg="white").place(x=680,y=257)
    Checkbutton(bg,text="Ca 2",font=("Baloo Tamma 2 Medium",10),variable=ca[2],bg="white").place(x=730,y=257)
    Checkbutton(bg,text="Ca 3",font=("Baloo Tamma 2 Medium",10),variable=ca[3],bg="white").place(x=780,y=257)
    Checkbutton(bg,text="Ca 4",font=("Baloo Tamma 2 Medium",10),variable=ca[4],bg="white").place(x=830,y=257)

    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command= lambda:them(1,data_ngay.get()))
    btnthem.place(x=527,y=327)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=726,y=327)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=925,y=327)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,activebackground='white',command=timkiem)
    btntimkiem.place(x=1076,y=419)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground='white',command=khoiphuc)
    btnkhoiphuc.place(x=1111,y=419)

    f=Frame(bg)
    f.place(x=305,y=80)
    lb=Label(f,bg="#E8DFF1",fg="#E8DFF1")
    lb.pack()

    btnchonlich=Button(bg,image=img_btnchonlich,bd=0,highlightthickness=0,command=chonlich)
    btnchonlich.place(x=910,y=219)


    # tạo stype cho bảng
    
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=373,y=491)

    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5,6,7),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=50, anchor='center')
    tv.column(2, width=80 ,anchor='center')
    tv.column(3, width=250)
    tv.column(4, width=100)
    tv.column(5, width=100,anchor='center')
    tv.column(6, width=50,anchor=CENTER)
    tv.column(7, width=100,anchor=CENTER)

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="Mã TKB", anchor='center')
    tv.heading(3,text="Môn học")
    tv.heading(4,text="LT-TH")
    tv.heading(5,text="Ngày")
    tv.heading(6,text="ca")
    tv.heading(7,text="Trang thái")
    
    tv.pack()
    tv.bind('<ButtonRelease-1>', getrow)
    tv.tag_configure("ollrow" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))

    l = Label(bg, font=("Digital-7",12),background="white",foreground="black")
    l.place(x=885,y=2)
    tg = Label(bg, font=("Digital-7",12),background="white",foreground="black")
    tg.place(x=980,y=2)

    
    
    lock()
    luong(loaddl)

    win.mainloop()

if __name__ == '__main__':
    main()