from tkinter import *
from tkinter import Scrollbar, ttk

from PIL.Image import fromqimage

root = Tk()
root.geometry("1000x500")

style = ttk.Style()
style.theme_use('xpnative')
style.configure("Treeview", 
background="white",
fg="white",
rowheight="25",
fieldbackground="white"
)

# Thay đổi màu đã chọn
style.map("Treeview", 
background=[('selected','#5F1965')]
)


# tạo frame cho treeview
f = Frame(root)
f.pack(pady=10)

#tạo thanh cuộn 
tree_scroll = Scrollbar(f)
tree_scroll.pack(side='right', fill="y")

#tạo một bảng
tree = ttk.Treeview(f,yscrollcommand=tree_scroll.set)
tree.pack()

#Cấu hình thanh cuộn
tree_scroll.config(command=tree.yview)

# tạo cột
tree['columns']=('STT', 'Mã sinh viên', 'Tên sinh viên','Thông tin','Thời gian vào', 'Thời gian ra','Ghi chú')

# định dạng cột
tree.column('#0', width=0, stretch='no')
tree.column('STT', width=50, anchor='center')
tree.column('Mã sinh viên', width=100, anchor='center')
tree.column('Tên sinh viên', width=100)
tree.column('Thông tin', width=100)
tree.column('Thời gian vào', width=100)
tree.column('Thời gian ra', width=100)
tree.column('Ghi chú', width=100)

tree.heading('#0', text="", anchor='center')
tree.heading('STT', text="STT", anchor='center')
tree.heading('Mã sinh viên', text="MÃ SINH VIÊN", anchor='center')
tree.heading('Tên sinh viên', text="TÊN SINH VIÊN", anchor='center')
tree.heading('Thông tin', text="THÔNG TIN", anchor='center')
tree.heading('Thời gian vào', text="THỜI GIAN VÀO", anchor='center')
tree.heading('Thời gian ra', text="THỜI GIAN RA", anchor='center')
tree.heading('Ghi chú', text="GHI CHÚ", anchor='center')

data=[
    ["1","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["2","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["3","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["4","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["5","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["6","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["7","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["8","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["9","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["10","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
    ["11","1111","Nguyễn Khắc Huy","Có","11:00:00","12:00:00",""],
]

tree.tag_configure("ollrow" ,background="white")
tree.tag_configure("evenrow" ,background="#FEF7F3")


global dem
dem=0
for i in data:
    if dem%2==0:
        tree.insert("",index="end",iid=dem,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),text='',tags=('evenrow'))
    else:
        tree.insert("",index="end",iid=dem,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),text='',tags=('ollrow'))
    dem += 1

print(style.theme_names())
root.mainloop()

