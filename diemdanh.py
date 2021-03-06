from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox
from backend.dl_khoa import khoa_co_quyen_all
import dangnhap
import socket
import pickle
import cv2
import face_recognition
import sinhvien
import thongke
import diemdanh_bu
import taikhoan
import backend.dl_diemdanh as diemdanh
from backend.dl_tkb import lop_matkb
from backend.dl_thongke import  luughichu_dd
from backend.dl_giangvien import tengv_email,makhoa_email,magv_email
from backend.dl_adminlop import malop_ten,tenlop_ma
from backend.dl_monhoc import mamh_ten
from backend.dl_sinhvien import ds_ma_sv, lop_khoa, tensv_ma,malop_masv
import numpy as np
from tkinter import ttk
from datetime import datetime
import re
import threading
# from speak import speak
import thietlap
from kt_nhap import khong_dau
from uploadfile import download_filemahoa, load
from styletable import style, update
from random import randrange
from time import strftime
import time as t
from numpy import asarray

def main():
    
    def diemdanhvaobang(masv, tt,tg, vao_ra):
        row_id=tv.get_children()
        for i in row_id:
            a=tv.item(i)['values']
            if str(a[1]) == str(masv) and vao_ra == 0:
                tv.item(i, text="", values=(a[0], a[1],a[2],str(tt),tg, a[5], a[6],))
            elif str(a[1]) == str(masv) and vao_ra==1:
                tv.item(i, text="", values=(a[0], a[1],a[2],str(tt),a[4],tg, a[6],))


    def chondong(event):
        rowid = tv.identify_row(event.y)
        txt_ghichu.delete(1.0,END)
        item = tv.item(tv.focus())
        txt_ghichu.insert(END,item['values'][6])
        data_masv.set(item['values'][1])


    def timkiem():
        row=diemdanh.timkiem_dd(matkb.get(),ndtimkiem.get())
        update(tv,row)
        loadding(1)
        btnkhoiphuc['state']='normal'

    def khoiphuc():
        loadding(1)
        ndtimkiem.set("")
        if quyen == str(1):
            malop=malop_ten(data_lop.get())
            row=diemdanh.bangdiemdanh1(matkb.get(),malop)
        else:row=diemdanh.bangdiemdanh(matkb.get())
        capnhatbang(row)
        loadding(0)
    
    def capnhatbang(row):
        tv.delete(*tv.get_children())
        global dem
        dem=0
        for i in row:
            i.insert(0,dem+1)
            i[2]= tensv_ma(i[2])
            if dem%2==0:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
            else:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
            dem += 1
            
    def luong(ham):
        threading.Thread(target=ham).start()

    def loadl_dd():
        try:
            loadding(1)
            global malop
            global mamh
            global magv
            global a
            global ref_dictt
            global embed_dictt
            global dd
            global dd_ra
            global tg_tre
            global tgbd
            global ma
            global sv_da_vao
        
            ma=matkb.get()
            magv=ma_gv.get()
            mamh=mamh_ten(data_mon.get())
            
            ref_dictt = {}
            embed_dictt = {}
            sv_da_vao=[]
            a=[]
            
            if quyen == str(1):
                val_lop = lop_matkb(matkb.get())
                for i in val_lop:
                    lopp=khong_dau(i).replace(" ","_")
                    f=open("mahoa/"+lopp+".pkl","rb")
                    tensv=pickle.load(f) #?????c file v?? luu t??n theo id v??o bi???n ref_dictt
                    f.close()
                    g=open("mahoa/"+lopp+"mahoa.pkl","rb")
                    mahoasv=pickle.load(g) #?????c file v?? luu h??nh ???nh ???? bi???t ???????c m?? ho??  theo id v??o bi???n embed_dictt
                    g.close()
                    malop=malop_ten(i)
                    sv_da_vao += diemdanh.sv_da_dd_vao1(ma,malop)
                    a=a+ds_ma_sv(malop)
                    ref_dictt={**ref_dictt,**tensv}
                    embed_dictt={**embed_dictt,**mahoasv}
            else:
                malop=malop_ten(data_lop.get())
                a=ds_ma_sv(malop)
                lopp=khong_dau(data_lop.get().replace(" ","_"))
                f=open("mahoa/"+lopp+".pkl","rb")
                ref_dictt=pickle.load(f) #?????c file v?? luu t??n theo id v??o bi???n ref_dictt
                f.close()
                g=open("mahoa/"+lopp+"mahoa.pkl","rb")
                embed_dictt=pickle.load(g) #?????c file v?? luu h??nh ???nh ???? bi???t ???????c m?? ho??  theo id v??o bi???n embed_dictt
                g.close()
                sv_da_vao=diemdanh.sv_da_dd_vao(ma)
            dd=diemdanh.dd_sv_vao(ma)
            dd_ra=diemdanh.dd_sv_ra(ma)
            tgbd= diemdanh.tgbd_dd(ma)
            tg_tre = doigiaytre(diemdanh.tg_tre(magv))
            loadding(0)
        except: loadl_dd()

    def load_gd():
        global val_lop
        tengv.set(tengv_email(d[0]))
        ma_gv.set(magv_email(d[0]))
        makhoa.set(makhoa_email(d[0]))
        thongtin = diemdanh.thong_tin_theo_tkb(ma_gv.get(),ngay,ca)
        if thongtin == []:
            data_lop.set("B???n kh??ng c?? ti???t gi???ng !")
            data_mon.set("B???n kh??ng c?? ti???t gi???ng !")
            matkb.set("")
        else:
            data_lop.set(thongtin[0])
            data_mon.set(thongtin[1])
            matkb.set(thongtin[2])
            luong(loadl_dd)

        lbgv.config(text=tengv.get())
        if quyen== str(1):
            try:
                val_lop = lop_matkb(matkb.get())
                cblop.config(values=val_lop)
                cblop.current(0)
            except: print("Kh??ng c?? ti???t gi???ng")
        else:
            lblop.config(text=data_lop.get())
        lbmon.config(text=data_mon.get())
        luong(khoiphuc)
        
    
    def lock():
        string=strftime("%H:%M:%S %p")
        dmy=strftime("%d/%m/%Y")
        l.configure(text=string) 
        tg.config(text=dmy)
        l.after(1000,lock)
        
  
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

    def doigiaytre(s):
        i=str(s).replace('.',' ').replace(':'," ").split()
        p=i[0]
        s=i[1]
        giay=int(p)*60+int(s)
        return giay

    def doigiay(s):
        h=str(s)[0:1]
        p=str(s)[2:4]
        s=str(s)[5:7]
        giay=int(h)*60*60+int(p)*60+int(s)
        return giay

    def xulyvao(ma,name):
        # if name not in dd and s >= tg_tre and name != "Khongbiet" and int(tg_tre) != 0 and '1' in real[name] and '2' in real[name]:
        now = datetime.now()
        now=now.strftime("%X")
        format = '%H:%M:%S'
        kq=datetime.strptime(now, format) - datetime.strptime(tgbd, format) #t??nh th???i gian Tr???
        s=doigiay(kq)
        if s >= tg_tre  and int(tg_tre) != 0 and name not in sv_da_vao:
            tre="Tr??? "+str(kq)[0:7]
            sv_da_vao.append(name)
            threading.Thread(target=diemdanh.capnhat_tgvao,args=(ma,name,now,tre)).start()
            threading.Thread(target=gananh_khi_click,args=(name,now)).start()
            diemdanhvaobang(name,tre,now, vao_ra)
        elif name not in sv_da_vao:
            # elif name not in dd and name != "Khongbiet"and '1' in real[name] and '2' in real[name]:
            # diemdanh.xoasv_dd(ma,name)
            threading.Thread(target=diemdanh.capnhat_tgvao,args=(ma,name,now,"c?? m???t")).start()
            sv_da_vao.append(name)
            threading.Thread(target=gananh_khi_click,args=(name,now)).start()
            diemdanhvaobang(name, "c?? m???t",now, vao_ra)

    def xulyra(ma,name):
        dd_ra.append(name)
        now = datetime.now()
        now=now.strftime("%X")
        diemdanhvaobang(name, "c?? m???t",now, vao_ra)
        threading.Thread(target=diemdanh.capnhat_tgra,args=(ma,name,now)).start()
        threading.Thread(target=gananh_khi_click,args=(name,now)).start()

    
    # def mahoa(rgb_small_frame,face_locations,known_face_encodings,known_face_names,frame):
    #     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #m?? ho?? khu??n m???t hi???n t???i trong khung h??nh c???a video
    #     for face_encoding in face_encodings:
    #         # Xem khu??n m???t c?? kh???t c???i c??c khu??n m???t ???? bi???t kh??ng
    #         try:
    #             matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.4)
    #         except:print("l???i")
    #         name = "Unknow"
    #         #????a ra c??c kho???ng c??ch gi???a c??c khu??n m???t v?? khu??n m???t ???? bi???t
    #         face_names=[]
    #         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    #         best_match_index = np.argmin(face_distances) #C??i n??o g???n h??n th?? l??u v??o bi???n best_match_index
    #         if matches[best_match_index]:
    #             name = known_face_names[best_match_index]

    #         now = datetime.now()
    #         now=now.strftime("%X")
    #         if vao_ra==0 and name!= "Unknow":
    #             threading.Thread(target=xulyvao,args=(ma,name,now)).start()
    #         elif name not in dd_ra and name != 'Unknow': 
    #             threading.Thread(target=xulyra,args=(ma,name,now)).start()
    #             dd_ra.append(name)

    def batdaudiemdanh():
        known_face_encodings = []
        known_face_names = []
        for ref_id , embed_list in embed_dictt.items():
            for my_embed in embed_list:
                known_face_encodings += [my_embed]
                known_face_names += [ref_id]
        camera=[]
        for i in range(0, 2):
            cap = cv2.VideoCapture(i+cv2.CAP_DSHOW)
            test, frame = cap.read()
            if test==True: 
                camera.append(i)
        if camera != []:
            webcam = cv2.VideoCapture(max(camera) + cv2.CAP_DSHOW)

            face_locations = []
            face_encodings = []
            process_this_frame = True
            dem=0
            try:
                while True  :
                    ret, frame = webcam.read()
                    # print(frame)
                    rgb_small_frame = frame[:, :, ::-1] # Chuy???n ?????i h??nh ???nh t??? m??u BGR (OpenCV s??? d???ng) sang m??u RGB (face_recognition s??? d???ng)

                    if process_this_frame:
                        face_names = []
                        face_locations = face_recognition.face_locations(rgb_small_frame)# t??m t???t c??? khu??n m???t trong khung h??nh hi???n t???i v???a video
                        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #m?? ho?? khu??n m???t hi???n t???i trong khung h??nh c???a video
                        for face_encoding in face_encodings:
                            # Xem khu??n m???t c?? kh???t c???i c??c khu??n m???t ???? bi???t kh??ng
                            try:
                                matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.4)
                            except:print("l???i")
                            name = "Unknow"
                            #????a ra c??c kho???ng c??ch gi???a c??c khu??n m???t v?? khu??n m???t ???? bi???t
                            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                            best_match_index = np.argmin(face_distances) #C??i n??o g???n h??n th?? l??u v??o bi???n best_match_index
                            if matches[best_match_index]:
                                name = known_face_names[best_match_index]
                            face_names.append(name)

                            if vao_ra==0 and name != "Unknow":
                                xulyvao(ma,name)
                            elif name != "Unknow" and name not in dd_ra :
                                xulyra(ma,name)
                            
                                    
                    process_this_frame = not process_this_frame
                    #Hi???n th??? k???t qu???
                    try:
                        for (top_s, right, bottom, left), name in zip(face_locations, face_names):
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            if name == "Unknow":

                                cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 0,255), 2)
                                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                            else:
                                cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 255,0), 2)
                                cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                                
                                
                    except:print("no name")
                    cv2.imshow('Video', frame)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):

                        webcam.release()
                        if vao_ra==1:
                            threading.Thread(target=diemdanh.kiemtrathongtin,args=(ma,)).start()
                        loadding(0)
                        f2.place_forget()
                        cv2.destroyAllWindows()
                        break
            #     #----------------------------------------------------------------------------
                diemdanh.update_TT_diemdanh(matkb.get())
            except: print("L???i")
        else:messagebox.warning("th??ng b??o","Thi???t b??? ??ang s??? d???ng kh??ng c?? camera")

        
    # #-----------------------------------------------------------------------------------------------------------------------
    def kt ():
        global vao_ra
        vao_ra=0
        catkb=str(diemdanh.catkb(matkb.get()))
        if data_lop.get() == "B???n kh??ng c?? ti???t gi???ng !":
            messagebox.showwarning("th??ng b??o","B???n kh??ng c?? ti???t d???y")
        elif diemdanh.khoang_tgvao(str(catkb[0]))==False:
            messagebox.showwarning("th??ng b??o","???? h???t th???i gian ??i???m danh v??o")
        else:
            for i in range(0,len(a)):
                if a[i] not in dd:
                    malop=malop_masv(a[i])
                    dd.append(a[i])
                    threading.Thread(target = diemdanh.diem_danh_vao_csdl, args = (matkb.get(),a[i],"v???ng",str(malop),mamh,magv,ngay,ca,"")).start()
            luong(hen_ngay_xoa)
            luong(khoiphuc)
            luong(batdaudiemdanh)
        try:
            lb1.pack()
            lb2.pack()
        except:return
    def kt_tgra ():
        global vao_ra
        vao_ra=1
        catkb=str(diemdanh.catkb(matkb.get()))
        vt=len(catkb)-1
        if data_lop.get() == "B???n kh??ng c?? ti???t gi???ng !":
            messagebox.showwarning("th??ng b??o","B???n kh??ng c?? ti???t d???y")
        elif diemdanh.khoang_tgra(catkb[vt])==False:
            messagebox.showwarning("th??ng b??o","Ch??a ?????n th???i gian ??i???m danh ra")
        else:
            for i in range(0,len(a)):
                if a[i] not in dd:
                    malop=malop_masv(a[i])
                    dd.append(a[i])
                    threading.Thread(target = diemdanh.diem_danh_vao_csdl, args = (matkb.get(),a[i],"v???ng",str(malop),mamh,magv,ngay,ca,"")).start()
            luong(batdaudiemdanh)
            loadding(1)
        try:
            lb1.pack()
            lb2.pack()
        except:return

    def hen_ngay_xoa():
        if diemdanh.kt_hen_ngay_xoa(matkb.get()) == False or diemdanh.kt_hen_ngay_xoa(matkb.get()) == None:
            diemdanh.hen_ngay_xoa_du_lieu(matkb.get(),ngay)

    def loadding(a):
        if a==1:# ??ang load d??? li???u
            lb_loadding.place(x=1120,y=2)
            tl["state"] = "disabled"
            btndangxuat["state"] = "disabled"
            btnkhoiphuc["state"] = "disabled"
            btntimkiem["state"] = "disabled"
            btnghichu["state"] = "disabled"
            btndiemdanhra["state"] = "disabled"
            btndiemdanh["state"] = "disabled"
            
        else:
            lb_loadding.place_forget()
            tl["state"] = "normal"
            btndangxuat["state"] = "normal"
            btnkhoiphuc["state"] = "normal"
            btntimkiem["state"] = "normal"
            btnghichu["state"] = "normal"
            btndiemdanhra["state"] = "normal"
            btndiemdanh["state"] = "normal"
            
    def gan_anh(path):
        img=Image.open(path)
        img.thumbnail((150,150))
        img=ImageTk.PhotoImage(img)
        lb1.config(image=img)
        lb1.image=img
    def gananh_khi_click(masv,tgra):
        f2.place(x=838,y=80)
        if masv != "Unknow" :
            anh=str(masv)+"1.png"
            if(anh==""):
                gan_anh("img_anhsv/aa.jpg")
            else:
                gan_anh("img_anhsv/aa.jpg")
                gan_anh(load(anh))
            lb2.config(text="Th???i gian: "+tgra)
            lb3.config(text=tensv_ma(masv))
        else:
            gan_anh("a.png")
            lb2.config(text="Th???i gian: "+tgra)
            lb3.config(text="Ch??a x??c ?????nh")
            

    def xem_ghichu():
        if data_masv.get() != "":

            frame_ghichu.place(x=330,y=110)
            frame_ghichu.config(bg="white")
            lb_ghichu.config(text="Ghi ch??",background="white")
            txt_ghichu.pack(padx=20)
            btn_trolai.pack(side="right",padx=10,pady=10)
            btn_luu.pack(side="right",padx=10,pady=10)
        
    def trolai():
        frame_ghichu.place_forget()
        txt_ghichu.delete(1.0,END)

    def luu_ghichu():
        if luughichu_dd(ma,data_masv.get(),txt_ghichu.get("1.0",END)) == True:
            threading.Thread(target=khoiphuc).start()
            messagebox.showinfo("th??ng b??o","???? l??u ghi ch??")
            trolai()
        else: 
            messagebox.showerror("th??ng b??o","L??u kh??ng th??nh c??ng")
            

    def thietlaptre():
        win.destroy()
        thietlap.main()
    def dd_bu():
        win.destroy()
        diemdanh_bu.main(0)
            
    def menutaikhoan():
        win.destroy()
        taikhoan.main()

    def menuthongke():
        win.destroy()
        thongke.main()

    def menuthemsv():
        win.destroy()
        sinhvien.main()

    def dangxuat():
        if messagebox.askyesno("Th??ng b??o","B???n c?? th???c s??? mu???n ????ng xu???t ?"):
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
    win.title("??i???m danh sinh vi??n")
    img_bg=ImageTk.PhotoImage(file="img/bg_diemdanh.png")
    
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh1.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btndiemdanh=ImageTk.PhotoImage(file="img/btndiemdanh.png")
    ing_btntgra=ImageTk.PhotoImage(file="img/diemdanhra.png")
    ing_btntam=ImageTk.PhotoImage(file="img/anhtam.png")
    ing_btnthetlap=ImageTk.PhotoImage(file="img/thietlap.png")
    ing_btndd_bu=ImageTk.PhotoImage(file="img/chuadd.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    img_btnluu = ImageTk.PhotoImage(file="img_admin/btnluu.png")
    img_btntrove = ImageTk.PhotoImage(file="img_admin/btn_trolai1.png")
    img_btnghichu = ImageTk.PhotoImage(file="img_admin/btn_ghichu.png")
    
    bg=Canvas(win,width=1200,height=800,bg="white")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(600,400,image=img_bg)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthemsv)
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,activebackground='#857EBD',highlightthickness=0)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD', command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD', command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)
#_______________________________________________________________________________________________________________________________
    
    #d??? li???u hi???n l???p, m??n
    ten_thiet_bi = socket.gethostname()
    d=[]
    # bi???n t???m ????? t??? ?????ng c???p nh???t b???ng
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()
    makhoa=StringVar()
    tengv=StringVar()
    ma_gv=StringVar()
    ca=diemdanh.cahoc()
    time = datetime.now()
    now = time.strftime("%x")
    ngay=dinh_dang_ngay(now)
    matkb=StringVar()
    data_lop=StringVar()
    data_mon=StringVar()
    ndtimkiem=StringVar()
    data_masv=StringVar()
    makhoa.set(makhoa_email(d[0]))

    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=38)
    global quyen
    quyen=khoa_co_quyen_all(makhoa.get())
    if quyen == str(1) :
        cblop = Combobox(bg,textvariable=data_lop,font=("Baloo Tamma 2 Medium",11),justify="center",state='readonly', width=27)
        # cblop.bind('<<ComboboxSelected>>', chonlop)
        cblop.place(x=460,y=107)
        Frame(bg,width=268,height=2,bg="white").place(x=460,y=107)
        Frame(bg,width=3,height=30,bg="white").place(x=460,y=107)
        Frame(bg,width=268,height=2,bg="white").place(x=460,y=137)
    else:
        lblop=Label(bg,font=("Baloo Tamma 2 Medium",10),justify='center',bg="white",fg="black",width=35)
        lblop.place(x=475,y=110)

    lbmon=Label(bg,font=("Baloo Tamma 2 Medium",10),justify='center',bg="white",fg="black",width=37)
    lbmon.place(x=460,y=150)

    #n??t ??i???m diemdanh
    btndiemdanh = Button(bg,image=ing_btndiemdanh,bd=0,highlightthickness=0,command=kt)
    btndiemdanh.place(x=368,y=221)
    btndiemdanhra = Button(bg,image=ing_btntgra,bd=0,highlightthickness=0,command=kt_tgra)
    btndiemdanhra.place(x=591,y=221)

    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,activebackground='white',command=timkiem)
    btntimkiem.place( x=1080,y=373)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground='white',command=khoiphuc)
    btnkhoiphuc.place(x=1116,y=373)
    txt_timkiem=Entry(bg,width=25,bd=0,font=("Baloo Tamma 2 Medium",12),textvariable=ndtimkiem,highlightthickness=0)
    txt_timkiem.place(x=845,y=371)
    #bang diemdanh

    tl=Button(bg,image=ing_btnthetlap,bd=0,highlightthickness=0,command=thietlaptre)
    tl.place(x=1145,y=7)
    dd_bu=Button(bg,image=ing_btndd_bu,bd=0,highlightthickness=0,command=dd_bu)
    dd_bu.place(x=1090,y=7)

    # t???o stype cho b???ng
    style()
    # t???o fram cho b???ng
    fr_tb = Frame(bg)
    fr_tb.place(x=330,y=475)

    #t???o thanh cu???n 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")
   
    tv = ttk.Treeview(fr_tb, columns=(1,2,3,4,5,6,7),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=50,anchor=CENTER )
    tv.column(2, width=100,anchor=CENTER )
    tv.column(3, width=200)
    tv.column(4, width=130,anchor=CENTER)
    tv.column(5, width=90,anchor=CENTER)
    tv.column(6, width=90,anchor=CENTER)
    tv.column(7, width=150,anchor=CENTER)
    # tv.column(5, width=120)
    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="M?? sinh vi??n")
    tv.heading(3,text="H??? t??n")
    tv.heading(4,text="Th??ng tin")
    tv.heading(5,text="Th???i gian v??o")
    tv.heading(6,text="Th???i gian ra")
    tv.heading(7,text="Ghi ch??")
    # tv.heading(5,text="Ghi ch??")
    tv.pack()
    tree_scroll.config(command=tv.yview)
    
    tv.bind('<ButtonRelease-1>', chondong)
    tv.tag_configure("ollrow" ,background="white",font=('Baloo Tamma 2 Medium',10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))

    # ?????ng h???
    l = Label(bg, font=("Digital-7",12),background="white",foreground="black")
    l.place(x=460,y=2)
    tg = Label(bg, font=("Digital-7",12),background="white",foreground="black")
    tg.place(x=365,y=2)
    lock()
    f2=Frame(bg,background="#FCE2E9")
    

    lb1=Label(f2,background="#FCE2E9")
    lb1.pack()
    lb3=Label(f2,background="#FCE2E9")
    lb3.pack()
    lb2=Label(f2,background="#FCE2E9")
    lb2.pack()
    

    #ghi ch??
    btnghichu=Button(bg,image=img_btnghichu,bd=0,highlightthickness=0,activebackground='white',command=xem_ghichu)
    btnghichu.place(x=1105,y=424)

    frame_ghichu=Frame(bg,background="#E8DFF1")
    lb_ghichu=Label(frame_ghichu,font=("Baloo Tamma 2 Medium",14),fg="#A672BB")
    lb_ghichu.pack()

    txt_ghichu=Text(frame_ghichu,width=60,height=6,bd=1,background="#F1F1F1",font=("Baloo Tamma 2 Medium",10))
    btn_trolai= Button(frame_ghichu,image=img_btntrove,bd=0,highlightthickness=0,activebackground="white",command=trolai)
    btn_luu= Button(frame_ghichu,image=img_btnluu,bd=0,highlightthickness=0,activebackground="white",command=luu_ghichu)
    lb_loadding=Label(bg,text=" ??ang t???i . . . " ,font=("Baloo Tamma 2 Medium",12),bg="#FFF4FF",fg="#AD7B98")

    loadding(1)
    luong(load_gd)
    
    win.mainloop()

if __name__ == '__main__':
    main()