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
from backend.dl_giangvien import tengv_email,makhoa_email,magv_ten,magv_email
import backend.dl_thongke as tk
import os
import xlsxwriter
import threading
from tkinter import filedialog
from styletable import style, update
import backend.dl_tkb as tkb
from backend.dl_adminlop import malop_ten
from backend.dl_sinhvien import tensv_ma
from backend.dl_monhoc import tenmh_ma
import time as t
import admin_tkb1
from backend.dl_khoa import khoa_co_quyen_all

def main():
    def loadding(a):
        if a == 1:# đang load dữ liệu
            lb_loadding.place(x=1110,y=4)
            btndangxuat["state"] = "disabled"
            btnkhoiphuc["state"] = "disabled"
            btntimkiem["state"] = "disabled"
        else:
            lb_loadding.place_forget()
            btndangxuat["state"] = "normal"
            btnkhoiphuc["state"] = "normal"
            btntimkiem["state"] = "normal"


    def dongluu(row,ma,ten,tt,TG,TGra,ghichu):

        for i in row:
            ma.append(i[0]) 
            ten.append(tensv_ma(i[1]))
            tt.append(i[2]) 
            TG.append(i[3]) 
            TGra.append(i[4]) 
            ghichu.append(i[5]) 

    def xuat_excel():
        row=tk.bangdd_ma(matkb.get())
        ma=[]
        ten=[]
        tt=[]
        TG=[]
        TGra=[]
        ghichu=[]
        dongluu(row,ma,ten,tt,TG,TGra,ghichu)

        if len(ma) < 1:
            messagebox.showwarning("thông báo","Không có dữ liệu xuất file excel !")
            return False
        else:
            try:
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Lưu file excel",filetypes=(("XLSX File","*.xlsx"),("All File","*.*")))
            except: print("")
            out_workbook = xlsxwriter.Workbook(fln+".xlsx")
            outsheet = out_workbook.add_worksheet()
            tenlop=data_lop.get()
            mh=tenmh.get()
            outsheet.write("A1","Tên lớp: "+tenlop)
            outsheet.write("B1","Môn học: "+mh)
            outsheet.write("C1","Ngày: "+ngay.get())

            outsheet.write("A3","Mã sinh viên")
            outsheet.write("B3","Tên sinh viên")
            outsheet.write("C3","Thông tin")
            outsheet.write("D3","Thời gian vào")
            outsheet.write("E3","Thời gian ra")
            outsheet.write("F3","Ghi chú")
            def write_data_to_file(array,x):
                for i in range(len(array)):
                    outsheet.write(i+3,x,array[i])
            write_data_to_file(ma,0)
            write_data_to_file(ten,1)
            write_data_to_file(tt,2)
            write_data_to_file(TG,3)
            write_data_to_file(TGra,4)
            write_data_to_file(ghichu,5)
            out_workbook.close()
    def bat_dau_tim():

        malop = malop_ten(data_lop.get())
        namhoc = tkb.manh_ten(data_namhoc.get())
        gv=magv_ten(data_gv.get())
        loai=data_tim.get()
        # nd_tim=["Mã TKB","Môn học","LT-TH","Ngày","Ca","Trạng Thái"]
        row = tkb.timkiem_dong_tkb(malop,namhoc,data_hocky.get(),gv,ndtimkiem.get(),loai)
        if row == []:
            messagebox.showwarning("thông báo","Không có dữ liệu")
            update(tv,row)
            loadding(0)
        else:
            update(tv,row)
            loadding(0)

    def timkiem():
        loadding(1)
        threading.Thread(target=bat_dau_tim).start()

    def khoiphuc_dd():
        row =tk.bangdd_ma(matkb.get())
        load_bang_diemdanh(row)

    def getrow(event):
        tam.set(0)
        t.sleep(1)
        tb.delete(*tb.get_children())
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        matkb.set(item['values'][1])
        matkb1.set('Mã thời khoá biểu : '+str(item['values'][1]))
        ngay.set(item['values'][4])
        ca.set(item['values'][5])
        tenmh.set(item['values'][2])
        try:
            f.place(x=330,y=440)
        except:print("Đã tạo frame rồi")
        if (str(item['values'][6])=="Chưa điểm danh"):
            messagebox.showwarning("Thông báo","Chưa điểm danh")
            try:
                f.place_forget()
            except:return
        else:
            threading.Thread(target=khoiphuc_dd).start() 

    def load_bang_tkb(row):
        tv.delete(*tv.get_children())
        global dem
        dem = 0
        tam.set(1)
        for i in row:
            i.insert(0,dem+1)
            i[2]=tenmh_ma(i[2])
            if dem%2==0:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
            else:tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
            dem += 1
            if tam.get() == str(0):
                break
        loadding(0)


    def load_bang_diemdanh(row):
        tam.set(1)
        tb.delete(*tb.get_children())
        global dem
        dem = 0
        for i in row:
            i.insert(0,dem+1)
            i[2]=tensv_ma(i[2])
            if dem%2==0:
                tb.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
            else:tb.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
            dem += 1
            if tam.get()==str(0):break
        loadding(0)

    def loaddl():
        tengv.set(tengv_email(d[0]))
        makhoa.set(makhoa_email(d[0]))
        tengv.set(tengv_email(d[0]))
        lbgv.config(text=tengv.get())
        global quyen
        quyen = khoa_co_quyen_all(makhoa.get())
        if quyen == str(1):
            lop = tkb.all_lop()
        else:
            lop = tkb.lop_khoa(makhoa.get())
        gv = tkb.gv_khoa(makhoa.get())
        namhoc=tkb.namhoc()
        #set cho combobox to
        cblop.config(values=lop)
        cblop.current(0)
        cbgv.config(values=gv)
        cbgv.current(0)
        cbnam.config(values=namhoc)
        cbnam.current(0)
        threading.Thread(target=loadbang).start()
        
    def capnhatbang(event):
        tam.set(0)
        t.sleep(1)
        fr_dd.place_forget()
        loadding(1)
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        gv=magv_ten(data_gv.get())
        row=tkb.bang_tkb(malop,namhoc,data_hocky.get(),gv)
        global a
    
        if row == []:
            messagebox.showwarning("thông báo","Không có dữ liệu")
            a=threading.Thread(target=load_bang_tkb,args=(row,))
            a.start()
        else:
            a=threading.Thread(target=load_bang_tkb,args=(row,))
            a.start()
        try:
            f.place_forget()
        except:loadding(0)
        loadding(0)

    def loadbang():
        ndtimkiem.set("")
        malop=malop_ten(data_lop.get())
        namhoc=tkb.manh_ten(data_namhoc.get())
        gv=magv_ten(data_gv.get())
        row=tkb.bang_tkb(malop,namhoc,data_hocky.get(),gv)
        if row == []:
            messagebox.showwarning("thông báo","Không có dữ liệu")
            load_bang_diemdanh(row)
            f.place_forget()
        else:
            load_bang_tkb(row)
        loadding(0)

    def chondong(event):
        rowid=tb.identify_row(event.y)
        txt_ghichu.delete(1.0,END)
        item=tb.item(tb.focus())
        txt_ghichu.insert(END,item['values'][6])
        data_masv.set(item['values'][1])

    def xem_ghichu():
        if data_masv.get() != "":
            fr_tb.place_forget()
            frame_ghichu.place(x=330,y=110)
            frame_ghichu.config(bg="white")
            lb_ghichu.config(text="Ghi chú",background="white")
            txt_ghichu.pack(padx=20)
            btn_trolai.pack(side="right",padx=10,pady=10)

        
    def trolai():
        frame_ghichu.place_forget()
        fr_tb.place(x=330,y=110)
        txt_ghichu.delete(1.0,END)


    def menutkb():
        quyen = khoa_co_quyen_all(makhoa.get())
        win.destroy()
        if quyen== str(1):
            admin_tkb1.main()
        else:
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
    win.geometry("1200x800+120+10")
    win.resizable(False,False)
    win.iconbitmap(r"img/iconphanmem.ico")
    win.config(bg="white")
    win.title("Thống kê")
    img_bg=ImageTk.PhotoImage(file="img_admin/bg_thongke_admin.png")
    img_erorr=ImageTk.PhotoImage(file="img/bg_thongke_erorr.png")
    
    img_menulophoc=ImageTk.PhotoImage(file="img_admin/menu_lophoc.png")
    img_menugiangvien=ImageTk.PhotoImage(file="img_admin/menu_giangvien.png")
    img_menutkb=ImageTk.PhotoImage(file="img_admin/menu_tkb.png")
    img_menuthongke=ImageTk.PhotoImage(file="img_admin/menu_thongke1.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    ing_timkiem=ImageTk.PhotoImage(file="img/btn_timkiem.png")
    img_btnexcel_xuat=ImageTk.PhotoImage(file="img_admin/xuat_excel.png")
    img_btnghichu = ImageTk.PhotoImage(file="img_admin/btn_ghichu.png")
    img_btntrove = ImageTk.PhotoImage(file="img_admin/btn_trolai1.png")
    img_menumonhoc=ImageTk.PhotoImage(file="img_admin/menu_monhoc.png")

    bg=Canvas(win,width=1200,height=800,bg="white")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(600,400,image=img_bg)

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

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    btntimkiem=Button(bg,image=ing_timkiem,bd=0,activebackground='white',highlightthickness=0,command=timkiem)
    btntimkiem.place(x=1116,y=64)
    
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,activebackground='white',highlightthickness=0,command=loadbang, bg="white")
    btnkhoiphuc.place(x=1156,y=65)
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    tengv=StringVar()
    magv=StringVar()
    makhoa=StringVar()
    data_namhoc=StringVar()
    data_hocky=StringVar()
    data_lop=StringVar()
    data_gv=StringVar()
    matkb=StringVar()
    data_masv=StringVar()
    ngay=StringVar()
    ca=StringVar()
    ndtimkiem=StringVar()
    tenmh=StringVar()
    matkb1 = StringVar()
    tam=StringVar()
    tam.set(0)
    data_tim=StringVar()
    nd_tim=["Môn học","LT-TH","Ngày","Ca","Trạng Thái"]

    # value cho combobox 
    hocky=[1,2]

    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)

    cbnam =Combobox(bg,textvariable=data_namhoc,font=("Baloo Tamma 2 Medium",10),justify="center", width=13,state='readonly')
    cbnam.bind('<<ComboboxSelected>>', capnhatbang)
    cbnam.place(x=425,y=10)
    Frame(bg,width=125,height=2,bg="white").place(x=425,y=10)
    Frame(bg,width=3,height=30,bg="white").place(x=425,y=10)
    Frame(bg,width=125,height=2,bg="white").place(x=425,y=37)

    cbhk =Combobox(bg,textvariable=data_hocky,font=("Baloo Tamma 2 Medium",10),justify="center", width=7, state='readonly', values=hocky)
    cbhk.current(0)
    cbhk.bind('<<ComboboxSelected>>', capnhatbang)
    cbhk.place(x=627,y=10)
    Frame(bg,width=78,height=2,bg="white").place(x=627,y=10)
    Frame(bg,width=3,height=30,bg="white").place(x=627,y=10)
    Frame(bg,width=78,height=2,bg="white").place(x=627,y=37)

    cblop =Combobox(bg,textvariable=data_lop,font=("Baloo Tamma 2 Medium",11),state='readonly', width=30)
    cblop.bind('<<ComboboxSelected>>', capnhatbang)
    cblop.place(x=811,y=10)
    Frame(bg,width=290,height=2,bg="white").place(x=811,y=10)
    Frame(bg,width=3,height=30,bg="white").place(x=811,y=10)
    Frame(bg,width=290,height=2,bg="white").place(x=811,y=40)

    cbgv =Combobox(bg,textvariable=data_gv,font=("Baloo Tamma 2 Medium",11),state='readonly', width=27)
    cbgv.bind('<<ComboboxSelected>>', capnhatbang)
    cbgv.place(x=450,y=60)
    Frame(bg,width=263,height=2,bg="white").place(x=450,y=60)
    Frame(bg,width=3,height=30,bg="white").place(x=450,y=60)
    Frame(bg,width=263,height=2,bg="white").place(x=450,y=90)

    cbtim =Combobox(bg,textvariable=data_tim,font=("Baloo Tamma 2 Medium",11),justify="center",state='readonly', width=13, value=nd_tim)
    cbtim.place(x=739,y=62)
    cbtim.current(0)
    Frame(bg,width=135,height=2,bg="white").place(x=739,y=62)
    Frame(bg,width=3,height=30,bg="white").place(x=739,y=62)
    Frame(bg,width=135,height=2,bg="white").place(x=739,y=92)

    style()

    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=330,y=110)


    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
   
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5,6,7),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=50, anchor='center')
    tv.column(2, width=100 ,anchor='center')
    tv.column(3, width=250)
    tv.column(4, width=100)
    tv.column(5, width=100,anchor='center')
    tv.column(6, width=80,anchor=CENTER)
    tv.column(7, width=100,anchor=CENTER)

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="MÃ TKB", anchor='center')
    tv.heading(3,text="Môn học")
    tv.heading(4,text="LT-TH")
    tv.heading(5,text="Ngày")
    tv.heading(6,text="ca")
    tv.heading(7,text="Trạng thái")
    
    tv.pack()
    tree_scroll.config(command=tv.yview)
    tv.bind('<ButtonRelease-1>', getrow)
    tv.tag_configure("ollrow" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))

    f=Frame(bg,background="white")
    f1=Frame(f,background="white")
    f1.pack(side="top",anchor='e')
    Label(f1,textvariable = matkb1, font=("Baloo Tamma 2 Medium",14),bg="white",fg = "#837EBE" ).pack(side='left',anchor='w',padx=280)
    btnghichu=Button(f1,image=img_btnghichu,bd=0,highlightthickness=0,activebackground='white',command=xem_ghichu)
    btnghichu.pack(side="right", anchor='e',padx=5,pady=8)
    btnexcelxuat=Button(f1,image=img_btnexcel_xuat,bd=0,highlightthickness=0,command=xuat_excel)
    btnexcelxuat.pack(side="right", anchor='e')
    fr_dd=Frame(f)
    fr_dd.pack(side="bottom")

        #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_dd)
    tree_scroll.pack(side='right', fill="y")

    tb = ttk.Treeview(fr_dd, columns=(1,2,3,4,5,6,7),yscrollcommand=tree_scroll.set)
    tb.column('#0', width=0, stretch='no')
    tb.column(1, width=50, anchor='center')
    tb.column(2, width=100 ,anchor='center')
    tb.column(3, width=150)
    tb.column(4, width=150,anchor='center')
    tb.column(5, width=100,anchor='center')
    tb.column(6, width=100,anchor='center')
    tb.column(7, width=150,anchor='center')

    tb.heading('#0', text="", anchor='center')
    tb.heading(1,text="STT")
    tb.heading(2,text="Mã sinh viên", anchor='center')
    tb.heading(3,text="Tên Sinh viên")
    tb.heading(4,text="Thông tin")
    tb.heading(5,text="Thời gian vào")
    tb.heading(6,text="Thời gian ra")
    tb.heading(7,text="Ghi chú")
    tb.bind('<ButtonRelease-1>', chondong)
    tb.pack()
    tree_scroll.config(command=tb.yview)
    tb.tag_configure("ollrow" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tb.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))

    frame_ghichu=Frame(bg,background="#E8DFF1")
    lb_ghichu=Label(frame_ghichu,font=("Baloo Tamma 2 Medium",14),fg="#A672BB")
    lb_ghichu.pack()

    txt_ghichu=Text(frame_ghichu,width=60,height=6,bd=1,background="#F1F1F1",font=("Baloo Tamma 2 Medium",10))
    btn_trolai= Button(frame_ghichu,image=img_btntrove,bd=0,highlightthickness=0,activebackground="white",command=trolai)


    txttim=Entry(bg,font=("Baloo Tamma 2 Medium",11),width=25,textvariable=ndtimkiem,bd=0,highlightthickness=0)
    txttim.place(x=888, y=64)

    lb_loadding=Label(bg,text=" Đang tải . . . ", font=("Baloo Tamma 2 Medium",11),bg="#FCE2E9",fg="#AD7B98", width=12)

    loadding(1)
    threading.Thread(target=loaddl).start()
    win.mainloop()
if __name__ == '__main__':
    main()
    