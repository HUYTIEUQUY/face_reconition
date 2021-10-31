import smtplib 
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# lấy thông tin cơ bản
# email = "khachuyboss@gmail.com"
# passw = "huy123@.com"

# address = 'khachuyboss@gmail.com'
# message = input('Message: ')


def gmail_login(diachiemail,matkhau,quyen):
    client = smtplib.SMTP("smtp.gmail.com",587)
    client.connect("smtp.gmail.com",587)
    client.starttls()
    client.login("1911020030@stu.mku.edu.vn","huy123@.com")
    # mail message
    msg = MIMEMultipart()
    msg['Subject'] = 'Ứng dụng điểm danh'
    msg['From'] = '1911020030@stu.mku.edu.vn'
    msg['To'] = diachiemail
    msg['Bcc'] = ''

    

    body1 = """
    Xin chào,<br><br> Bạn đã là thành viên của ứng dụng điểm danh với quyền là người quản trị của khoa <br> Tải ứng dụng https://stackoverflow.com/questions/60950088/typeerror-sequence-item-0-expected-str-instance-tuple-found .
    <br> Đăng nhập với email: 
    """+diachiemail+"""
    <br> Mật khẩu:"""+matkhau+""" <br>Có thể đổi mật khẩu khi mở ứng dụng.
    """
    body = """
    Xin chào,<br><br> Bạn đã là thành viên của ứng dụng điểm danh với quyền là người dùng <br> Tải ứng dụng https://stackoverflow.com/questions/60950088/typeerror-sequence-item-0-expected-str-instance-tuple-found .
    <br> Đăng nhập với email: 
    """+diachiemail+"""
    <br> Mật khẩu:"""+matkhau+""" <br> Có thể đổi mật khẩu khi mở ứng dụng.
    """
    if quyen == 1:
        msg.attach(MIMEText(body1,'html'))
    else:
        msg.attach(MIMEText(body,'html'))
    client.send_message(msg)
    # print("đã gửi")
    client.quit()
def main():
    print("Đây là trang gửi email")
if __name__ == '__main__':
    main()