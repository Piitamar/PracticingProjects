from Note import Note, NoteManager
import customtkinter as ctk
from datetime import date, datetime

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
datestuff2.grid(row=0, column=0, padx=10, pady=5, sticky="w")

notetext = ctk.CTkLabel(app, text = 'NOTE!', font = font1)
notetext.grid(row=0, column=0, padx=10, pady=5, sticky="w")

noteentry = ctk.CTkEntry(master = app, placeholder_text = "write your note", width = 300, height= 200 )
noteentry.grid(row=0, column=0, padx=10, pady=5, sticky="w")

button = ctk.CTkButton(app, text="Click me", command=lambda: print("Clicked!"))
button.grid(row=0, column=0, padx=10, pady=5, sticky="w")

app.mainloop()
