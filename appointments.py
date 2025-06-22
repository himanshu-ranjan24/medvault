from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar,DateEntry

def open_appointments():
    root = Tk()
    root.title("Appointments")
    # root.geometry("500x500")

    Label(root, text="Appointments", font=("Arial", 20, "bold")).pack(pady=10)

    # --- Input Fields ---
    Label(root, text="Patient Name").pack()
    patient_entry = Entry(root)
    patient_entry.pack()

    Label(root, text="Doctor Name").pack()
    doctor_entry = Entry(root)
    doctor_entry.pack()

    Label(root, text="Date (YYYY-MM-DD)").pack()
    date_entry = Entry(root)
    date_entry.pack()

    Label(root, text="Time (HH:MM)").pack()
    time_entry = Entry(root)
    time_entry.pack()

    Label(root, text="Reason").pack()
    reason_entry = Entry(root)
    reason_entry.pack()

    # --- Insert Function ---
    def add_appointment():
        patient = patient_entry.get()
        doctor = doctor_entry.get()
        date = date_entry.get()
        time = time_entry.get()
        reason = reason_entry.get()

        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='0365', db='python')
        cur = db.cursor()
        q = "INSERT INTO appointments (patient_name, doctor_name, date, time, reason) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(q, (patient, doctor, date, time, reason))
        db.commit()
        messagebox.showinfo("Success", "Appointment Added Successfully")
        clear_fields()

    def clear_fields():
        patient_entry.delete(0, END)
        doctor_entry.delete(0, END)
        date_entry.delete(0, END)
        time_entry.delete(0, END)
        reason_entry.delete(0, END) 

    def show_all():
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='0365', db='python')
        cur = db.cursor()
        cur.execute("SELECT * FROM appointments")
        data = cur.fetchall()
        output.delete(1.0, END)
        for row in data:
            output.insert(END, f"ID: {row[0]}, Patient: {row[1]}, Doctor: {row[2]}, Date: {row[3]}, Time: {row[4]}, Reason: {row[5]}\n")

    def delete_by_id():
        import pymysql as sql
        id_to_delete = id_entry.get()
        db = sql.connect(host='localhost', user='root', password='0365', db='python')
        cur = db.cursor()
        cur.execute("DELETE FROM appointments WHERE id=%s", (id_to_delete,))
        db.commit()
        messagebox.showinfo("Deleted", "Appointment Deleted")
        id_entry.delete(0, END)

    # --- Buttons ---
    Button(root, text="Add Appointment", command=add_appointment, bg="green", fg="white").pack(pady=10)
    Button(root, text="Show All", command=show_all).pack(pady=5)

    Label(root, text="Delete by ID").pack()
    id_entry = Entry(root)
    id_entry.pack()
    Button(root, text="Delete", command=delete_by_id, bg="red", fg="white").pack(pady=5)

    # --- Output Box ---
    output = Text(root, height=10, width=60)
    output.pack(pady=10)


    


    root.mainloop()

if __name__ == "__main__":
    open_appointments()

        