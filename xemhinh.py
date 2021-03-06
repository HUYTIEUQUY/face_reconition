from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import shutil
from tkinter import messagebox
import dangnhap
import socket
import sinhvien
import diemdanh
import pickle
import cv2
import face_recognition
import thongke
import taikhoan
import re
from backend.dl_adminlop import tenlop_ma,malop_masv
from backend.dl_giangvien import tengv_email,makhoa_email
import backend.dl_sinhvien as sv
from uploadfile import upload_anh,load,upload_filemahoa
import threading



def main(masv):
    def khong_dau(s):
        s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
        s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
        s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
        s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
        s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
        s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
        s = re.sub(r'[ìíịỉĩ]', 'i', s)
        s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
        s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
        s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
        s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
        s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
        s = re.sub(r'[Đ]', 'D', s)
        s = re.sub(r'[đ]', 'd', s)
        return s
    a=[]
    # def sua_anh(lb,i,btn):
    #     a.pop(i-1)
    #     chonanh(lb,i,btn)


    # def chonanh(lb,i,btn):
    #     x= filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
    #     shutil.copyfile(x,"./img_anhsv/"+str(masv)+str(i)+".png")
    #     a.insert(i-1,str(masv)+str(i)+".png")
    #     img=Image.open(x)
    #     img.thumbnail((80,100))
    #     img=ImageTk.PhotoImage(img)
    #     lb.config(image=img)
    #     lb.image=img
    #     btn.config(command=lambda:sua_anh(lb,i,btn) )

    def gananh(manganh,i):
        try:
            img=Image.open(load(manganh[i]))
        except:img=Image.open("img_anhsv/aa.jpg")
        # img = Image.open(load())
        img.thumbnail((200,200))
        # img = img.resize ((50, 50), Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
    
        if(i==0):
            lb1.config(image=img)
            lb1.image=img
        if(i==1):
            lb2.config(image=img)
            lb2.image=img
        if(i==2):
            lb3.config(image=img)
            lb3.image=img
        if(i==3):
            lb4.config(image=img)
            lb4.image=img
        if(i==4):
            lb5.config(image=img)
            lb5.image=img

    def loadanh(anh):
        manganh=anh.split()
        for i in range(5):
            threading.Thread(target=gananh,args=(manganh,i,)).start()

    def menusinhvien():
        win.destroy()
        sinhvien.main()
    def menutaikhoan():
        win.destroy()
        taikhoan.main()
    def menuthongke():
        win.destroy()
        thongke.main()
    def menudiemdanh():
        win.destroy()
        diemdanh.main()
    def trolai():
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
   
    def capnhat():

        anh=""
        id=masv
        malop=malop_masv(masv)
        tenlop=tenlop_ma(malop)

        #thêm id , name vào co sở dữ liệu
        lop=tenlop.replace(" ","_")
        lop=khong_dau(lop)

        try:
            f=open("mahoa/"+lop+"mahoa.pkl","rb")
            embed_dictt=pickle.load(f)
            f.close()
        except:
            embed_dictt={}

        try:
            embed_dictt.pop(masv)
        except:print("không có mã trong facefrint")

        camera=[]
        for i in range(0, 2):
            cap = cv2.VideoCapture(i+cv2.CAP_DSHOW)
            test, frame = cap.read()
            if test==True: 
                camera.append(i)
        if camera != []:
            webcam = cv2.VideoCapture(max(camera) + cv2.CAP_DSHOW)
        # webcam = cv2.VideoCapture("kha.mp4")

        dem=0
        while True:
            print(dem)
            check, frame = webcam.read()
            
            # Thay đổi kích thước trong opencv
            #frame: màn hình là hình ảnh đầu vào
            #(0, 0), fx=0.25, fy=0.25 : kích thước mong muốn cho hình ảnh đầu
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
            face_locations = face_recognition.face_locations(rgb_small_frame)
            for (top_s, right, bottom, left) in face_locations:
                top_s=top_s*4
                right=right*4
                bottom=bottom*4
                left=left*4
                cv2.rectangle(frame, (left, top_s), (right, bottom), (0,255,0), 2)
                cv2.putText(frame,str(dem+1),(10,50),cv2.FONT_HERSHEY_SIMPLEX,2, (0, 255, 0), 2)
            if cv2.waitKey(1) & 0xFF == ord('s')  :
                try: 
                    if face_locations != [] and dem <=4: #nếu có khuôn mặt
                        cv2.imwrite('img_anhsv/'+str(id)+str(dem+1)+'.png',frame)
                        face_encoding = face_recognition.face_encodings(frame)[0] #mã hoá và lưu vào biến face_encoding
                        anh=anh+' '+str(id)+str(dem+1)+'.png'
                        if id in embed_dictt: #Nếu id đã tồn tại thì cộng thêm hình ảnh đã mã hoá vào
                            embed_dictt[id]+=[face_encoding]
                        else:#Nếu chưa tồn tại thì khởi tạo với "id"="dữ liệu hình ảnh mã hoá"
                            embed_dictt[id]=[face_encoding]
                    dem +=1
                except: continue
            elif dem>5 and face_locations and dem<20 and face_locations != [] and len(face_locations) == 1:
                try:
                    face_encoding = face_recognition.face_encodings(frame)[0]
                    if id in embed_dictt: 
                        embed_dictt[id]+=[face_encoding]
                    else:
                        embed_dictt[id]=[face_encoding]
                    dem +=1
                except:continue
                
            if dem==20:
                messagebox.showinfo("thông báo", "Đã lưu")
                webcam.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow("Capturing", frame)

        sv.suaanh(anh,id)
        f=open("mahoa/"+lop+"mahoa.pkl","wb")
        pickle.dump(embed_dictt,f)
        f.close()

        anh=sv.anh(masv)
        upload_anh(masv)
        threading.Thread(target=loadanh,args=(anh,)).start()
        threading.Thread(target=upload_filemahoa,args=("mahoa/"+lop+"mahoa.pkl",)).start()

    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.iconbitmap(r"img/iconphanmem.ico")
    win.title("Ảnh sinh viên")
    img_bg=ImageTk.PhotoImage(file="img/bg_xemhinh.png")
 
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl.png")
    ing_btncapnhat=ImageTk.PhotoImage(file="img/btncapnhat.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btntrolai=ImageTk.PhotoImage(file="img/btn_trolai.png")


    bg=Canvas(win,width=1000,height=600,bg="white")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)


    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD', command=menusinhvien)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,activebackground='#857EBD',command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD',command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=40)

    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()

    tengv=tengv_email(d[0])
    tensv=StringVar()
    tensv.set(sv.tensv_ma(masv))
    Label(bg,text=tengv,font=("Baloo Tamma 2 Medium",13),fg="#A672BB",bg="white").place(x=45,y=35)

    f1=Frame(bg,bg="white",width=100,height=120)
    f1.place(x=310,y=120)
    f2=Frame(bg,bg="white",width=100,height=120)
    f2.place(x=540,y=120)
    f3=Frame(bg,bg="white",width=100,height=120)
    f3.place(x=770,y=120)
    f4=Frame(bg,bg="white",width=100,height=120)
    f4.place(x=400,y=300)
    f5=Frame(bg,bg="white",width=100,height=120)
    f5.place(x=630,y=300)


    img=Image.open("img_anhsv/aa.jpg")
    img.thumbnail((200,200))
    img=ImageTk.PhotoImage(img)
    lb1=Label(f1,image=img,bg="white")
    lb1.pack()
    lb1.image=img

    lb2=Label(f2,image=img,bg="white")
    lb2.pack()
    lb2.image=img

    lb3=Label(f3,image=img,bg="white")
    lb3.pack()
    lb3.image=img

    lb4=Label(f4,image=img,bg="white")
    lb4.pack()
    lb4.image=img

    lb5=Label(f5,image=img,bg="white")
    lb5.pack()
    lb5.image=img
    
    anh=sv.anh(masv)
   
    if anh=="":
        anh='aa.jpg aa.jpg aa.jpg aa.jpg aa.jpg'

    btn_capnhat=Button(bg,image=ing_btncapnhat,bd=0,highlightthickness=0,command=capnhat)
    btn_capnhat.place(x=618,y=518)
    btn_trolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=trolai)
    btn_trolai.place(x=948,y=2)

    Label(bg,text = masv,font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#EEE0EE").place(x=450,y=59)
    Label(bg,textvariable = tensv,font=("Baloo Tamma 2 Medium",14),fg="#5F1965",bg="#F5E1EC").place(x=730,y=59)
    
    threading.Thread(target=loadanh,args=(anh,)).start()
    win.mainloop()
if __name__ == '__main__':
    main()
