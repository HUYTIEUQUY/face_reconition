from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk
import dangnhap
import socket
import sinhvien
import diemdanh
import thongke

# import diemdanhbu
# import taikhoan_thongbao


def main():
    # def thongbaodd():
    #     win.destroy()
    #     diemdanhbu.main()
    def thietlap():
        return
    # def lichgiang():
    #     win.destroy()
    #     taikhoan_thongbao.main()

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
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
    # makhoa=csdl.makhoa_tu_email(email)
    # tenkhoa=csdl.tenkhoatuma(makhoa)

#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    # tengv=csdl.tim_tengv_tu_email()
    # Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    # lbgv=Label(bg,text=tengv,font=("Baloo Tamma",12),fg="black",bg="white")
    # lbgv.place(x=560,y=155)
    
    # lbtk=Label(bg,text=tenkhoa,font=("Baloo Tamma",12),fg="black",bg="white")
    # lbtk.place(x=560,y=220)

    # lbe=Label(bg,text=email,font=("Baloo Tamma",12),fg="black",bg="white")
    # lbe.place(x=560,y=280)

    # l=[]
    # m=[]
    # c=[]
    # ngaydd=[]
    # tenlopdd=[]
    # tenmhdd=[]
    # cadd=[]
    # magv=csdl.tengv_thanh_ma(tengv)
    # # csdl.cagiang(magv,l,m,c)
    # # for i in range(len(l)):
    # #     cagiang= "Bạn có lịch giảng lớp "+str(l[i])+" môn"+str(m[i])+" vào ca "+str(c[i])
    # #     Label(bg,text=cagiang,font=("Baloo Tamma",12),fg="black",bg="white").place(x=560,y=343)
    # # Label(bg,text="Bạn thực hiện việc điểm danh rất tốt",font=("Baloo Tamma",12),fg="black",bg="white").place(x=560,y=405)

    # # btnthongbaodd=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0)
    # # btnthongbaodd.place(x=790,y=390)

    # if csdl.cagiang(magv,l,m,c) == False:
    #     lbcg=Label(bg,text="Hôm nay, bạn không có tiết giảng",font=("Baloo Tamma",12),fg="black",bg="white")
    #     lbcg.place(x=560,y=343)
    # else:
    #     lbcg=Label(bg,text="Hôm nay, bạn có lịch giảng !",font=("Baloo Tamma",12),fg="black",bg="white")
    #     lbcg.place(x=560,y=343)
    #     btnthongbao=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command=lichgiang)
    #     btnthongbao.place(x=790,y=330)
    #     lbstb=Label(bg,text=len(l),fg="red",font=("Arial",10),bg="white")
    #     lbstb.place(x=822,y=330)

    # if csdl.gvdiemdanh(magv,ngaydd,tenlopdd,tenmhdd,cadd)== False:
    #     lbdd=Label(bg,text="Bạn thực hiện việc điểm danh rất tốt",font=("Baloo Tamma",12),fg="black",bg="white")
    #     lbdd.place(x=560,y=405)
    # else:
    #     lbdd=Label(bg,text="Có lẽ bạn đã quên điểm danh !",font=("Baloo Tamma",12),fg="black",bg="white")
    #     lbdd.place(x=560,y=405)
        
    #     btnthongbaodd=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command=thongbaodd)
    #     btnthongbaodd.place(x=790,y=390)
    #     lbstb1=Label(bg,text=len(ngaydd),fg="red",font=("Arial",10),bg="white")
    #     lbstb1.place(x=822,y=390)

    # btndoimatkhau=Button(bg,image=ing_btndoimatkhau,bd=0,highlightthickness=0)
    # btndoimatkhau.place(x=672,y=539)

    # btndangxuat1=Button(bg,image=ing_btndangxuat1,bd=0,highlightthickness=0,command=dangxuat)
    # btndangxuat1.place(x=836,y=537)

    # btnthietlap=Button(bg,image=ing_btnthietlap,bd=0,highlightthickness=0,command=thietlap)
    # btnthietlap.place(x=949,y=2)
    
    win.mainloop()

if __name__ == '__main__':
    main()