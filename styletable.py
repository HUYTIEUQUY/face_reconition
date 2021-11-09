from tkinter import ttk




def style():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", 
    background="white",
    fg="white",
    rowheight="25",
    fieldbackground="white"
    )
    style.configure("Treeview.Heading", 
    background="#E8DFF1",
    foreground="#5F1965",
    height="10",
    font=("Baloo Tamma 2 Medium",10),
    fieldbackground="white"
    )
    style.configure("TCombobox", 
    background="white",
    foreground="back",
    height="10",
    font=("Baloo Tamma 2 Medium",11)
    )


    # Thay đổi màu đã chọn
    style.map ("Treeview", 
    background=[('selected','#5F1965')]
    )

    style.map('TCombobox', fieldbackground=[('readonly','white')])
    style.map('TCombobox', selectbackground=[('readonly', 'white')])
    style.map('TCombobox', selectforeground=[('readonly', '#5F1965')])
    

def update(tv,row):
    tv.delete(*tv.get_children())
    global dem

    dem=0
    for i in row:
        i.insert(0,dem+1)
        if dem%2==0:
            tv.insert("",index="end",iid=dem,values=i,text='',tags=('evenrow'))
        else:
            tv.insert("",index="end",iid=dem,values=i,text='',tags=('ollrow'))
        dem += 1
