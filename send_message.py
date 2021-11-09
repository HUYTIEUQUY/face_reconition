import smtplib 
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yagmail


def gmail_login(diachiemail,matkhau,quyen):
    receiver = diachiemail  # receiver email address
    
    # filename = "Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"  # attach the file
    
    # mail information
    yag = yagmail.SMTP("1911020030@stu.mku.edu.vn", "huy123@.com")
    
    # sent the mail
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
        content=body1
    else:
        content=body
    yag.send(
        to=receiver,
        subject="Attendance Report",  # email subject
        contents=content  # email body
        # attachments=filename,  # file attached
    )

def main():
    print("Đây là trang gửi email")
if __name__ == '__main__':
    main()