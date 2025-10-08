from datetime import date

class Note:
    def __init__(self, text):
        self.date = date.today()
        self.text = text

    def __str__(self):
        return f"{self.date} - {self.text}"

class NoteManager:
    def __init__(self):
        self.notes = []

    def __repr__(self):
        return f"Note(text='{self.text}', date={self.date})"

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, note):
        self.notes.remove(note)

    def search(self, keyword):
        return [n for n in self.notes if keyword in n.text]

    def get_notes_sorted(self):
        return sorted(self.notes, key=lambda n: n.date)
    
    def printlist(self):
        for note in self.notes:
            print (note)

note1= Note('Hôm nay trPời mưa')
note2= Note('Hôm nay mình buồn')

notemanager1= NoteManager()
for note in [note1, note2]:
    notemanager1.add_note(note)
notemanager1.printlist()

