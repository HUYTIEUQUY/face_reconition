from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import Face_AttendanceMKU


def main():
    def thulai():
        win.destroy()
        Face_AttendanceMKU.main()
    def thoat():
        win.destroy()


    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Không kết nối internet")
    img_bg=ImageTk.PhotoImage(file="img/khongketnoiinternet.png")
    img_thulai=ImageTk.PhotoImage(file="img/thulai.png")
    img_thoat=ImageTk.PhotoImage(file="img/thoat.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    btnthulai=Button(bg,image=img_thulai,bd=0,highlightthickness=0,command=thulai)
    btnthulai.place(x=323,y=504)
    btnthoat=Button(bg,image=img_thoat,bd=0,highlightthickness=0,command=thoat)
    btnthoat.place(x=558,y=504)

    win.mainloop()
if __name__ == '__main__':
    main()
