
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk






top=Tk()
top.geometry('1200x600')
top.title('Welcome Form')




def home():
    import os
    top.destroy()
    import home
    os.system(' python home.py')



b6=Button(top,text='home',font=('Arial 15 bold') ,command=home)
b6.place(x=1050,y=35)


top.mainloop()







'''
old login



def showpasword():
    if e2.cget('show')=="*":
        e2.config(show="")
    else:
        e2.config(show="*")


def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='0365', db='python')
    cur = db.cursor()
    cur.execute("SELECT * FROM prjk WHERE name = %s AND password = %s", (e1.get(),e2.get()))
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("Error","Invalid user Name and Password")
    else:
        top.destroy()
        import home

L= Label(top,text='Login',bg='blue',fg='white',font=('Arial 25 bold'))
L.place(x=500,y=50)
Label(top, text="Username").place(x=50, y=80)
username = Entry(top)
username.place(x=150, y=80)

L2= Label(top,text='name',bg='white',fg='black',font=('Arial 20 bold'))
L2.place(x=200,y=150)

e1=Entry(top,font=('Arial 20 bold'))
e1.place(x=350,y=150)

L3= Label(top,text='Password',bg='white',fg='black',font=('Arial 20 bold'))
L3.place(x=200,y=250)

e2=Entry(top,font=('Arial 20 bold'),show='*')
e2.place(x=350,y=250)

cbk=Checkbutton(top,command=showpasword)
cbk.place(x=660,y=250)

b1=Button(top,text='Login',font=('Arial 15 bold'),command=Login)
b1.place(x=250,y=400)
'''




'''
new login


from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.geometry("400x300")
top.title("Login Form")

Label(top, text="Username").place(x=50, y=80)
    username = Entry(top)
    username.place(x=150, y=80)

    Label(top, text="Password").place(x=50, y=120)
    password = Entry(top, show="*")
    password.place(x=150, y=120)

    def verify():
        user = username.get()
        pwd = password.get()
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='0365', db='python')
        cur = db.cursor()
        s = "SELECT * FROM prjk WHERE name=%s AND password=%s"
        result = cur.execute(s, (user, pwd))
        if result > 0:
            messagebox.showinfo("Login", "✅ Login Successful!")
            top.destroy()
            import home
            home.open_home(user)
        else:
            messagebox.showerror("Login", "❌ Invalid credentials")

    Button(top, text="Login", command=verify).place(x=150, y=180)



    top.mainloop()'''






'''from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar,DateEntry

def show():
    t=cal.get()
    print(t)


top=Tk()
top.geometry('1500x600')
top.title('welcome')

f1= Frame(top,height=200,width=1500,bg='orange')
f1.place(x=0,y=0)

f2= Frame(top,height=200,width=1500,bg='white')
f2.place(x=0,y=201)

f3= Frame(top,height=200,width=1500,bg='green')
f3.place(x=0,y=401)


c1= Checkbutton(f2,text='java',font=('Arial 15 bold'))
c1.place(x=200,y=100)

c2= Checkbutton(f2,text='python',font=('Arial 15 bold'))
c2.place(x=300,y=100)

c3= Checkbutton(f2,text='php',font=('Arial 15 bold'))
c3.place(x=400,y=100)


c1= Radiobutton(f3,text='Male',value='Male',font=('Arial 15 bold'))
c1.place(x=200,y=100)

c2= Radiobutton(f3,text='Female',value='Female',font=('Arial 15 bold'))
c2.place(x=300,y=100)

c3= Radiobutton(f3,text='Other',value='other',font=('Arial 15 bold'))
c3.place(x=400,y=100)

c1.select()


k=['Select','java','python','php','ruby','html','css','React','other']

cb=ttk.Combobox(f1, value=k,font=('Arial 20 bold'))
cb.place(x=200,y=50)
cb.current(0)

cal= DateEntry(f3,width=30,fg='white',bg='black',font=('Arial 25 bold'))
cal.place(x=300,y=100)

L= Label(top,text='welcome',bg='blue',fg='white',font=('Arial 25 bold'))
L.place(x=500,y=50)

b=Button(f3,text='submit',command=show)
b.place(x=400,y=150)'''


