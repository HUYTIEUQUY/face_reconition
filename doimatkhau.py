from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk
from tkinter import messagebox
import socket
import backend.xacthuc as xacthuc
import taikhoan
import dangnhap
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading


def main(trang):
    
    def hien(txtPass):
        if txtPass["show"]=="*":
            txtPass["show"]=""
        else:
            txtPass["show"]="*"


    def kt_dangnhap(email,passw,passwn):
        if email=="" or passw=="" or passwn=="":
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
            return False
        elif len(passw)<6 or len(passwn)<6 :
            messagebox.showwarning("thông báo","Vui lòng kiểm tra lại mật khẩu")
            return False
        elif xacthuc.xacthuc(email,passw)==False:
             messagebox.showerror("Thông báo","mật khẩu cũ không đúng")
             return False
        else:
            return True

    def truycapwweb(email,passw):
        cred = credentials.Certificate("nckh.json")
        firebase_admin.initialize_app(cred)
        link= auth.generate_password_reset_link(email)
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver=webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=options)
        driver.get(link)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/div[2]/div/div[1]/input"))).send_keys(passw)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/div[3]/div/button"))).click()
        driver.quit()


    def doimatkhau():
        email=data_e.get()
        passw=data_p.get()
        passwn=data_pn.get()

        if kt_dangnhap(email,passw,passwn) == True:
            truycapwweb(email,passwn)
            messagebox.showinfo("thông báo","Đã đổi mật khẩu")
            trove()
        else:
            messagebox.showerror("Lỗi","Đổi mật khẩu thất bại")
    def trove():
        win.destroy()
        if trang==1:
            taikhoan.main()
        else: 
            dangnhap.main()

    win=Tk()
    win.geometry("600x600+400+100")
    win.resizable(False,False)
    win.config(bg="green")
    win.title("Menu tkinter")
    img_bg=ImageTk.PhotoImage(file="img/bg_doimatkhau.png")
    img_btn=ImageTk.PhotoImage(file=f"img/btn_doimatkhau.png")
    img_btnhien=ImageTk.PhotoImage(file="img/img_btnhienmk.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/trove_bgdoimatkhau.png")

    bg=Canvas(win,width=600,height=600,bg="green")
    bg.pack(side="left",padx=0)


    anhnen=bg.create_image(300,300,image=img_bg)
    data_e=StringVar()
    data_p=StringVar()
    data_pn=StringVar()
    ten_thiet_bi = socket.gethostname()
    

    if trang==1:
        d=[]
        with open(ten_thiet_bi+".txt","r") as file:
            d=file.read().split()
        data_e.set(d[0])
        txtEmail=Label(bg,width=25,font=("Baloo Tamma",12),bg="white",bd=0,textvariable=data_e)
        txtEmail.place(x=220,y=228)
    else:
        txtEmail=Entry(bg,width=24,font=("Baloo Tamma",12),bg="white",bd=0,textvariable=data_e)
        txtEmail.place(x=240,y=228)
    
    
    txtPass=Entry(bg,width=17,font=("Baloo Tamma",12), bd=0, show="*", textvariable=data_p)
    txtPass.place(x=280,y=290)
   
    txtpassnew=Entry(bg,width=17,font=("Baloo Tamma",12), bd=0, show="*", textvariable = data_pn)
    txtpassnew.place(x=280,y=350)


    btn=Button(bg,image=img_btn,bd=0,borderwidth=0, highlightthickness=0, command=doimatkhau )
    btn.place(x=231,y=494)

    btn_trolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=trove)
    btn_trolai.place(x=550,y=2)

    btnhien=Button(bg,image=img_btnhien,bd=0,highlightthickness=0,command=lambda:hien(txtPass))
    btnhien.place(x=434,y=287)
    btnhienpn=Button(bg,image=img_btnhien,bd=0,highlightthickness=0,command=lambda:hien(txtpassnew))
    btnhienpn.place(x=434,y=347)
    win.mainloop()

if __name__ == '__main__':
    main()