from tkinter import *
from tkinter import ttk
import mysql.connector
import os

z=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='jo7812002',
    )
a=z.cursor()
a.execute("use passmanager")

root=Tk()
root.title('Dashboard')
root.geometry('925x500+300+200')
root.resizable(False,False)
#---------------------------------------------------FRAMES-----------------------------------------------------------------------------------------------------------------------------
header_frame = Frame(root,background="#ADEFD1",height=70, width=1100)
header_frame.pack()
header_frame.pack_propagate(0)

body_frame = Frame(root,background="#ADEFD1",height=300, width=1100)
body_frame.pack()
header_frame.pack_propagate(0)
##00EBBF
footer_frame = Frame(root,background="#ADEFD1",height=300, width=1100)
footer_frame.pack()
header_frame.pack_propagate(0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login():
    root.destroy()
    os.system('python login.py')
def home():
    #------------header file ------------------------

    Label(header_frame,text="Hello , vickyd",font=("monotype corsiva",30),bg="#ADEFD1").place(x=20,y=10)
    #Label(header_frame,text="dei parama padi da",font=("monotype corsiva",30),bg="pink").place(x=550,y=10)
    Button(header_frame,width=8,text="Logout",bg='#00203F',fg='white',font=("monotype corsiva",16),border=0,command=login).place(x=800,y=15)

    #--------------------Body content---------------------------------
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    tv = ttk.Treeview(body_frame, show='headings', height=12,style="mystyle.Treeview")
    tv.pack(side=LEFT)

    tv['columns'] = ('S.No', 'Website', 'Username', 'Password')
    tv.column('S.No', anchor='w', width=50)
    tv.column('Website', anchor='center', width=300)
    tv.column('Username', anchor='center', width=250)
    tv.column('Password', anchor='center', width=300)

    tv.heading('#0', text='Label', anchor='w')
    tv.heading('S.No', text='S.No', anchor='w')
    tv.heading('Website', text='Website', anchor='center')
    tv.heading('Username', text='Username', anchor='center')
    tv.heading('Password', text='Password', anchor='center')

    '''
    a.execute("SELECT * FROM vickyd")
    res=a.fetchall()
    for i in range(len(res)):
        print(res[i])
    '''
    
    tv.insert(parent='', index=0, iid=0, values=(1,"instagram", "damvicky.13",'vd@1234'))
    tv.insert(parent='', index=1, iid=1, values=(2,"gmail", "damvicky.13@gmail.com",'vicky@1234'))
    tv.insert(parent='', index=2, iid=2, values=(3,"discord", "vignesh#4003",'vicky@1234'))
    tv.insert(parent='', index=3, iid=3, values=(4,"netflix", "vignesh",'nopassword'))
    tv.insert(parent='', index=4, iid=4, values=(5,"hotstar", "6380484345",'khatija'))
    tv.insert(parent='', index=5, iid=5, values=(6,"instagram", "damvicky.13",'vd@1234'))
    tv.insert(parent='', index=6, iid=6, values=(7,"gmail", "damvicky.13@gmail.com",'vicky@1234'))
    tv.insert(parent='', index=7, iid=7, values=(8,"discord", "vignesh#4003",'vicky@1234'))
    tv.insert(parent='', index=8, iid=8, values=(9,"netflix", "vignesh",'nopassword'))
    tv.insert(parent='', index=9, iid=9, values=(10,"hotstar", "6380484345",'khatija'))
    tv.insert(parent='', index=10, iid=10, values=(11,"instagram", "damvicky.13",'vd@1234'))
    tv.insert(parent='', index=11, iid=11, values=(12,"gmail", "damvicky.13@gmail.com",'vicky@1234'))
    tv.insert(parent='', index=12, iid=12, values=(13,"discord", "vignesh#4003",'vicky@1234'))
    tv.insert(parent='', index=13, iid=13, values=(14,"netflix", "vignesh",'nopassword'))
    tv.insert(parent='', index=14, iid=14, values=(15,"hotstar", "6380484345",'khatija'))
    tv.insert(parent='', index=15, iid=15, values=(16,"instagram", "damvicky.13",'vd@1234'))
    tv.insert(parent='', index=16, iid=16, values=(17,"gmail", "damvicky.13@gmail.com",'vicky@1234'))
    tv.insert(parent='', index=17, iid=17, values=(18,"discord", "vignesh#4003",'vicky@1234'))
    tv.insert(parent='', index=18, iid=18, values=(19,"netflix", "vignesh",'nopassword'))
    tv.insert(parent='', index=19, iid=19, values=(20,"hotstar", "6380484345",'khatija'))

    sb = Scrollbar(body_frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    tv.config(yscrollcommand=sb.set)
    sb.config(command=tv.yview)

    #-----------footer----------------------------------
    Label(footer_frame,text="Website",font=("monotype corsiva",14),bg="#ADEFD1").place(x=215,y=20)
    Label(footer_frame,text="Username",font=("monotype corsiva",14),bg="#ADEFD1").place(x=395,y=20)
    Label(footer_frame,text="Password",font=("monotype corsiva",14),bg="#ADEFD1").place(x=575,y=20)
    web=Entry(footer_frame,width=20,border=0,bg="white",font=('microsoft YaHei UI Light',12))
    web.place(x=155,y=50)
    usn=Entry(footer_frame,width=20,border=0,bg="white",font=('microsoft YaHei UI Light',12))
    usn.place(x=340,y=50)
    pswd=Entry(footer_frame,width=20,border=0,bg="white",font=('microsoft YaHei UI Light',12))
    pswd.place(x=525,y=50)

    Button(footer_frame,text=" Add/Update ",bg='#00203F',fg='white',font=("monotype corsiva",13),border=0).place(x=720,y=45)
    Button(footer_frame,text=" Delete All ",bg='red',fg='white',font=("monotype corsiva",13),border=0).place(x=100,y=105)
    Button(footer_frame,text="Delete ",bg='#00203F',fg='white',font=("monotype corsiva",13),border=0).place(x=30,y=105)
    Button(footer_frame,text=" Show Password ",bg='#00203F',fg='white',font=("monotype corsiva",13),border=0).place(x=780,y=105)
    
home()
root.mainloop()
