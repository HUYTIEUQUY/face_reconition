# from tkinter import *
# from tkinter import ttk
# from tkinter import PhotoImage
# from tkinter.ttk import Combobox
# from PIL import ImageTk
# import csdl
# from tkinter import messagebox
# import dangnhap
# import socket
# import numpy as np
# import pickle
# import cv2
# import face_recognition
# import sinhvien
# import diemdanh
# import taikhoan
# import thongke


# def main():
#     def trolai():
#         win.destroy()
#         diemdanh.main()
#     def diemdanh():
#         messagebox.showwarning("thông báo","Nhấn 'q' để thoát ")
#         malop=csdl.tenlop_thanh_ma(datalop.get())
#         a=csdl.lay_id_theo_lop(malop)#------------------lấy id theo lop
#         lopp=str(datalop.get()).replace(" ","_")
#         f=open("mahoa/"+lopp+".pkl","rb")
#         ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
#         f.close()
#         f=open("mahoa/"+lopp+"mahoa.pkl","rb")
#         embed_dictt=pickle.load(f) #đọc file và luu hình ảnh đã biết được mã hoá  theo id vào biến embed_dictt
#         f.close()

#         known_face_encodings = []  
#         known_face_names = []  

#         for ref_id , embed_list in embed_dictt.items():
#             for my_embed in embed_list:
#                 known_face_encodings +=[my_embed]
#                 known_face_names += [ref_id]

#         video_capture  = cv2.VideoCapture(0)
#         face_locations = []
#         face_encodings = []
#         face_names     = []
#         diemdanh       =[]
#         process_this_frame = True #xử lý khung
#         while True  :
        
#             ret, frame = video_capture.read()
#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#             rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
#             if process_this_frame:
#                 face_locations = face_recognition.face_locations(rgb_small_frame)# tìm tất cả khuôn mặt trong khung hình hiện tại vủa video
#                 face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #mã hoá khuôn mặt hiện tại trong khung hình của video
#                 face_names = []
#                 for face_encoding in face_encodings:
#                     # Xem khuôn mặt có khớt cới các khuôn mặt đã biết không
#                     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                     name = "Unknown"
#                     #Đưa ra các khoảng cách giữa các khuôn mặt và khuôn mặt đã biết
#                     face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances) #Cái nào gần hơn thì lưu vào biến best_match_index
#                     if matches[best_match_index]:
#                         name = known_face_names[best_match_index]
                        
#                     face_names.append(name)
#                     if name not in diemdanh:
#                         # speak(ref_dictt[name]+" đã điểm danh")
#                         diemdanh.append(name)
#             process_this_frame = not process_this_frame
            

#             #Hiển thị kết quả
#             for (top_s, right, bottom, left), name in zip(face_locations, face_names):
#                 top_s *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4
#                 cv2.rectangle(frame, (left, top_s), (right, bottom), (255,0, 0), 2)
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255,0, 0), cv2.FILLED)
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 if name == "Unknown":
#                     cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 0,255), 2)
#                     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0,255), cv2.FILLED)
#                     cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
#                 else:
#                     cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)
                
#             cv2.imshow('Video', frame)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         video_capture.release()
#         cv2.destroyAllWindows()

#         #----------------------------------------------------------------------------
#         malop=csdl.tenlop_thanh_ma(datalop.get())
#         mamh=csdl.tenmon_thanh_ma(datamon.get())
#         magv=csdl.tim_magv_tu_email()
#         ca=dataca.get()
#         ngay=datangay.get()
#         csdl.diem_danh_vao_csdl(a,diemdanh,malop,mamh,magv,ca,ngay)
#         csdl.update_TT_diemdanh(malop,mamh,magv,ngay)
#         row=csdl.diemdanhbu(magv)
#         update(row)
#         anhnen=bg.create_image(500,300,image=img_bg1)
#         btndiemdanh.destroy()
#         f1.config(width=410)
#         f4.config(width=410)
#         tv.config(column=(1,2))
#         tv.column(1, width=300 )
#         tv.column(2, width=300 )
#         f5=Frame(bg,width=5,height=230 ,bg="white")
#         f5.place(x=718,y=90)
#         row=csdl.bangdiemdanh(malop,mamh,ca,ngay)
#         update(row)
#         btndiemdanhlai=Button(bg,image=ing_btndiemdanhlai,bd=0,highlightthickness=0,command=diemdanh)
#         btndiemdanhlai.place(x=594,y=533)
# #___________________________________________________________________________________________
#     def getrow(event):
#         rowid=tv.identify_row(event.y)
#         item=tv.item(tv.focus())
#         datangay.set(item['values'][0])
#         datalop.set(item['values'][1])
#         datamon.set(item['values'][2])
#         dataca.set(item['values'][3])
#     def update(row):
#         tv.delete(*tv.get_children())
#         for i in row:
#             tv.insert('','end',values=i)
#     def menuthongke():
#         win.destroy()
#         thongke.main()

