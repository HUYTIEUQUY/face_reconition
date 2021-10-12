 def diemdanhra():
        dd=diemdanh.dd_sv_ra(matkb.get())
        messagebox.showwarning("thông báo","Nhấn 'Q' để thoát ")
        malop=malop_ten(data_lop.get())
        mamh=mamh_ten(data_mon.get())
        magv=ma_gv.get()
        a=ds_ma_sv(malop)
        lopp=khong_dau(data_lop.get().replace(" ","_"))
        f=open("mahoa/"+lopp+".pkl","rb")
        ref_dictt=pickle.load(f) #đọc file và luu tên theo id vào biến ref_dictt
        f.close()
        f=open("mahoa/"+lopp+"mahoa.pkl","rb")
        embed_dictt=pickle.load(f) #đọc file và luu hình ảnh đã biết được mã hoá  theo id vào biến embed_dictt
        f.close()
        known_face_encodings = []  
        known_face_names = []  
        for ref_id , embed_list in embed_dictt.items():
            for my_embed in embed_list:
                known_face_encodings +=[my_embed]
                known_face_names += [ref_id]
        try:
            webcam = cv2.VideoCapture(1)
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
        except:webcam = cv2.VideoCapture(0)
        face_locations = []
        face_encodings = []
        face_names     = []
        process_this_frame = True #xử lý khung
        # ret = video_capture.set(cv2.CAP_PROP_FRAME_WIDTH,600)
        # ret = video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        #these landmarks are based on the image above 
        left_eye_landmarks  = [36, 37, 38, 39, 40, 41]
        right_eye_landmarks = [42, 43, 44, 45, 46, 47]
        try:
            while True  :
                
                ret, frame = webcam.read()
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1] # Chuyển đổi hình ảnh từ màu BGR (OpenCV sử dụng) sang màu RGB (face_recognition sử dụng)
                gray=cv2.cvtColor(small_frame,cv2.COLOR_BGR2GRAY)
                faces,_,_ = detector.run(image = gray, upsample_num_times = 0, adjust_threshold = 0.0)
                
                if process_this_frame:
                    face_locations = face_recognition.face_locations(rgb_small_frame)# tìm tất cả khuôn mặt trong khung hình hiện tại vủa video
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #mã hoá khuôn mặt hiện tại trong khung hình của video
                    face_names = []
                    for face_encoding in face_encodings:
                        # Xem khuôn mặt có khớt cới các khuôn mặt đã biết không
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,0.4)
                        name = "Khongbiet"
                        #Đưa ra các khoảng cách giữa các khuôn mặt và khuôn mặt đã biết
                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances) #Cái nào gần hơn thì lưu vào biến best_match_index
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                        face_names.append(name)
                        now = datetime.now()
                        now=now.strftime("%X")
                       
                        
                        for face in faces:
                            try:
                                landmarks = predictor(rgb_small_frame, face)
                                left_eye_ratio  = eye.get_blink_ratio(left_eye_landmarks, landmarks)
                                right_eye_ratio = eye.get_blink_ratio(right_eye_landmarks, landmarks)
                                blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2
                            except: blink_ratio=0

                            if blink_ratio > 4.7:
                                threading.Thread(target=diemdanh.capnhat_tgra,args=(matkb.get(),name,now)).start()
                                threading.Thread(target=gananh_khi_click,args=(name,now)).start()

                process_this_frame = not process_this_frame
                #Hiển thị kết quả
                try:
                    for (top_s, right, bottom, left), name in zip(face_locations, face_names):
                        top_s *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4

                        font = cv2.FONT_HERSHEY_SIMPLEX
                        if name == "Khongbiet":
                            cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 0,255), 2)
                            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0,255), cv2.FILLED)
                            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                        elif name in dd:
                            cv2.rectangle(frame, (left, top_s), (right, bottom), (255, 0,0), 2)
                            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255,0, 0), cv2.FILLED)
                            cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)
                        else:
                            cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 255,0), 2)
                            
                except:print("no name")
                cv2.imshow('Video', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    webcam.release()
                    tudong.set(str(0))
                    lb2.config(text="")
                    lb1.config(img=ing_btntam)
                    cv2.destroyAllWindows()
                    break
        except:print("có lỗi")
    #     #----------------------------------------------------------------------------
        dd=diemdanh.sv_da_dd(matkb.get())
        now=""
        for i in range(0,len(a)):
            if a[i] not in dd :
                threading.Thread(target=diemdanh.diem_danh_vao_csdl,args=(matkb.get(),a[i],"vắng",malop,mamh,magv,ngay,ca,now)).start()
        diemdanh.update_TT_diemdanh(matkb.get())