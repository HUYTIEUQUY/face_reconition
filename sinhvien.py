from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
import shutil
from tkinter import messagebox
import dangnhap
import socket
import xemhinh
import pickle
import cv2
import face_recognition
import diemdanh
import thongke
import taikhoan
import re
import xlsxwriter
import pandas as pd
from backend.dl_giangvien import tengv_email,makhoa_email,magv_ten
from backend.dl_adminlop import malop_ten, tenlop_ma
import backend.dl_sinhvien as sv
import threading
import kt_nhap as kt
from uploadfile import upload_anh, load,deleteanh,upload_filemahoa
from styletable import style
from backend.dl_khoa import khoa_co_quyen_all


def main():
    def loadding(a):
        if a==1:# đang load dữ liệu
            lb_loadding.place(x=1120,y=20)
            btnexcelxuat['state']='disabled'
            btnexcelnhap['state']='disabled'
            btnkhoiphuc['state']='disabled'
            btntimkiem['state']='disabled'
            btnthem['state']='disabled'
            btnsua['state']='disabled'
            btnxoa['state']='disabled'
        else:
            lb_loadding.place_forget()
            btnexcelxuat['state']= 'normal'
            btnexcelnhap['state']='normal'
            btnkhoiphuc['state']='normal'
            btntimkiem['state']='normal'
            btnthem['state']='normal'
            btnsua['state']='normal'
            btnxoa['state']='normal'
        

    def gan_anh(path):
        img=Image.open(path)
        img.thumbnail((180,180))
        img=ImageTk.PhotoImage(img)
        lb1.config(image=img)
        lb1.image=img

    def luong(ham):
        threading.Thread(target=ham).start()

    def loaddl():
        tengv.set(tengv_email(d[0]))
        makhoa.set(makhoa_email(d[0]))
        global quyen
        quyen=khoa_co_quyen_all(makhoa.get())
        if quyen == str(1):
            data_lop = sv.all_lop()
        else:
            data_lop=sv.lop_khoa(makhoa.get())
        lbgv.config(text=tengv.get())
        cb_lop.config(values=data_lop)
        cb_lop.current(0)
        
        khoiphuc()

    def nhap_excel():
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Mở file excel ",filetypes=(("XLSX file","*.xlsx"),("All file","*.*")))
        ko_luu=[]
        malop=malop_ten(cb_lop.get())
        lop=kt.khong_dau(cb_lop.get()).replace(" ","_")
        xl = pd.ExcelFile(fln)
        df = pd.read_excel(xl, 0) 
        for i in range(df.shape[0]):
            masv=df['Mã sinh viên'][i]
            tensv=df['Tên sinh viên'][i]
            if sv.kt_masv_tontai(masv) !=[]:
               ko_luu.append(masv)
            else:
                sv.themsv(masv,tensv,malop,"")
                try:
                    f=open("mahoa/"+lop+".pkl","rb")
                    ref_dictt=pickle.load(f)
                    f.close()
                except:
                    ref_dictt={}
                ref_dictt[masv]=tensv
                try:
                    f=open("mahoa/"+lop+".pkl","wb")
                    pickle.dump(ref_dictt,f)
                    f.close()
                except:
                    return
                

        if ko_luu !=[]:
            messagebox.showerror("thông báo","Mã sinh viên đã tồn tại\n"+str(ko_luu))
        else: messagebox.showinfo("thông báo","Thêm sinh viên thành công")
        luong(khoiphuc)
        threading.Thread(target=upload_filemahoa,args=("mahoa/"+lop+".pkl",)).start()

    def xuat_excel():
        loadding(1)
        malop=malop_ten(cb_lop.get())
        row =sv.bangsv(malop)
        if len(row)<1:
            messagebox.showwarning("thông báo","Không có dữ liệu xuất file excel !")
            return False
        else:
            try:
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Lưu file excel",filetypes=(("XLSX File","*.xlsx"),("All File","*.*")))
                if fln != "":
                    a=sv.dong_ma_sv(malop)
                    b=sv.dong_ten_sv(malop)
                    out_workbook = xlsxwriter.Workbook(fln+".xlsx")
                    outsheet = out_workbook.add_worksheet()
                    outsheet.write("A1","Mã sinh viên")
                    outsheet.write("B1","Tên sinh viên")
                    
                    def write_data_to_file(array,x):
                        for i in range(len(array)):
                            outsheet.write(i+2,x,array[i])
                    write_data_to_file(a,0)
                    write_data_to_file(b,1)
                    out_workbook.close()
                    messagebox.showinfo("thông báo","Đã xuất thành công ")
            except:print("Error")
            loadding(0)
    
    def khoiphuc():
        loadding(1)
        macu.set("")
        ma.set("")
        ten.set("")
        ndtimkiem.set("")
        malop=malop_ten(cb_lop.get())
        row=sv.bangsv(malop)
        update(row)
        gan_anh("img/bg_themdl2.png")
        lb2.config(text="")
        btn_xemanh.config(image=img_btnxem2)
        loadding(0)
        
    def update(row):
        tv.delete(*tv.get_children())
        global dem
        dem=0
        for i in row:
            i.insert(0,dem+1)
            if dem%2==0:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
            else:
                tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
            dem += 1

    def capnhat(event):
        loadding(1)
        malop=malop_ten(cb_lop.get())
        row=sv.bangsv(malop)
        update(row)
        img=Image.open("img/bg_themdl2.png")
        img.thumbnail((180,180))
        img=ImageTk.PhotoImage(img)
        lb1.config(image=img)
        lb1.image=img
        lb2.config(text="")
        btn_xemanh.config(image=img_btnxem2)
        loadding(0)
        
    def timkiem():
        malop=malop_ten(lop.get())
        row=sv.timsv(malop,ndtimkiem.get())
        if row ==[]:
            messagebox.showwarning("thông báo","Không tìm được kết quả")
            update(row)
        else:
            update(row)

    def xemanh():
        win.destroy()
        xemhinh.main(ma.get())

    def getrow(event):
        rowid=tv.identify_row(event.y)
        item=tv.item(tv.focus())
        ten.set(item['values'][2])
        ma.set(item['values'][1])
        macu.set(item['values'][1])
        anh=sv.anh(ma.get()).split()
        lb2.config(text=item['values'][1])
        threading.Thread(target=gananh_khi_click,args=(anh,)).start()
        
    def gananh_khi_click(anh):
        if(anh==[]):
            gan_anh("img_anhsv/aa.jpg")
        else:
            gan_anh("img_anhsv/aa.jpg")
            gan_anh(load(anh[0]))
        btn_xemanh.config(image=img_btnxem)

    def sua():
        if macu.get()=="":
            messagebox.showerror("thông báo","Chưa có dữ liệu sửa. \nHãy nhấn 2 lần vào dòng dữ liệu, thay đổi tên và cập nhật")
        elif ma.get()=="" or ten.get() == "" :
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
        elif kt_dau_khoangcach(ma.get())==False or kt_dau_khoangcach(ten.get())==False:
            messagebox.showwarning("thông báo","Dữ liệu không hợp lệ")
        elif(ma.get()!=macu.get()):
            messagebox.showerror("thông báo","Bạn không được sửa mã")
            ma.set(macu.get())
        else:
            masv=ma.get()
            tensv=ten.get()
            sv.suasv(masv,tensv)
            # xoa_sv_matran(masv)
            suamatran()
            messagebox.showinfo("thông báo","Bạn đã sửa thành công")
            #sửa bảng
            row_id=tv.get_children()
            for i in row_id:
                a=tv.item(i)['values']
                if str(a[1]) == str(masv):
                    tv.item(i, text="", values=(a[0], a[1],tensv,))


    def suamatran():
        id=ma.get()
        namemahoa=kt.khong_dau(ten.get())
        lop=cb_lop.get().replace(" ","_")
        lopmahoa=kt.khong_dau(lop)
        try:
            f=open("mahoa/"+lopmahoa+".pkl","rb")
            ref_dictt=pickle.load(f)
            f.close()
        except:
            ref_dictt={}
        ref_dictt[id]=namemahoa
        f=open("mahoa/"+lopmahoa+".pkl","wb")
        pickle.dump(ref_dictt,f)
        f.close()

    def xoa():
        if messagebox.askyesno("thông báo","Bạn có thực sự muốn xoá"):
            x=tv.selection()
            listma = []
            ko_xoa=[]
            for i in x:
                listma.append(tv.item(i,'values')[1])
            for i in listma:
                if sv.kt_sv_diemdanh(i)== False:
                    sv.xoasv(i)
                    luong(khoiphuc)
                    try:
                        xoa_sv_matran(i)#xoá mahoa anh 
                    except:print("xoá sv ma trận thất bại")
                else:
                    ko_xoa.append(i)
            if(ko_xoa!=[]):
                messagebox.showwarning("thông báo","Không thể xoá sinh viên có mã "+str(ko_xoa))
            tenlop=kt.khong_dau(lop.get()).replace(" ","_")
            path ="mahoa/"+tenlop+"mahoa.pkl"
            pathten ="mahoa/"+tenlop+".pkl"
            threading.Thread(target=upload_filemahoa,args=(path,)).start()
            threading.Thread(target=upload_filemahoa,args=(pathten,)).start()
        else: return

    def xoa_sv_matran(masv):
        tenlop=lop.get().replace(" ","_")
        lopmahoa=kt.khong_dau(tenlop)
        with open("mahoa/"+str(lopmahoa)+"mahoa.pkl","rb") as f:
            ref_dictt=pickle.load(f)
            ref_dictt.pop(masv)
        file= open("mahoa/"+str(lopmahoa)+"mahoa.pkl","wb") 
        pickle.dump(ref_dictt,file)
        file.close()
       
        with open("mahoa/"+str(lopmahoa)+".pkl","rb") as f:
            ref_dictt=pickle.load(f)
            ref_dictt.pop(masv)
        file= open("mahoa/"+str(lopmahoa)+".pkl","wb") 
        pickle.dump(ref_dictt,file)
        file.close()

    # def xoaanh(masv):
    #     for i in range(5):
    #         os.remove("img_anhsv/"+str(masv)+str(i+1)+".png")

    def menutaikhoan():
        win.destroy()
        taikhoan.main()
    def menuthongke():
        win.destroy()
        thongke.main()
    def menudiemdanh():
        win.destroy()
        diemdanh.main()
    def dangxuat():
        if messagebox.askyesno("Thông báo","Bạn có thực sự muốn đăng xuất ?"):
            ten_thiet_bi = socket.gethostname()
            file=open(ten_thiet_bi+".txt","w")
            file.write("")
            file.close()
            win.destroy()
            dangnhap.main()
        else: return
    
    def kt_dau_khoangcach(s):
        return bool(s and s.strip())
    
    def xoa_khoangcach(s):
        s=s.split()
        a=""
        for i in s:
            a=a+i+" "
        return a

    def kt_kitudacbiet(s):
        s=xoa_khoangcach(s).replace(" ","")
        s=kt.khong_dau(s)
        kitu = re.sub(r"[a-zA-Z0-9]","",str(s))
        return kitu

    def kt_nhap():
        if ma.get()=="" or ten.get() == "" :
            messagebox.showwarning("thông báo","Hãy nhập đầy đủ dữ liệu")
        elif kt_dau_khoangcach(ma.get())==False or kt_dau_khoangcach(ten.get())==False or kt_kitudacbiet(ten.get()) != "":
            messagebox.showwarning("thông báo","Dữ liệu không hợp lệ")
        elif str(ma.get()).isnumeric()==False or len(str(ma.get()))!=10:
            messagebox.showwarning("thông báo","Kiểm tra lại mã sinh viên")
        elif sv.kt_masv_tontai(ma.get()) !=[]:
            messagebox.showerror("thông báo","Mã sinh viên đã tồn tại")
        else:
            luong(themdlkhuonmat)


    def themdlkhuonmat():
        soanh=5
        anh=""
        id=txt_masv.get()
        name=xoa_khoangcach(txt_hoten.get())
        name_mahoa=kt.khong_dau(name)
        malop=malop_ten(cb_lop.get())
        #thêm id , name vào co sở dữ liệu
        lop=cb_lop.get().replace(" ","_")
        lop=kt.khong_dau(lop)
        try:
            f=open("mahoa/"+lop+".pkl","rb")
            ref_dictt=pickle.load(f)
            f.close()
        except:
            ref_dictt={}
        ref_dictt[id]=name_mahoa

        try:
            f=open("mahoa/"+lop+".pkl","wb")
            pickle.dump(ref_dictt,f)
            f.close()
        except:
            return

        try:
            f=open("mahoa/"+lop+"mahoa.pkl","rb")
            embed_dictt=pickle.load(f)
            f.close()
        except:
            embed_dictt={}

        camera=[]
        for i in range(0, 2):
            cap = cv2.VideoCapture(i+cv2.CAP_DSHOW)
            test, frame = cap.read()
            if test==True: 
                camera.append(i)
        if camera != []:
            webcam = cv2.VideoCapture(max(camera) + cv2.CAP_DSHOW)
        # webcam = cv2.VideoCapture("hai.mp4")

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
                if cv2.waitKey(1) & 0xFF == ord('s') : 
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
                    face_encoding = face_recognition.face_encodings(frame)[0]
                    if id in embed_dictt: 
                        embed_dictt[id]+=[face_encoding]
                    else:
                        embed_dictt[id]=[face_encoding]
                    dem +=1
                
            if dem==20:
                messagebox.showinfo("thông báo", "Đã lưu")
                webcam.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow("Capturing", frame)
            # thoát khỏi camera
        
        threading.Thread(target=upload_anh, args=(id,)).start()
        sv.themsv(id,name,malop,anh)
        f=open("mahoa/"+lop+"mahoa.pkl","wb")
        pickle.dump(embed_dictt,f)
        f.close()
        threading.Thread(target=upload_filemahoa, args=("mahoa/"+lop+"mahoa.pkl",)).start()
        threading.Thread(target=upload_filemahoa, args=("mahoa/"+lop+".pkl",)).start()
        khoiphuc()


    win=Tk()
    win.geometry("1000x600+300+120")
    win.resizable(False,False)
    win.iconbitmap(r"img/iconphanmem.ico")
    win.config(bg="green")
    win.title("Quản lý thông tin sinh viên")
    img_bg=ImageTk.PhotoImage(file="img/bg_themdl.png")
 
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    img_btnthem=ImageTk.PhotoImage(file="img_admin/btn_them.png")
    img_btnxem=ImageTk.PhotoImage(file="img/btn_xem.png")
    img_btnxem2=ImageTk.PhotoImage(file="img/btn_xem2.png")
    img_btnsua=ImageTk.PhotoImage(file="img_admin/btn_sua.png")
    img_btnxoa=ImageTk.PhotoImage(file="img_admin/btn_xoa.png")
    img_btntimkiem=ImageTk.PhotoImage(file="img_admin/btn_timkiem.png")
    img_btnkhoiphuc=ImageTk.PhotoImage(file="img_admin/btn_khoiphuc.png")
    img_btnexcel_nhap=ImageTk.PhotoImage(file="img_admin/nhap_excel.png")
    img_btnexcel_xuat=ImageTk.PhotoImage(file="img_admin/xuat_excel.png")

    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    #chọn lớp

    ma=StringVar()
    macu=StringVar()
    ten=StringVar()
    lop=StringVar()
    ndtimkiem=StringVar()
    
    ten_thiet_bi = socket.gethostname()
    d=[]
    with open(ten_thiet_bi+".txt","r") as file:
        d=file.read().split()

    tengv=StringVar()
    makhoa=StringVar()
    

    
    cb_lop=Combobox(bg,width=34, font=("Baloo Tamma 2 Medium",10),state='readonly',textvariable=lop)
    cb_lop.place(x=580,y=52)
    cb_lop.bind('<<ComboboxSelected>>', capnhat)
    Frame(bg,width=303,height=5,bg= "white").place(x=570,y=52)
    Frame(bg,width=303,height=5,bg= "white").place(x=570,y=76)
    Frame(bg,width=5,height=24,bg= "white").place(x=577,y=52)

    
    txt_masv=Entry(bg,width=32,bd=0,font=("Baloo Tamma 2 Medium",10),textvariable=ma,highlightthickness=0)
    txt_masv.place(x=580,y=90)
    txt_timkiem=Entry(bg,width=25,bd=0,font=("Baloo Tamma 2 Medium",10),textvariable=ndtimkiem,highlightthickness=0)
    txt_timkiem.place(x=660,y=244)
    txt_hoten=Entry(bg,width=32,bd=0,font=("Baloo Tamma 2 Medium",10),textvariable=ten,highlightthickness=0)
    txt_hoten.place(x=580,y=125)


    btnthem=Button(bg,image=img_btnthem,bd=0,highlightthickness=0,command=kt_nhap)
    btnthem.place(x=487,y=185)
    btnsua=Button(bg,image=img_btnsua,bd=0,highlightthickness=0,command=sua)
    btnsua.place(x=637,y=185)
    btnxoa=Button(bg,image=img_btnxoa,bd=0,highlightthickness=0,command=xoa)
    btnxoa.place(x=770,y=185)
    btntimkiem=Button(bg,image=img_btntimkiem,bd=0,highlightthickness=0,activebackground='#ffffff',command=timkiem)
    btntimkiem.place(x=888,y=241)
    btnkhoiphuc=Button(bg,image=img_btnkhoiphuc,bd=0,highlightthickness=0,activebackground='#ffffff',command=khoiphuc)
    btnkhoiphuc.place(x=925,y=241)
    btnexcelnhap=Button(bg,image=img_btnexcel_nhap,bd=0,highlightthickness=0,command=nhap_excel)
    btnexcelnhap.place(x=948,y=2)
    btnexcelxuat=Button(bg,image=img_btnexcel_xuat,bd=0,highlightthickness=0,command=xuat_excel)
    btnexcelxuat.place(x=898,y=2)

    menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,activebackground='#857EBD')
    menuthem.place(x=46,y=129)

    menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,activebackground='#857EBD',command=menudiemdanh)
    menudiemdanh.place(x=46,y=248)

    menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,activebackground='#857EBD',command=menuthongke)
    menuthongke.place(x=46,y=366)

    menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,activebackground='#857EBD',command=menutaikhoan)
    menutaikhoan.place(x=46,y=484)

    btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    btndangxuat.place(x=248,y=44)

    lbgv=Label(bg,font=("Baloo Tamma 2 Medium",12),fg="#A672BB",bg="white")
    lbgv.place(x=45,y=40)
    

    # tạo stype cho bảng
    style()
    # tạo fram cho bảng
    fr_tb = Frame(bg)
    fr_tb.place(x=368,y=300)

    #tạo thanh cuộn 
    tree_scroll = Scrollbar(fr_tb)
    tree_scroll.pack(side='right', fill="y")

    tv = ttk.Treeview(fr_tb, columns=(1,2,3),yscrollcommand=tree_scroll.set)
    tv.column('#0', width=0, stretch='no')
    tv.column(1, width=50,anchor=CENTER)
    tv.column(2, width=100,anchor=CENTER)
    tv.column(3, width=200)

    tv.heading('#0', text="", anchor='center')
    tv.heading(1,text="STT")
    tv.heading(2,text="MÃ SINH VIÊN")
    tv.heading(3,text="TÊN SINH VIÊN")
    tv.pack()
    tree_scroll.config(command=tv.yview)
    tv.bind('<ButtonRelease-1>', getrow)
    tv.tag_configure("ollrow" ,background="white", font=("Baloo Tamma 2 Medium",10))
    tv.tag_configure("evenrow" ,background="#ECECEC",font=("Baloo Tamma 2 Medium",10))
    

    f1=Frame(bg,bg="white",width=140,height=140)
    f1.place(x=782,y=350)

    lb1=Label(f1,bg="white")
    lb1.pack()
    lb2=Label(f1,bg="white",font=("Baloo Tamma 2 Medium",10))
    lb2.pack()

    gan_anh("img/bg_themdl2.png")
    

    btn_xemanh=Button(f1,image=img_btnxem2,bd=0,highlightthickness=0,command=xemanh)
    btn_xemanh.pack()
    lb_loadding=Label(bg,text=" Đang tải . . . " ,font=("Baloo Tamma 2 Medium",12),bg="#FFF4FF",fg="#AD7B98")

    luong(loaddl)
    win.mainloop()

if __name__ == '__main__':
    main()