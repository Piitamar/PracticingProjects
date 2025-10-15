from Note import Note, NoteManager
import customtkinter as ctk
from datetime import date, datetime
import csv
import pandas as pd
from Note import Note, NoteManager

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')
font1 = font = ("Arial", 24, "bold")
font2 = font = ("Arial", 12,"bold")

app = ctk.CTk()
app.geometry('800x600')
app.title("REINA'S DEMO NOTE APP")

'''------------------SCROLLBAR--------------------------------------------------'''
sframe = ctk.CTkScrollableFrame(master=app, width=800, height=600, bg_color="#ffffff", corner_radius=5,scrollbar_button_color="#527280")
sframe.pack()

'''----------------------TOPPAGE-----------------------------------------------------'''
datestuff1 = ctk.CTkLabel(master=sframe, text_color="#3f8d8f", text=date.today().strftime("%d/%m/%y"))
datestuff2 = ctk.CTkLabel(master=sframe, text_color="#3f8d8f", text=datetime.now().strftime("%H:%M:%S"))
datestuff1.grid(row=1, column=0, padx=20, sticky="w")
datestuff2.grid(row=2, column=0, padx=20, sticky="w")

notetext = ctk.CTkLabel(sframe, text = 'NOTE!', font = font1)
notetext.grid(row=1, column=0, padx=2, pady=5)

'''----------------------NOTEENTRY---------------------------------------------------'''

noteentry = ctk.CTkEntry(master = sframe, placeholder_text = "write your note", width = 300, height= 200 )
noteentry.grid(row=3, column=0, padx=2, pady=5)

def get_text():
    global notes
    text = noteentry.get()

    print(text)
    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        time = datetime.now().strftime("%H:%M:%S")
        writer.writerow([time, text])

    notes = []
    with open('data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            notes.append(line)
    
    for time, text in notes:
        print(f"{time} — {text}")


button = ctk.CTkButton(sframe, bg_color="#356C7D", text="Commit", command=lambda: get_text())
button.grid(row=4, column=0, padx=2, pady=5)

'''------------------PHẦN KHUNG NOTES THẢ XUỐNG-----------------------------------'''
def createnotelabel(TEXT,n):
    notelabels = ctk.CTkLabel(master=sframe, width=300, fg_color="#bcd2d6", corner_radius=10, height=70, text_color="#277576", font=font2,anchor="w", text=TEXT)
    notelabels.grid(row=5+n, column=0, padx=2, pady=5)

notes = []
with open('data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        notes.append(line)

for n, note in enumerate(notes):
    createnotelabel(note,n)

'''--------------------NÚT DELL------------------------------------------------------------'''
def delete_row(note):
    df = pd.read_csv("data.csv", names=['date', 'text'], header=None)
    df[df['text'] != note]
    df.to_csv("data.csv")

def createdeletebutton(note, n):
    deletebuttons = ctk.CTkButton(master=sframe, text="Delete", width=20, command=delete_row(note))
    deletebuttons.grid(row=5+n, column=1, padx=2, pady=5)

for n, note in enumerate(notes):
    createdeletebutton(note, n)

'''-----------------------------------END----------------------------------------------'''
app.mainloop()
