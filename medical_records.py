from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar,DateEntry


def open_medical_records():
    win = Tk()
    win.geometry("500x500")
    win.title("Medical Records")

    # Labels
    Label(win, text="Patient Name").place(x=50, y=50)
    Label(win, text="Disease").place(x=50, y=100)
    Label(win, text="Diagnosis Date").place(x=50, y=150)
    Label(win, text="Treatment").place(x=50, y=200)
    Label(win, text="Doctor").place(x=50, y=250)

    # Entry Fields
    patient_entry = Entry(win)
    patient_entry.place(x=200, y=50)

    disease_entry = Entry(win)
    disease_entry.place(x=200, y=100)

    date_entry = Entry(win)
    date_entry.place(x=200, y=150)

    treatment_entry = Entry(win)
    treatment_entry.place(x=200, y=200)

    doctor_entry = Entry(win)
    doctor_entry.place(x=200, y=250)

    # Function to insert medical record
    def add_record():
        patient = patient_entry.get()
        disease = disease_entry.get()
        date = date_entry.get()
        treatment = treatment_entry.get()
        doctor = doctor_entry.get()

        if patient and disease:
            import pymysql as sql
            db = sql.connect(host='localhost', user='root', password='0365', db='python')
            cur = db.cursor()
            q = "INSERT INTO medical_records (patient, disease, diagnosis_date, treatment, doctor) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(q, (patient, disease, date, treatment, doctor))
            db.commit()
            messagebox.showinfo("Success", "Medical Record Added Successfully")
            clear_fields()
        else:
            messagebox.showerror("Error", "Please fill all required fields")

    def clear_fields():
        patient_entry.delete(0, END)
        disease_entry.delete(0, END)
        date_entry.delete(0, END)
        treatment_entry.delete(0, END)
        doctor_entry.delete(0, END)

    # Button to add
    Button(win, text="Add Record", command=add_record).place(x=200, y=320)

    win.mainloop()

# Run directly
if __name__ == "__main__":
    open_medical_records()
