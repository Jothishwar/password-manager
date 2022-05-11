from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import re
import mysql.connector

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
    #print("table created")
except:
    a.execute("use passmanager")
    #print("table used") '''
#---------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.title('Password Manager')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def login():
    root.destroy()
    # import login
    os.system('python login.py')

def signup():
    mail=email.get()
    username=user.get()
    password=code.get()
    cp=cpass.get()
    if checkmail(mail):
        if checkuser(username):
            if checkpass(password):
                if checkps(cp):
                    print(mail,username,password,cp)
                    try:
                        sql="INSERT INTO users VALUES(%s,%s,%s)"
                        val=(mail,username,password)
                        a.execute(sql,val)
                        a.execute("CREATE TABLE %s(S_No INT PRIMARY KEY AUTO_INCREMENT,Website VARCHAR(100),Username VARCHAR(40),Password VARCHAR(40))"%(username))
                        z.commit()
                        messagebox.showinfo("Success","Account Created")
                    except:
                        messagebox.showerror("Error","User Already Exists")
                else:
                    messagebox.showerror("Invalid","Passwords do not match")
            else:
                messagebox.showerror("Invalid","Enter a valid Password")
        else:
            messagebox.showerror("Invalid","Enter a valid Username")
    else:
        messagebox.showerror("Invalid","Enter a valid email address")
        
img =ImageTk.PhotoImage(file='signup.png')
Label(root,image=img,bg='white',width=500,height=600).place(x=0,y=-60)

frame=Frame(root,width=380,height=380,bg="white")
frame.place(x=500,y=40)
heading=Label(frame,text='CREATE AN ACCOUNT',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=20,y=5)

#############-----------------------------
mregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def checkmail(email):
    if(re.fullmatch(mregex, email)):
        print("Valid Email")
        Frame(frame,width=295,height=2,bg='green').place(x=25,y=107)
        return True
 
    else:
        print("Invalid Email")
        Frame(frame,width=295,height=2,bg='red').place(x=25,y=107)
        return False

def on_enter(e):
    email.delete(0, 'end')

def on_leave(e):
    mail=email.get()
    if mail=='':
        email.insert(0,'email')        
email = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11),validate="focusout")
email["validatecommand"]=(email.register(checkmail),'%P')
email.place(x=30,y=80)
email.insert(0,'email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##########-------------------------------
uregex=r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
def checkuser(usn):
    if(re.fullmatch(uregex, usn)):
        print("Valid Username")
        Frame(frame,width=295,height=2,bg='green').place(x=25,y=157)
        return True
 
    else:
        print("Invalid Username")
        Frame(frame,width=295,height=2,bg='red').place(x=25,y=157)
        return False

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')
        
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11),validate="focusout")
user["validatecommand"]=(user.register(checkuser),'%P')
user.place(x=30,y=130)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)

##########-------------------------------

pregex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
def checkpass(ps):
    if(re.fullmatch(pregex, ps)):
        print("Valid Password")
        Frame(frame,width=295,height=2,bg='green').place(x=25,y=207)
        return True
 
    else:
        print("Invalid Password")
        Frame(frame,width=295,height=2,bg='red').place(x=25,y=207)
        return False

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    password=code.get()
    if password=='':
        code.insert(0,'password')

        
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11),validate="focusout")
code["validatecommand"]=(code.register(checkpass),'%P')
code.place(x=30,y=180)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=207)

##########-------------------------------

def checkps(ps):
    if(re.fullmatch(code.get(), ps)):
        print("Valid C-Password")
        Frame(frame,width=295,height=2,bg='green').place(x=25,y=257)
        return True
 
    else:
        print("Invalid C-Password")
        Frame(frame,width=295,height=2,bg='red').place(x=25,y=257)
        return False

def on_enter(e):
    cpass.delete(0, 'end')

def on_leave(e):
    password=cpass.get()
    if password=='':
        cpass.insert(0,'password')

cpass = Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11),show="*",validate="focusout")
cpass["validatecommand"]=(cpass.register(checkps),'%P')
cpass.place(x=30,y=230)
cpass.insert(0,'Password')
cpass.bind('<FocusIn>',on_enter)
cpass.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=257)

################################

s=Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup)
s.place(x=35,y=277)
label=Label(frame,text="Existing Member? ",fg='black',bg='white',font=('Microsft YaHei UI Light',9))
label.place(x=35,y=337)

signin= Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=login)
signin.place(x=140,y=337)

root.mainloop()
