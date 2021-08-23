from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk
import dangnhap
import socket
import sinhvien
import diemdanh
import thongke
import taikhoan


def main(lichgiang):
    
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
    img_bg1=ImageTk.PhotoImage(file="img/bgtaikhoan1.png")
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan1.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btnquaylai=ImageTk.PhotoImage(file="img/btnquaylai.png")
#------------------------------------------------------------------------------
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    email=d[0]
  

#-------------------------------------------------------------------------------
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg1)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,command=quaylai)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    bglichgiang=Frame(bg,width=450,height=140,bg="#A672BB")
    bglichgiang.place(x=410,y=155)

    Label(bglichgiang,text="Lớp",width=22,bg="#5F1965",fg="white").grid(row=0,column=0,pady=10,padx=5)
    Label(bglichgiang,text="Môn học",width=22,bg="#5F1965",fg="white").grid(row=0,column=1,pady=10,padx=5)
    Label(bglichgiang,text="Ca học",width=22,bg="#5F1965",fg="white").grid(row=0,column=2,pady=10,padx=5)
    for i in range(len(lichgiang)):
        for j in range(len(lichgiang[i])):
            Label(bglichgiang,text=lichgiang[i][j],width=22).grid(row=i+1,column=j,pady=10,padx=5)
    
    btnquaylai=Button(bg,image=ing_btnquaylai,bd=0,highlightthickness=0,command=quaylai)
    btnquaylai.place(x=836,y=537)

    win.mainloop()

if __name__ == '__main__':
    main()