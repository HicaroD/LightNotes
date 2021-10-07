import os
import tkinter
import webbrowser
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox, simpledialog, filedialog

CURRENT_MAIN_FILE_ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_NOTES_FOLDER_PATH = os.path.join(CURRENT_MAIN_FILE_ABSOLUTE_PATH, "project_notes/")
PROJECT_GITHUB_LINK = "https://github.com/HicaroD/LightNotes"
LABEL_NOTES_SCREEN_POSITION = (70, 70)

def info():
    """A method for opening a web browser and redirect the user to the LightNotes repository"""
    webbrowser.open(PROJECT_GITHUB_LINK)

class ProjectErrorChecker:
    def __init__(self):
        self.create_project_notes_folder()

    def check_if_project_notes_folder_exists(self):
        return os.path.isdir(PROJECT_NOTES_FOLDER_PATH)

    def create_project_notes_folder(self):
        if not self.check_if_project_notes_folder_exists():
            print("Creating project_notes folder")
            os.mkdir(PROJECT_NOTES_FOLDER_PATH)

    def check_if_project_notes_folder_is_empty(self):
        return not os.listdir(PROJECT_NOTES_FOLDER_PATH)


class ProjectManager:
    def __init__(self, master = tkinter.Tk):
        self.master = master
        self.widget = Widget()
        self.project_error_checker = ProjectErrorChecker()
        self.text_widget_for_notes = tkinter.Text(self.master)

    def create_file(self, project_name, path_for_project_notes):
        with open(path_for_project_notes, 'x') as f:
            f.write(project_name.title() + "\n\n")

    def create_project(self):
        try:
            project_name = self.widget.ask_for_project_name()

            if project_name is not None:
                file_name_for_project = f"{project_name}.txt".replace(" ", "_")
                path_for_project_notes = os.path.join(PROJECT_NOTES_FOLDER_PATH,
                                                      file_name_for_project)
                self.create_file(project_name, path_for_project_notes)

        except FileExistsError:
            if self.widget.wants_to_overwrite_project():
                os.remove(path_for_project_notes)
                self.create_file(project_name, path_for_project_notes)

    def create_timestamp_for_input_note(self):
        return datetime.now().strftime("\U0001F4C5 %m/%d/%Y  \U0001F551 %H:%M:%S\n")

    def remove_note(self):
        if self.project_error_checker.check_if_project_notes_folder_is_empty():
            self.widget.show_warning_for_empty_project_notes()
            return

        project_notes_path_to_remove = self.widget.get_project_note_full_path()

        if project_notes_path_to_remove != "":
            os.remove(project_notes_path_to_remove)
            self.text_widget_for_notes.configure(state = "normal")
            self.text_widget_for_notes.delete(1.0, tkinter.END)
            self.text_widget_for_notes.configure(state = "disabled")

    def add_input_note_to_text_widget(self):
        if self.project_error_checker.check_if_project_notes_folder_is_empty():
            self.widget.show_warning_for_empty_project_notes()
            return

        project_note_full_path = self.widget.get_project_note_full_path()

        if isinstance(project_note_full_path, str):
            input_note = self.widget.get_input_note()

            if input_note is not None:
                self.write_input_notes_to_file(input_note, project_note_full_path)
                self.insert_text_from_file_into_text_widget(project_note_full_path)
                self.place_text_widget()

    def write_input_notes_to_file(self, input_note : str, project_note_full_path : str):
        timestamp_for_input_note = self.create_timestamp_for_input_note()

        with open(project_note_full_path, 'a', encoding="utf-8") as project_note_file:
            project_note_file.write(timestamp_for_input_note)
            project_note_file.write(input_note + "\n\n")

    def place_text_widget(self):
        self.text_widget_for_notes.place(x = LABEL_NOTES_SCREEN_POSITION[0],
                                         y = LABEL_NOTES_SCREEN_POSITION[1])

    def insert_text_from_file_into_text_widget(self, project_note_path : str):
        with open(project_note_path) as project_note:
            self.text_widget_for_notes.configure(state = "normal")
            self.text_widget_for_notes.delete(1.0, tkinter.END)
            self.text_widget_for_notes.insert(1.0, project_note.read())
            self.text_widget_for_notes.configure(state = "disabled")

    def see_notes(self):
        try:
            if self.project_error_checker.check_if_project_notes_folder_is_empty():
                self.widget.show_warning_for_empty_project_notes()
                return

            project_note_path = self.widget.get_project_note_full_path()
            self.insert_text_from_file_into_text_widget(project_note_path)
            self.place_text_widget()

        except (TypeError, FileNotFoundError) as e:
            messagebox.showwarning("Invalid input", "Select a valid file")

class Widget:
    def ask_for_project_name(self):
        return tkinter.simpledialog.askstring("Project name", "Insert the name of the project")

    def get_project_note_full_path(self):
        return tkinter.filedialog.askopenfilename(initialdir = PROJECT_NOTES_FOLDER_PATH,
                                                  filetypes=[("Text files", "*.txt")])

    def get_input_note(self):
        return tkinter.simpledialog.askstring("Input", "Add note to project in the dialog below:")

    def wants_to_overwrite_project(self) -> bool:
        return messagebox.askyesno("WARNING", "Project already exists! \nDo you want overwrite it?")

    def show_warning_for_empty_project_notes(self):
        messagebox.showwarning("Folder is empty", "You should create a project first")
        return
