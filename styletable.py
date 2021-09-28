from tkinter import ttk




def style():
    style = ttk.Style()
    # style.theme_use('xpnative')
    style.configure("Treeview", 
    background="white",
    fg="white",
    rowheight="25",
    fieldbackground="white"
    )

    # Thay đổi màu đã chọn
    style.map ("Treeview", 
    background=[('selected','#5F1965')]
    )
    

def update(tv,row):
    tv.delete(*tv.get_children())
    global dem
    dem=0
    for i in row:
        if dem%2==0:
            tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
        else:
            tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
        dem += 1
