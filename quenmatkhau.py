from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk
from tkinter import messagebox
import socket
import dangnhap
from backend.dl_giangvien  import tengv_email
from send_message import gui_ma_xn
from backend.xacthuc import kt_ma_xacnhan,xoa_ma_xacnhan
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def main():



    def gui_ma_xacnhan():
        if data_e.get() == "":
            messagebox.showerror("Thông báo","Vui lòng nhập email")
        elif tengv_email(data_e.get()) == "":
            messagebox.showerror("Thông báo","Email chưa đăng ký tài khoản")
        else:
            gui_ma_xn(data_e.get())
            lbem.config(text="Mã")
            txtEmail.config(textvariable=data_ma)
            btn.config(command=xacnhanma)
    def xacnhanma():
        if len(data_ma.get()) != 4:
            messagebox.showerror("Thông báo" , "Mã xác nhận có 4 chữ số")
        elif kt_ma_xacnhan(data_e.get(),data_ma.get()) == "" :
            messagebox.showerror("Thông báo","Mã xác nhận không đúng")
        else:
            lb_frame.place_forget()
            btn.config(command=capnhatmatkhau)
            lbem.config(text="Mật khẩu")
            txtEmail.config(textvariable=data_matkhau)
            
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
    def capnhatmatkhau():
        if data_matkhau.get()=="" and data_nhaplai.get()=="":
            messagebox.showerror("Thông báo","Nhập đầy đủ dữ liệu")
        elif data_matkhau.get() != data_nhaplai.get():
            messagebox.showerror("Thông báo","Mật khẩu không khớp")
        elif len(data_matkhau.get()) <6 and len(data_matkhau.get())>10:
            messagebox.showerror("Thông báo","Mật khẩu phải từ 6 đến 10 kí tự")
        else:
            truycapwweb(data_e.get(),data_matkhau.get())
            messagebox.showinfo("thông báo","Đã cập nhật mật khẩu")
            threading.Thread(target=xoa_ma_xacnhan,args=(data_e.get(),)).start()
            trove()
        

    def trove():
        win.destroy()
        dangnhap.main()

    win=Tk()
    win.geometry("600x600+400+100")
    win.resizable(False,False)
    win.iconbitmap(r"img/iconphanmem.ico")
    win.config(bg="green")
    win.title("Quên mật khẩu")
    img_bg=ImageTk.PhotoImage(file="img/bg_laylaimatkhau.png")
    img_btn=ImageTk.PhotoImage(file=f"img/btn_xacnhan.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/trove_bgdoimatkhau.png")
    bg_an=ImageTk.PhotoImage(file="img/frame_bg.png")

    bg=Canvas(win,width=600,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(300,300,image=img_bg)
    ten_thiet_bi = socket.gethostname()
    
    data_e=StringVar()
    data_ma=StringVar()
    data_matkhau=StringVar()
    data_nhaplai=StringVar()

    
    txtEmail=Entry(bg,width=23,font=("Baloo Tamma 2 Medium",12),bg="white",bd=0,textvariable=data_e)
    txtEmail.place(x=243,y=228)
    txtnhaplai=Entry(bg,width=23,font=("Baloo Tamma 2 Medium",12),bg="white",bd=0,textvariable=data_nhaplai)
    txtnhaplai.place(x=243,y=287)
    
    lbem=Label(bg,text="Email",font=("Baloo Tamma 2 Medium",14),width=8,fg="#5F1965",justify="center",bg="#F9D9D4")
    lbem.place(x=148,y=224)
    
    lbnhaplai=Label(bg,text="Nhập lại",font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#F9D9D4")
    lbnhaplai.place(x=151,y=281)
    
    lb_frame = Label(bg,image=bg_an,bd=0,borderwidth=0, highlightthickness=0)
    lb_frame.place(x=134,y=272)
    
    btn=Button(bg,image=img_btn,bd=0,borderwidth=0, highlightthickness=0,activebackground="#BFAAE5" ,command=gui_ma_xacnhan)
    btn.place(x=231,y=494)

    win.mainloop()

if __name__ == '__main__':
    main()