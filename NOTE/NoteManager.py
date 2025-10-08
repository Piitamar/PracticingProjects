from Note import Note, NoteManager
import customtkinter as ctk

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')

app = ctk.Ctk()
app.geometry('500x300')
app.title("REINA'S DEMO NOTE APP")

notetext = ctk.CtkLabel(app, text = 'NOTE!')
notetext.pack(pady=20)

entrynote = ctk.CtkEntry(app, )
ctk.CTkEntry

button = ctk.CTkButton(app, text="Click me", command=lambda: print("Clicked!"))
button.pack(pady=10)

app.mainloop()
