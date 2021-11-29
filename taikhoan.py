from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk
import dangnhap
import socket
import sinhvien
import diemdanh
import thongke
from backend.dl_giangvien import tengv_email,makhoa_email,sdt_email,magv_email,update_sdt
from backend.dl_khoa import tenkhoa
from backend.dl_tkb import kt_lichgiang_gv,gv_dd
import doimatkhau
import taikhoan_thongbao
import datetime
import threading
import diemdanh_bu

def main():

    def loadding(a):
        if a == 1:# đang load dữ liệu
            lb_loadding.place(x=904,y=1)
            print(a)
            btn_capnhatsdt["state"] = "disabled"
            btndangxuat["state"] = "disabled"
            btndangxuat1["state"] = "disabled"
            btndoimatkhau["state"] = "disabled"
        else:
            lb_loadding.place_forget()
            btn_capnhatsdt["state"] = "normal"
            btndangxuat["state"] = "normal"
            btndangxuat1["state"] = "normal"
            btndoimatkhau["state"] = "normal"



    def luong(ham):
        threading.Thread(target=ham).start()
    
    def loaddl():
        makhoa.set(makhoa_email(email))
        tengv.set(tengv_email(email))
        magv.set(magv_email(email))
        tenkh.set(tenkhoa(makhoa.get()))
        sdt.set(sdt_email(email))

        lbgv.config(text=tengv.get())
        lb_gv.config(text=tengv.get())
        lbtk.config(text=tenkh.get())

        lichgiang=(kt_lichgiang_gv(magv.get(),ngay))

        gvdd=gv_dd(magv.get(),ngay)

        if lichgiang == []:
            data_lichgiang.set("Hôm nay, không có tiết giảng")
        else:
            data_lichgiang.set("Hôm nay, có lịch giảng !")
            btnthongbao=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command=lambda: chuyentrang_lichgiang(lichgiang))
            btnthongbao.place(x=920,y=365)
            lbstb=Label(bg,text=len(lichgiang),fg="red",font=("Arial",10),bg="white")
            lbstb.place(x=952,y=360)

        if gvdd == []:
            data_dd.set("Đã điểm danh tất cả")
        else:
            data_dd.set("Chưa điểm danh")
            btnthongbaodd=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command= thongbaodd())
            btnthongbaodd.place(x=920,y=425)
            lbstb1=Label(bg,text=len(gvdd),fg="red",font=("Arial",10),bg="white")
            lbstb1.place(x=952,y=420)
        loadding(0)



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

    def capnhat_sdt():
        if len(sdt.get()) !=10 or sdt.get().isnumeric()== False:
            messagebox.showwarning("thông báo","Số điện thoại không đúng")
        elif update_sdt(magv.get(),sdt.get()):
            messagebox.showinfo("thông báo","Đã cập nhật số điện thoại")
        else:
            messagebox.showwarning("Lỗi ","Cập nhật không thành công")
    def thongbaodd():
        win.destroy()
        diemdanh_bu.main(1)

    def chuyentrang_lichgiang(lichgiang):
        win.destroy()
        taikhoan_thongbao.main(lichgiang, tengv.get())

    def btndoimatkhau():
        win.destroy()
        doimatkhau.main(1)
    def menuthongke():
        win.destroy()
        thongke.main()

    def menudiemdanh():
        win.destroy()
        diemdanh.main()

    def menuthemsv():
        win.destroy()
        sinhvien.main()

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
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.iconbitmap(r"img/iconphanmem.ico")
    win.config(bg="green")
    win.title("Thông tin người dùng")
    img_bg=ImageTk.PhotoImage(file="img/bgtaikhoan.png")
    img_bg1=ImageTk.PhotoImage(file="img/bgtaikhoan1.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan1.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btndangxuat1=ImageTk.PhotoImage(file="img/btndangxuat1.png")
    ing_btndoimatkhau=ImageTk.PhotoImage(file="img/btndoimatkhau.png")
    ing_btnthongbao=ImageTk.PhotoImage(file="img/btnthongbao.png")
    ing_btnthietlap=ImageTk.PhotoImage(file="img/thietlap.png")
    ing_btnquaylai=ImageTk.PhotoImage(file="img/btnquaylai.png")
    ing_capnhatsdt=ImageTk.PhotoImage(file="img/capnhatsdt.png")
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    makhoa=StringVar()
    tengv=StringVar()
    magv=StringVar()
    tenkh=StringVar()
    sdt=StringVar()
    data_lichgiang=StringVar()
    data_dd=StringVar()


    time = datetime.datetime.now()
    now = time.strftime("%x")
    ngay=dinh_dang_ngay(now)
    
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,activebackground='#857EBD',command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD')
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    
    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)

    lb_gv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="black",bg="white")
    lb_gv.place(x=570,y=201)
    
    lbtk=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="black",bg="white")
    lbtk.place(x=570,y=141)

    lbe=Label(bg,text=email,font=("Baloo Tamma 2 Medium",12),fg="black",bg="white")
    lbe.place(x=570,y=261)

    lbsdt=Entry(bg,textvariable=sdt,font=("Baloo Tamma 2 Medium",12),fg="black",bg="white",bd=0,highlightthickness=0,)
    lbsdt.place(x=570,y=321)

    btn_capnhatsdt=Button(bg,image=ing_capnhatsdt,bd=0,highlightthickness=0,command=capnhat_sdt)
    btn_capnhatsdt.place(x=925,y=310)

    

    btndoimatkhau=Button(bg,image=ing_btndoimatkhau,bd=0,highlightthickness=0,command=btndoimatkhau)
    btndoimatkhau.place(x=672,y=539)

    btndangxuat1=Button(bg,image=ing_btndangxuat1,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat1.place(x=836,y=537)

    lbcg=Label(bg,textvariable=data_lichgiang,font=("Baloo Tamma 2 Medium",12),fg="black",bg="white")
    lbcg.place(x=570,y=381)

    lbdd=Label(bg,textvariable=data_dd,font=("Baloo Tamma 2 Medium",12),fg="black",bg="white")
    lbdd.place(x=570,y=441)

    # btnthietlap=Button(bg,image=ing_btnthietlap,bd=0,highlightthickness=0,command=thietlap)
    # btnthietlap.place(x=949,y=2)
    lb_loadding=Label(bg,text=" Đang tải . . . ", font=("Baloo Tamma 2 Medium",11),bg="#FFF4FF",fg="#AD7B98", width=14)

    luong(loaddl)
    loadding(1)
    win.mainloop()

if __name__ == '__main__':
    main()