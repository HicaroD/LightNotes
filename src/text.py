import tkinter
from datetime import datetime

LABEL_NOTES_SCREEN_POSITION = (70, 70)

class Text:
    def __init__(self, master : tkinter.Tk):
        self.master = master
        self.text_widget = tkinter.Text(self.master)
   
    def clear_text(self):
        self.text_widget.configure(state = "normal")
        self.text_widget.delete(1.0, tkinter.END)
        self.text_widget.configure(state = "disabled")
    
    def place_text_widget(self):
        self.text_widget.place(x = LABEL_NOTES_SCREEN_POSITION[0],
                               y = LABEL_NOTES_SCREEN_POSITION[1])

    def insert_text_from_file_into_text_widget(self, project_note_path : str):
        with open(project_note_path) as project_note:
            self.text_widget.configure(state = "normal")
            self.text_widget.delete(1.0, tkinter.END)
            self.text_widget.insert(1.0, project_note.read())
            self.text_widget.configure(state = "disabled")

    def create_timestamp_for_input_note(self):
        return datetime.now().strftime("%m/%d/%Y   %H:%M:%S\n")
