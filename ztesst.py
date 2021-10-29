import cv2
import face_recognition
import numpy as np
import pickle

f=open("mahoa/Cong_nghe_thong_tin_K19_.pkl","rb")
ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
f.close()
g=open("mahoa/Cong_nghe_thong_tin_K19_mahoa.pkl","rb")
embed_dictt=pickle.load(g) #đọc file và luu hình ảnh đã biết được mã hoá  theo id vào biến embed_dictt
g.close()

known_face_encodings = []  
known_face_names = []  
for ref_id , embed_list in embed_dictt.items():
    for my_embed in embed_list:
        known_face_encodings +=[my_embed]
        known_face_names += [ref_id]


webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()

face_locations = []
face_encodings = []

process_this_frame = True #xử lý khung
# ret = webcam.set(cv2.CAP_PROP_FRAME_WIDTH,600)
# ret = webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# #these landmarks are based on the image above 
# left_eye_landmarks  = [36, 37, 38, 39, 40, 41]
# right_eye_landmarks = [42, 43, 44, 45, 46, 47]
while True  :                
    ret, frame = webcam.read()
    
    # # print(frame)
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
    # gray=cv2.cvtColor(small_frame,cv2.COLOR_BGR2GRAY)
    # faces,_,_ = detector.run(image = gray, upsample_num_times = 0, adjust_threshold = 0.0)
    
    if process_this_frame:
        face_names = []
        face_locations = face_recognition.face_locations(rgb_small_frame)# tìm tất cả khuôn mặt trong khung hình hiện tại vủa video

        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #mã hoá khuôn mặt hiện tại trong khung hình của video
        for face_encoding in face_encodings:
            # Xem khuôn mặt có khớt cới các khuôn mặt đã biết không
            try:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.6)
                print(matches)
            except:print("lỗi")
            name = "Unknow"
            #Đưa ra các khoảng cách giữa các khuôn mặt và khuôn mặt đã biết
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances) #Cái nào gần hơn thì lưu vào biến best_match_index

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            # if vao_ra==0:
            #     xulyvao(ma,name)
            # else: 
            #     xulyra(ma,name)
            
            
    process_this_frame = not process_this_frame
    #Hiển thị kết quả
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
        cv2.destroyAllWindows()