#     def menutaikhoan():
#         win.destroy()
#         taikhoan.main()

#     def menudiemdanh():
#         win.destroy()
#         diemdanhsv.main()

#     def menuthemsv():
#         win.destroy()
#         them_sv_moi.main()
#     def dangxuat():
#         ten_thiet_bi = socket.gethostname()
#         file=open(ten_thiet_bi+".txt","w")
#         file.write("")
#         file.close()
#         win.destroy()
#         dangnhap.main()

#     win=Tk()
#     win.geometry("1000x600+300+120")
#     win.resizable(False,False)
#     win.config(bg="green")
#     win.title("Menu tkinter")
#     img_bg=ImageTk.PhotoImage(file="img/bg_diemdanhbu.png")
#     img_bg1=ImageTk.PhotoImage(file="img/danhsachdiemdanh.png")
    
#     ing_menuthem=ImageTk.PhotoImage(file="img/menuthemdl1.png")
#     ing_menudiemdanh=ImageTk.PhotoImage(file="img/menudiemdanh1.png")
#     ing_menutaikhoan=ImageTk.PhotoImage(file="img/menutaikhoan.png")
#     ing_menuthongke=ImageTk.PhotoImage(file="img/menuthongke.png")
#     ing_btndangxuat=ImageTk.PhotoImage(file="img/btndangxuat.png")
#     ing_btndiemdanh1=ImageTk.PhotoImage(file="img/btndiemdanh1.png")
#     ing_btndiemdanhlai=ImageTk.PhotoImage(file="img/btndiemdanhlai.png")
#     ing_btntrolai=ImageTk.PhotoImage(file="img/btn_trolai.png")


#     #-----------------------------------------------------------------------------
#     datalop=StringVar()
#     datamon=StringVar()
#     datangay=StringVar()
#     dataca=StringVar()
#     #----------------------------------------------------------------------------

#     bg=Canvas(win,width=1000,height=600,bg="green")
#     bg.pack(side="left",padx=0)
#     anhnen=bg.create_image(500,300,image=img_bg)
#     magv=csdl.tim_magv_tu_email()

#     menuthem=Button(bg,image=ing_menuthem,bd=0,highlightthickness=0,command=menuthemsv)
#     menuthem.place(x=46,y=129)

#     menudiemdanh=Button(bg,image=ing_menudiemdanh,bd=0,highlightthickness=0,command=menudiemdanh)
#     menudiemdanh.place(x=46,y=248)

#     menuthongke=Button(bg,image=ing_menuthongke,bd=0,highlightthickness=0,command=menuthongke)
#     menuthongke.place(x=46,y=366)

#     menutaikhoan=Button(bg,image=ing_menutaikhoan,bd=0,highlightthickness=0,command=menutaikhoan)
#     menutaikhoan.place(x=46,y=484)

#     btndangxuat=Button(bg,image=ing_btndangxuat,bd=0,highlightthickness=0,command=dangxuat)
#     btndangxuat.place(x=248,y=44)

#     tengv=csdl.tim_tengv_tu_email()
#     Label(bg,text=tengv,font=("Baloo Tamma",14),fg="#A672BB",bg="white").place(x=45,y=40)

#     f=Frame(bg,width=670,height=130,bg="red")
#     f.place(x=320,y=90)

#     row=csdl.diemdanhbu(magv)
#     tv = ttk.Treeview(f, columns=(1,2,3,4), show="headings")
#     tv.column(1, width=130 )
#     tv.column(2, width=240 )
#     tv.column(3, width=240)
#     tv.column(4, width=50)
#     tv.pack()
#     update(row)
#     f1=Frame(bg,width=664,height=22,bg="white")
#     f1.place(x=320,y=90)
#     f2=Frame(bg,width=2,height=230, bg="white")
#     f2.place(x=320,y=90)
#     f3=Frame(bg,width=2,height=230, bg="white")
#     f3.place(x=981,y=90)
#     f4=Frame(bg,width=664,bg="white")
#     f4.place(x=320,y=316)
    
#     btndiemdanh=Button(bg,image=ing_btndiemdanh1,bd=0,highlightthickness=0,command=diemdanh)
#     btndiemdanh.place(x=594,y=533)
#     tv.bind('<Double 1>', getrow)
    
#     Label(bg,textvariable=datangay,font=("Baloo Tamma",12),bg="white").place(x=860,y=390)
#     Label(bg,textvariable=datalop,font=("Baloo Tamma",12),bg="white").place(x=460,y=390)
#     Label(bg,textvariable=datamon,font=("Baloo Tamma",12),bg="white").place(x=480,y=470)
#     Label(bg,textvariable=dataca,font=("Baloo Tamma",12),bg="white").place(x=840,y=470)

#     btntrolai=Button(bg,image=ing_btntrolai,bd=0,highlightthickness=0,command=trolai)
#     btntrolai.place(x=950,y=1)


#     win.mainloop()

# if __name__ == '__main__':
#     main()