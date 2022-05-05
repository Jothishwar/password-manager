from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
'''import mysql.connector
z=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='jo7812002',
    )
a=z.cursor()
try:
    a.execute("CREATE DATABASE passmanager")
    a.execute("use passmanager")
    a.execute("create table users(email varchar(60),username varchar(30) primary key,passwd varchar(32))")
    print("table created")
except:
    a.execute("use passmanager")
    print("table used") '''
#---------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.title('Password Manager')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
def signup():
    username=user.get()
    password=code.get()
    mail=email.get()

    if username=='admin' and password=='1234':
        user.delete(0, 'end')
        code.delete(0, 'end')
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Password successfully Saved!',bg='#fff',font=('Calibri(body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif username!='admin' and password!='1234' :  
       messagebox.showerror("Invalid","invalid username and password")
       
    elif password!="1234":
       messagebox.showerror("Invalid","invalid password")

    elif username!='admin':
       messagebox.showerror("Invalid","invalid username")    
        
img =ImageTk.PhotoImage(file='signup.png')
Label(root,image=img,bg='white',width=500,height=600).place(x=0,y=-60)

frame=Frame(root,width=380,height=350,bg="white")
frame.place(x=500,y=80)
heading=Label(frame,text='CREATE AN ACCOUNT',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=20,y=5)

#############-----------------------------
def on_enter(e):
    email.delete(0, 'end')

def on_leave(e):
    mail=email.get()
    if mail=='':
        email.insert(0,'email')
        
email = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
email.place(x=30,y=80)
email.insert(0,'email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##########-------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')
        
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
user.place(x=30,y=130)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)

##########-------------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    password=code.get()
    if password=='':
        code.insert(0,'password')

        
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11),show="*")
code.place(x=30,y=180)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=207)

################################


Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=257)
label=Label(frame,text="Existing Member? ",fg='black',bg='white',font=('Microsft YaHei UI Light',9))
label.place(x=35,y=307)

signin= Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=140,y=307)

root.mainloop()
