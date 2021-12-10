from tkinter import *
from tkinter import PhotoImage ,messagebox
from PIL import ImageTk
import dangnhap
import socket
import sinhvien
import diemdanh
import thongke
import taikhoan



def main(lichgiang,tengv):
    
    def quaylai():
        win.destroy()
        taikhoan.main()  

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
    win.config(bg="white")
    win.title("Lịch giảng")
    img_bg1=ImageTk.PhotoImage(file="img/bgtaikhoan1.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan1.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/btn_trolai.png")
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="white")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg1)

    lbgv=Label(bg,text=tengv,font=("Baloo Tamma 2 Medium",13),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,activebackground='#857EBD',command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD',command=quaylai)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,activebackground='#857EBD',command=dangxuat)
    btndangxuat.place(x=248,y=44)

    bglichgiang=Frame(bg,width=450,height=140,bg="#A672BB")
    bglichgiang.place(x=380,y=155)



    Label(bglichgiang,text="Lớp",width=22,bg="#5F1965",fg="white",font=("Baloo Tamma 2 Medium",10)).grid(row=0,column=0,pady=10,padx=5)
    Label(bglichgiang,text="Môn học",width=22,bg="#5F1965",fg="white",font=("Baloo Tamma 2 Medium",10)).grid(row=0,column=1,pady=10,padx=5)
    Label(bglichgiang,text="Ca học",width=22,bg="#5F1965",fg="white",font=("Baloo Tamma 2 Medium",10)).grid(row=0,column=2,pady=10,padx=5)
    for i in range(len(lichgiang)):
        for j in range(len(lichgiang[i])):
            Label(bglichgiang,text=lichgiang[i][j],width=22,font=("Baloo Tamma 2 Medium",10)).grid(row=i+1,column=j,pady=10,padx=5)
    
    btntrolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=quaylai)
    btntrolai.place(x=948,y=2)


    win.mainloop()

if __name__ == '__main__':
    main()