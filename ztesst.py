import cv2
import face_recognition
from tkinter import messagebox
from PIL import Image
from numpy import asarray

anh=""

key = cv2. waitKey(1)
camera=[]
for i in range(0, 2):
    cap = cv2.VideoCapture(i+cv2.CAP_DSHOW)
    test, frame = cap.read()
    if test==True: 
        camera.append(i)
if camera != []:
    webcam = cv2.VideoCapture(max(camera)+cv2.CAP_DSHOW)
    
id=112
a=0
process_this_frame = True
while True:
    
    check, frame = webcam.read()
    
    # Thay đổi kích thước trong opencv
    #frame: màn hình là hình ảnh đầu vào
    #(0, 0), fx=0.25, fy=0.25 : kích thước mong muốn cho hình ảnh đầuq
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
    
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        
        if cv2.waitKey(1) == ord('s') : 

            if face_locations != [] and len(face_locations)==1: #nếu có khuôn mặt
                cv2.imwrite('img_anhsv/'+str(id)+str(a+1)+'.png',frame)
                top, right, bottom, left=face_locations[0]
                gbr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                gbr_array = asarray(gbr)
                face = gbr_array[top:bottom, left:right]
                face = Image.fromarray(face)                       
                face = face.resize((160,160))
                face = asarray(face)
                cv2.imwrite('img_anhsv/'+str(id)+str(a+1)+'.png',face)
                face_encoding = face_recognition.face_encodings(face) #mã hoá và lưu vào biến face_encoding
                # print(face_encoding)
                # anh=anh+' '+str(id)+str(a+1)+'.png'
                # if id in embed_dictt: #Nếu id đã tồn tại thì cộng thêm hình ảnh đã mã hoá vào
                #     embed_dictt[id]+=[face_encoding]
                # else:#Nếu chưa tồn tại thì khởi tạo với "id"="dữ liệu hình ảnh mã hoá"
                #     embed_dictt[id]=[face_encoding]
                
                a=a+1
                if(a==5):
                    messagebox.showinfo("thông báo", "Đã lưu")
                    print("thoát")
                    break
    process_this_frame= not process_this_frame
    for top_s, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 255,0), 2)
    
    cv2.imshow("Capturing", frame)
    if cv2.waitKey(1) == ord('q') :
        print("thoát")
        break
        

webcam.release()
cv2.destroyAllWindows()