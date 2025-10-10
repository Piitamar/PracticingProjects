from Note import Note, NoteManager
import customtkinter as ctk
from datetime import date, datetime
import csv
import pandas as pd

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
font1 = font = ("Arial", 24, "bold")
font2 = font = ("Arial", 14)

app = ctk.CTk()
app.geometry('500x600')
app.title("REINA'S DEMO NOTE APP")

datestuff1 = ctk.CTkLabel(master=app, text_color="#3f8d8f", text=date.today().strftime("%d/%m/%y"))
datestuff2 = ctk.CTkLabel(master=app, text_color="#3f8d8f", text=datetime.now().strftime("%H:%M:%S"))
datestuff1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
datestuff2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

notetext = ctk.CTkLabel(app, text = 'NOTE!', font = font1)
notetext.grid(row=0, column=2, padx=10, pady=5)

noteentry = ctk.CTkEntry(master = app, placeholder_text = "write your note", width = 300, height= 200 )
noteentry.grid(row=2, column=2, padx=20, pady=5)

def get_text():
    text = noteentry.get()
    print(text)
    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%H:%M:%S"), text])

button = ctk.CTkButton(app, text="Commit", command=lambda: get_text())
button.grid(row=3, column=2, padx=20, pady=5)

def delete_row():
    with open('data.csv', "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines:
        lines = lines[:-1]

    with open('data.csv', "w", encoding="utf-8") as f:
        f.writelines(lines)

button = ctk.CTkButton(app, text="Delete", command=lambda: delete_row())
button.grid(row=4, column=2, padx=20, pady=5)

app.mainloop()
