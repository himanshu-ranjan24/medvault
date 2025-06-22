from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar,DateEntry





def add_prescription():
    root = Tk()
    root.geometry("500x400")
    root.title("Prescriptions")

    Label(root, text="Patient Name").pack()
    patient = Entry(root)
    patient.pack()

    Label(root, text="Medicine").pack()
    medicine = Entry(root)
    medicine.pack()

    Label(root, text="Dosage").pack()
    dosage = Entry(root)
    dosage.pack()

    Label(root, text="Frequency").pack()
    frequency = Entry(root)
    frequency.pack()

    def submit():
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='0365', db='python')
        cur = db.cursor()
        s = "INSERT INTO prescriptions (name, medicine, dosage, frequency) VALUES (%s, %s, %s, %s)"
        cur.execute(s, (patient.get(), medicine.get(), dosage.get(), frequency.get()))
        db.commit()
        messagebox.showinfo("Success", "Prescription Added")
        root.destroy()

    Button(root, text="Submit", command=submit).pack(pady=10)
    root.mainloop()

add_prescription()


