from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk

top=Tk()
# top.geometry('1200x600')
top.attributes('-fullscreen', True)
top.title('Welcome Form')


def showpasword():
    if e4.cget('show')=="*":
        e4.config(show="")
    else:
        e4.config(show="*") 

        

def insert():
    k = e1.get()   # Ensure this line is present
    k2 = e2.get()
    k3 = int(e3.get())
    k4 = e4.get()
    k5 = var.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='0365', db='python')
    cur = db.cursor()
    
    s = "insert into prjk values('%s', '%s', '%s', '%s', '%s')" % (k, k2, k3, k4, k5)
    result = cur.execute(s)
    
    if result > 0:
        #db.commit()
        messagebox.showinfo("Result","Data inserted successfully")
    else:
        messagebox.showinfo("Result","Failed to insert data")
    db.commit()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')

def Delete():
    k = e1.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='0365', db='python')
    cur = db.cursor()
    s = "delete from prjk where name=%s"
    result = cur.execute(s,k)
    if (result > 0):
        messagebox.showinfo("Result","Record Delete  successfully")
    else:
        messagebox.showinfo("Result","Record not Delete  successfully")
    db.commit()

def search():
    #for i in tv.get_childern():
        #tv.delete(i)
        
    k = e1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='0365', db='python')
    cur = db.cursor()
    s = "select * from prjk where name=%s"
    t = cur.execute(s,k)
    result = cur.fetchall()
    if (t > 0) :
        for col in result:
            Name = col[0]
            Lastname = col[1]
            age = col[2]
            Password = col[3] 

            print(Name,Lastname,age,Password)
            messagebox.showinfo("Result","Record search  successfully")
    
    else:
        messagebox.showinfo("Result","No data found")

        


'''def show():
    for i in tv.get_children():
        tv.delete(i)      


    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='0365', db='python')
    cur = db.cursor()
    S="select * from prjk"
    t = cur.execute(S)
    result = cur.fetchall()
    if (t > 0) :
        for col in result:
            Name = col[0]
            Lastname = col[1]
            age = col[2]
            Password = col[3]
            
            tv.insert("", 'end', values=(Name,Lastname,age,Password))

            #print(Name,Lastname,age,Password)
    else:
        messagebox.showinfo("Result","No data found")'''

def login():
    import os
    #top.destroy()
    import login
    os.system(' python login.py')


def home():
    import os
    top.destroy()
    import home
    os.system(' python home.py')
        



var=StringVar()

path=r"C:\Users\Sudhanshu\Downloads\Biomedical-Data-Lifecycle-BlogHeroFeature-1400x788-1.jpg"
# img=ImageTk.PhotoImage(Image.open(path))

# L12=Label(top,image=img)
# L12.pack()

tv = ttk.Treeview(top)
tv['columns']=('Name', 'Lastname','age','password')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=150)
tv.column('Lastname', anchor=CENTER, width=150)
tv.column('age', anchor=CENTER, width=150)
tv.column('password', anchor=CENTER, width=150)


'''tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('age', text='age', anchor=CENTER)
tv.heading('password', text='Password', anchor=CENTER)
tv.place(x=600,y=150)'''

L=Label(top,text='Registration',bg='red',fg='white',font=('Arial 25 bold'))
L.place(x=500,y=30)

L2=Label(top,text='Name',bg='blue',fg='white',font=('Arial 12 bold'))
L2.place(x=100,y=150)

e1=Entry(top,font=('Arial 15 bold'))
e1.place(x=250,y=150)

L3=Label(top,text='Lastname',bg='blue',fg='white',font=('Arial 12 bold'))
L3.place(x=100,y=190)

e2=Entry(top,font=('Arial 15 bold'))
e2.place(x=250,y=190)

L4=Label(top,text='Age',bg='blue',fg='white',font=('Arial 12 bold'))
L4.place(x=100,y=230)

e3=Entry(top,font=('Arial 15 bold'))
e3.place(x=250,y=230)

L5=Label(top,text='Password',bg='blue',fg='white',font=('Arial 12 bold'))
L5.place(x=100,y=270)

e4=Entry(top,font=('Arial 15 bold'),show='*')
e4.place(x=250,y=270)

L6=Label(top,text='Gender',bg='blue',fg='white',font=('Arial 12 bold'))
L6.place(x=100,y=350)

r1=Radiobutton(top,text='Male',bg='gray',value='Male',variable=var,font=('Arial 10 bold'))
r1.place(x=250,y=350)

r2=Radiobutton(top,text='Female',bg='pink',value='Female',variable=var,font=('Arial 10 bold'))
r2.place(x=320,y=350)

r3=Radiobutton(top,text='Other',value='Other',variable=var,font=('Arial 10 bold'))
r3.place(x=410,y=350)

r1.select()

b1=Button(top,text='submit',bg='red',font=('Arial 15 bold'),command=insert)
b1.place(x=250,y=400)

'''b2=Button(top,text='Delete',font=('Arial 15 bold') ,command=Delete)
b2.place(x=200,y=500)

b3=Button(top,text='Search',font=('Arial 15 bold') ,command=search)
b3.place(x=450,y=500)'''


'''b4=Button(top,text='show',font=('Arial 15 bold') ,command=show)
b4.place(x=650,y=500)'''

b5=Button(top,text='Login',bg='RED',font=('Arial 15 bold') ,command=login)
b5.place(x=900,y=35)

#b6=Button(top,text='Exit',font=('Arial 15 bold') ,command=show)
#b6.place(x=950,y=500)

b6=Button(top,text='home',font=('Arial 15 bold') ,command=home)
b6.place(x=1050,y=35)


cbk=Checkbutton(top,command=showpasword)
cbk.place(x=480,y=270)

#top.config(bg='green')
top.mainloop()


