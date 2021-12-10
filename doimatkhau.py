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
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from send_message import gmail_doimatkhau




def main(trang):


    def kt_dangnhap(email,passw,passwn,passwn_nhaplai):
        print(xacthuc.xacthuc(email,passw))
        if email=="" or passw=="" or passwn=="" or passwn_nhaplai=="":
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
            return False
        elif (len(passw)<6 and len(passw)>10)  :
            messagebox.showwarning("thông báo","Vui lòng kiểm tra lại mật khẩu")
            return False
        elif passwn != passwn_nhaplai:
            messagebox.showerror("thông báo","Mật khẩu mới chưa khớp")
        elif xacthuc.xacthuc(email,passw) == False:
             messagebox.showerror("Thông báo","Vui lòng kiểm tra lại email và mật khẩu cũ")
             return False
        else:
            return True

    def truycapwweb(email,passw):
        # cred = credentials.Certificate("facerecognition.json")
        try:
            firebase_admin.get_app()
        except:
            cred = credentials.Certificate("facerecognition.json")
            firebase_admin.initialize_app(cred)
        link= auth.generate_password_reset_link(email)
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver=webdriver.Chrome(executable_path=r'C:/Program Files/Google/Chrome/Application/chrome.exe',chrome_options=options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/div[2]/div/div[1]/input"))).send_keys(passw)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/div[3]/div/button"))).click()
        driver.quit()


    def doimatkhau():
        email=data_e.get()
        passw=data_p.get()
        passwn=data_pn.get()
        passwn_nhaplai = data_pn_nhaplai.get()

        if kt_dangnhap(email,passw,passwn,passwn_nhaplai) == True:
            truycapwweb(email,passwn)
            messagebox.showinfo("thông báo","Đã đổi mật khẩu")
            threading.Thread(target=gmail_doimatkhau,args=(email,passwn,)).start()
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
    win.iconbitmap(r"img/iconphanmem.ico")
    win.config(bg="white")
    win.title("Đổi mật khẩu")
    img_bg=ImageTk.PhotoImage(file="img/bg_doimatkhau.png")
    img_btn=ImageTk.PhotoImage(file=f"img/btn_doimatkhau.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/trove_bgdoimatkhau.png")

    bg=Canvas(win,width=600,height=600,bg="white")
    bg.pack(side="left",padx=0)


    anhnen=bg.create_image(300,300,image=img_bg)
    data_e=StringVar()
    data_p=StringVar()
    data_pn=StringVar()
    data_pn_nhaplai=StringVar()
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
    
    txtpass_nhaplai=Entry(bg,width=17,font=("Baloo Tamma",12), bd=0, show="*", textvariable = data_pn_nhaplai)
    txtpass_nhaplai.place(x=280,y=409)


    btn=Button(bg,image=img_btn,bd=0,borderwidth=0, highlightthickness=0,activebackground="#BFAAE5", command=doimatkhau )
    btn.place(x=231,y=494)

    btn_trolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=trove)
    btn_trolai.place(x=550,y=2)

    win.mainloop()

if __name__ == '__main__':
    main()