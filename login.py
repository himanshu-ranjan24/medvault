from tkinter import *
from tkinter import messagebox


top=Tk()
top.geometry('600x400')
top.title('Login')


    # Show/hide password toggle
def toggle_password():
    if password.cget('show') == '':
        password.config(show='*')
    else:
        password.config(show='')


Label(top, text="Username").place(x=50, y=80)
username = Entry(top)
username.place(x=150, y=80)

Label(top, text="Password").place(x=50, y=120)
password = Entry(top, show="*")
password.place(x=150, y=120)

show_pass = Checkbutton(top, text="Show Password", command=toggle_password)
show_pass.place(x=150, y=150)


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
        messagebox.showerror("Login", "❌ Invalid user Name and Password")

Button(top, text="Login", command=verify).place(x=150, y=180)

top.config(bg='sky blue')
top.mainloop()