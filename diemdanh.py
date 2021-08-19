from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import Combobox
from PIL import ImageTk
# import csdl
from tkinter import messagebox
import dangnhap
import socket
import pickle
import cv2
import face_recognition
# import them_sv_moi
# import thongke
# import taikhoan
# import diemdanhbu
# import wikipedia
# from gtts import gTTS
# import playsound
# from webdriver_manager . chrome import ChromeDriverManager
# import os
import numpy as np
from tkinter import ttk
from datetime import datetime
import re


def main():
    # wikipedia.set_lang('vi')
    # language ='vi'
    # path = ChromeDriverManager().install()

    # def speak(text):
    #     tts = gTTS(text=text,lang=language,slow=False)
    #     tts.save("sound.mp3")
    #     playsound.playsound("sound.mp3", True)
    #     os.remove("sound.mp3")
    # def khong_dau(s):
    #     s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    #     s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    #     s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    #     s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    #     s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    #     s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    #     s = re.sub(r'[ìíịỉĩ]', 'i', s)
    #     s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    #     s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    #     s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    #     s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    #     s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    #     s = re.sub(r'[Đ]', 'D', s)
    #     s = re.sub(r'[đ]', 'd', s)
    #     return s
    # def diemdanhbulai():
    #     win.destroy()
    #     diemdanhbu.main()
    # def diemdanhlai():
    #     csdl.xoadiemdanh(malop,mamh,ma_gv,ca)
    #     batdaudiemdanh()
    # def update(row):
    #     tv.delete(*tv.get_children())
    #     for i in row:
    #         tv.insert('','end',values=i)
    # def doigiay(s):
    #     h=str(s)[0:1]
    #     p=str(s)[2:4]
    #     s=str(s)[5:7]
    #     giay=int(h)*60*60+int(p)*60+int(s)
    #     return giay
    # def batdaudiemdanh():

    #     messagebox.showwarning("thông báo","Nhấn 'q' để thoát ")
    #     tgbd= datetime.now()
    #     malop=csdl.tenlop_thanh_ma(data_lop)
    #     mamh=csdl.tenmon_thanh_ma(data_mon)
    #     magv=csdl.tim_magv_tu_email()
    #     ca=csdl.cahoc()
    #     ngay=csdl.ngay()
        
    #     a=csdl.lay_id_theo_lop(malop)#------------------lấy id theo lop

    #     lopp=khong_dau(data_lop.replace(" ","_"))
       
    #     f=open("mahoa/"+lopp+".pkl","rb")
    #     ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
    #     f.close()
    #     f=open("mahoa/"+lopp+"mahoa.pkl","rb")
    #     embed_dictt=pickle.load(f) #đọc file và luu hình ảnh đã biết được mã hoá  theo id vào biến embed_dictt
    #     f.close()

    #     known_face_encodings = []  
    #     known_face_names = []  

    #     for ref_id , embed_list in embed_dictt.items():
    #         for my_embed in embed_list:
    #             known_face_encodings +=[my_embed]
    #             known_face_names += [ref_id]

    #     video_capture  = cv2.VideoCapture(0)
    #     face_locations = []
    #     face_encodings = []
    #     face_names     = []
    #     diemdanh       =[]
    #     process_this_frame = True #xử lý khung
    #     while True  :
        
    #         ret, frame = video_capture.read()
    #         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    #         rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
    #         if process_this_frame:
    #             face_locations = face_recognition.face_locations(rgb_small_frame)# tìm tất cả khuôn mặt trong khung hình hiện tại vủa video
    #             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #mã hoá khuôn mặt hiện tại trong khung hình của video
    #             face_names = []
    #             for face_encoding in face_encodings:
    #                 # Xem khuôn mặt có khớt cới các khuôn mặt đã biết không
    #                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    #                 name = "Khongbiet"
    #                 #Đưa ra các khoảng cách giữa các khuôn mặt và khuôn mặt đã biết
    #                 face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    #                 best_match_index = np.argmin(face_distances) #Cái nào gần hơn thì lưu vào biến best_match_index
    #                 if matches[best_match_index]:
    #                     name = known_face_names[best_match_index]
                        
    #                 face_names.append(name)
    #                 now = datetime.now()
    #                 kq=now-tgbd
    #                 s=doigiay(kq)
                    
    #                 if name not in diemdanh and s>=60:
                        
    #                     tre="Trể "+str(kq)[0:7]
    #                     csdl.diem_danh_vao_csdl(name,tre,malop,mamh,magv,ca,ngay)
    #                     diemdanh.append(name)
    #                 elif name not in diemdanh :
    #                     print("đúng giờ")
    #                     print(diemdanh)
    #                     csdl.diem_danh_vao_csdl(name,"có",malop,mamh,magv,ca,ngay)
    #                     diemdanh.append(name)
                        
    #         process_this_frame = not process_this_frame
            

    #         #Hiển thị kết quả
    #         for (top_s, right, bottom, left), name in zip(face_locations, face_names):
    #             top_s *= 4
    #             right *= 4
    #             bottom *= 4
    #             left *= 4
    #             cv2.rectangle(frame, (left, top_s), (right, bottom), (255,0, 0), 2)
    #             cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255,0, 0), cv2.FILLED)
    #             font = cv2.FONT_HERSHEY_SIMPLEX
    #             if name == "Unknown":
    #                 cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 0,255), 2)
    #                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0,255), cv2.FILLED)
    #                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
    #             else:
    #                 cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)
                
    #         cv2.imshow('Video', frame)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #     video_capture.release()
    #     cv2.destroyAllWindows()
        
    #     #----------------------------------------------------------------------------
    #     for i in range(0,len(a)):
    #         if a[i] not in diemdanh:
    #             csdl.diem_danh_vao_csdl(a[i],"không",malop,mamh,magv,ca,ngay)
        
    #     csdl.update_TT_diemdanh(malop,mamh,magv,ngay)
        
    #     row=csdl.bangdiemdanh(malop,mamh,ca,ngay)
    #     update(row)

    # #---------------------------------------------
    # def kt ():
    #     mlop=csdl.tenlop_thanh_ma(data_lop)
    #     mmh=csdl.tenmon_thanh_ma(data_mon)
    #     mgv=csdl.tim_magv_tu_email()
        
    #     if data_lop == "Bạn không có tiết dạy !":
    #         messagebox.showwarning("thông báo","Bạn không có tiết dạy")
    #     elif csdl.kt_dd(mlop,mmh,mgv) == "chưa":
    #         batdaudiemdanh()
    #     else:
    #         messagebox.showwarning("thông báo","Đã điểm danh rồi !")
    # def menutaikhoan():
    #     win.destroy()
    #     taikhoan.main()

    # def menuthongke():
    #     win.destroy()
    #     thongke.main()

    # def menuthemsv():
    #     win.destroy()
    #     them_sv_moi.main()

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
    img_bg=ImageTk.PhotoImage(file="img/bg_diemdanh.png")
    
    ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
    ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh1.png")
    ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
    ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
    ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
    ing_btndiemdanh=ImageTk.PhotoImage(file="img/btndiemdanh.png")
    ing_btndiemdanhlai=ImageTk.PhotoImage(file="img/btndiemdanhlai.png")
    ing_btnthongbao=ImageTk.PhotoImage(file="img/btnthongbaodd.png")
    
    bg=Canvas(win,width=1000,height=600,bg="green")
    bg.pack(side="left",padx=0)
    anhnen=bg.create_image(500,300,image=img_bg)

    # menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,command=menuthemsv)
    # menuthem.place(x=46,y=129)

    # menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0)
    # menudiemdanh.place(x=46,y=248)

    # menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0, command=menuthongke)
    # menuthongke.place(x=46,y=366)

    # menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0, command=menutaikhoan)
    # menutaikhoan.place(x=46,y=484)

    # btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
    # btndangxuat.place(x=248,y=44)

    # tengv=csdl.tim_tengv_tu_email()
    # Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

    # #dữ liệu hiện lớp, môn
    # ten_thiet_bi = socket.gethostname()
    # d=[]
    # with open(ten_thiet_bi+".txt","r") as file:
    #     d=file.read().split()
    # makhoa=csdl.makhoa_tu_email(d[0])
    # ma_gv=csdl.tim_magv_tu_email()
    # ca=csdl.cahoc()
    # if(csdl.hien_lop_theo_tkb(ma_gv,ca) == []):
    #     data_lop="Bạn không có tiết dạy !"
    # else:
    #     data_lop = csdl.hien_lop_theo_tkb(ma_gv,ca)
    # #lớp
    # Label(bg,text=data_lop,font=("Baloo Tamma",12),bg="white").place(x=600,y=90)
    
    # #dieduf kiện hiện môn
    # if csdl.hien_mon_theo_tkb(ma_gv,ca) == []:
    #     data_mon="Bạn không có tiết dạy !"
    # else:
    #     data_mon=csdl.hien_mon_theo_tkb(ma_gv,ca)
    #     #môn
    # Label(bg,text=data_mon,font=("Baloo Tamma",12),bg="white").place(x=600,y=125)

    # #nút điểm diemdanh
    # btndiemdanh=Button(bg,image=ing_btndiemdanh,bd=0,highlightthickness=0,command=kt)
    # btndiemdanh.place(x=575,y=229)

    # #bang diemdanh
    # ngay=csdl.ngay()
    # malop=csdl.tenlop_thanh_ma(data_lop)
    # mamh=csdl.tenmon_thanh_ma(data_mon)
    # try:
    #     row=csdl.bangdiemdanh(malop,mamh,ca,ngay)
    # except:
    #     row=[]
   
   
    # tv = ttk.Treeview(bg, columns=(1,2,3,4,5), show="headings")
    # tv.column(1, width=180 )
    # tv.column(2, width=80,anchor=CENTER)
    # tv.column(3, width=80,anchor=CENTER)
    # tv.column(4, width=80,anchor=CENTER)
    # tv.column(5, width=180)
    # tv.heading(1,text="Sinh viên")
    # tv.heading(2,text="Thông tin")
    # tv.heading(3,text="Thời gian vào")
    # tv.heading(4,text="Thời gian ra")
    # tv.heading(5,text="Ghi chú")

    # tv.place(x=380,y=350)
    
    
    # update(row)

    # #nút  diemdanhlai
    # btndiemdanhlai=Button(bg,image=ing_btndiemdanhlai,bd=0,highlightthickness=0,command=diemdanhlai)
    # btndiemdanhlai.place(x=757,y=530)
    # #nút thông báo
    # l=[]
    # i=[]
    # magv=csdl.tim_magv_tu_email()
    # if csdl.gvdiemdanh(magv,l,i,i,i)== True:
    #     btnthongbao=Button(bg,image=ing_btnthongbao,bd=0,highlightthickness=0,command=diemdanhbulai)
    #     btnthongbao.place(x=943,y=0)
    #     lbstb1=Label(bg,text=len(l),fg="red",font=("Arial",10),bg="white")
    #     lbstb1.place(x=978,y=2)
    win.mainloop()

if __name__ == '__main__':
    main()