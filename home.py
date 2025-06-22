from tkinter import *
import os

# --- Main Window Setup ---
top = Tk()
top.title('MedVault – Home')
top.config(bg='white')

# Maximize to fill screen but allow resizing
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
top.geometry(f"{screen_width}x{screen_height}+0+0")

# --- Button Handlers ---
def open_appointments():
    os.system('python appointments.py')

def open_prescriptions():
    os.system('python prescriptions.py')

def open_medical_records():
    os.system('python medical_records.py')

def login():
    os.system('python login.py')

# --- HERO SECTION ---
hero_frame = Frame(top, bg='#003366')
hero_frame.pack(fill=X, padx=20, pady=20)

Label(hero_frame, text="MedVault – Personal Medical History Manager",
      font=('Arial', 28, 'bold'), fg='white', bg='#003366').pack(anchor='w', padx=30, pady=(10, 5))

Label(hero_frame, text="Your one-stop solution to manage health records, prescriptions, appointments and more.",
      font=('Arial', 14), fg='white', bg='#003366').pack(anchor='w', padx=30, pady=(0, 10))

# --- Login & Exit Buttons in Hero Section ---
btn_frame = Frame(hero_frame, bg='#003366')
btn_frame.pack(anchor='e', padx=40)
btn_style = {'bg': '#2ecc71', 'fg': 'white', 'font': ('Arial', 12, 'bold'), 'width': 10, 'height': 1}
Button(btn_frame, text="Login", command=login, **btn_style).pack(side=LEFT, padx=10)
Button(btn_frame, text="Exit", command=top.destroy, **btn_style).pack(side=LEFT, padx=10)

# --- FUNCTIONAL CARDS SECTION ---
cards_frame = Frame(top, bg='white')
cards_frame.pack(pady=40, fill=X, padx=40)

card_style = {'width': 22, 'height': 2, 'font': ('Arial', 12, 'bold'), 'fg': 'white'}

def create_card(parent, title, desc, color, command):
    card = Frame(parent, bg='white', bd=2, relief=RIDGE)
    card.grid_propagate(False)
    card.columnconfigure(0, weight=1)
    Label(card, text=title, font=('Arial', 14, 'bold')).grid(row=0, pady=10, padx=10, sticky='n')
    Label(card, text=desc, font=('Arial', 10)).grid(row=1, padx=10, sticky='n')
    Button(card, text=f"Open {title}", bg=color, command=command, **card_style).grid(row=2, pady=10, padx=10, sticky='n')
    return card

card1 = create_card(cards_frame, "Appointments", "Manage doctor visits & scheduling.", '#6ab04c', open_appointments)
card2 = create_card(cards_frame, "Prescriptions", "Track your medication with ease.", '#0984e3', open_prescriptions)
card3 = create_card(cards_frame, "Medical Records", "Access reports and health data.", '#e17055', open_medical_records)

card1.grid(row=0, column=0, padx=40, sticky='nsew')
card2.grid(row=0, column=1, padx=40, sticky='nsew')
card3.grid(row=0, column=2, padx=40, sticky='nsew')
cards_frame.columnconfigure((0, 1, 2), weight=1)

# --- SECTION TEMPLATE FUNCTION ---
def create_section(parent, title, color, command):
    section = Frame(parent, bg='white')
    section.pack(pady=40, padx=60, fill=X)

    content = Frame(section, bg='white')
    content.pack(fill=X)

    # Left (Image Placeholder)
    Frame(content, bg=color, width=240, height=160).pack(side=LEFT, padx=20)

    # Right
    right = Frame(content, bg='white')
    right.pack(side=LEFT, fill=BOTH, expand=True)

    Label(right, text=title, font=('Arial', 18, 'bold'), bg='white').pack(anchor='w')
    Label(right, text=f"Explore and manage your {title.lower()} here. Easy to view, update, and secure!",
          font=('Arial', 12), bg='white').pack(anchor='w', pady=10)
    Button(right, text=f"Go to {title}", bg=color, fg='white', font=('Arial', 12), command=command).pack(anchor='w')

# --- INDIVIDUAL SECTIONS ---
create_section(top, title="Appointments", color="#6ab04c", command=open_appointments)
create_section(top, title="Prescriptions", color="#0984e3", command=open_prescriptions)
create_section(top, title="Medical Records", color="#e17055", command=open_medical_records)

# --- Mainloop ---
top.mainloop()
