import smtplib 
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yagmail
import random
from backend.xacthuc import them_ma_xacnhan


def gmail_login(diachiemail,matkhau,quyen):
    receiver = diachiemail  # receiver email address
    
    # filename = "Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"  # attach the file
    
    # mail information
    yag = yagmail.SMTP("1911020030@stu.mku.edu.vn", "huy123@.com")
    
    # sent the mail
    body1 = """
    Xin chào,<br><br> Bạn đã là thành viên của ứng dụng điểm danh với quyền là người quản trị của khoa <br> Tải ứng dụng https://drive.google.com/drive/u/0/folders/1mbsgnZibzLQ1sk12lAT8jOJnRgrfi5J2
    <br> Đăng nhập với email: 
    """+diachiemail+"""
    <br> Mật khẩu:"""+matkhau+""" <br>Có thể đổi mật khẩu khi mở ứng dụng.
    """
    body = """
    Xin chào,<br><br> Bạn đã là thành viên của ứng dụng điểm danh với quyền là người dùng <br> Tải ứng dụng https://drive.google.com/drive/u/0/folders/1mbsgnZibzLQ1sk12lAT8jOJnRgrfi5J2
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
def gmail_doimatkhau(diachiemail,matkhaumoi):
    receiver = diachiemail  # receiver email address
    
    # filename = "Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"  # attach the file
    
    # mail information
    yag = yagmail.SMTP("1911020030@stu.mku.edu.vn", "huy123@.com")
    
    # sent the mail
    body = """
    Xin chào,<br><br> Bạn đã đổi mật khẩu trong ứng dụng điểm danh sinh viên trường Đại học Cửu Long <br> 
    <br> Đăng nhập với email: 
    """+diachiemail+"""
    <br> Mật khẩu mới:"""+matkhaumoi+""" <br>.
    """

    yag.send(
        to=receiver,
        subject="Attendance Report",  # email subject
        contents=body  # email body
        # attachments=filename,  # file attached
    )
def gui_ma_xn(diachiemail):
    receiver = diachiemail  # receiver email address
    a = random.sample(range(10), 4)
    ma=str(a[0])+str(a[1])+str(a[2])+str(a[3])
    # filename = "Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"  # attach the file
    
    # mail information
    yag = yagmail.SMTP("1911020030@stu.mku.edu.vn", "huy123@.com")
    
    # sent the mail
    body = """
    Xin chào,<br><br> Bạn đã quên mật khẩu trong ứng dụng điểm danh sinh viên trường Đại học Cửu Long <br> 
    <br> Bạn muốn lấy lại mật khẩu với email  
    """+diachiemail+"""
    <br> Mã xác nhận:"""+ma+""" <br>.
    """

    yag.send(
        to=receiver,
        subject="Attendance Report",  # email subject
        contents=body  # email body
        # attachments=filename,  # file attached
    )
    them_ma_xacnhan(receiver,ma)

def main():
    print("Đây là trang gửi email")
if __name__ == '__main__':
    main()