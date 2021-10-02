import tkinter
import webbrowser
from tkinter import ttk
from tkinter import messagebox, simpledialog, filedialog
from datetime import datetime
import os

CURRENT_MAIN_FILE_ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_NOTES_FOLDER_PATH = os.path.join(CURRENT_MAIN_FILE_ABSOLUTE_PATH, "project_notes/")
PROJECT_GITHUB_LINK = "https://github.com/HicaroD/LightNotes"
LABEL_NOTES_SCREEN_POSITION = (70, 70)

def info():
    """A method for opening a web browser and redirect the user to the LightNotes repository"""
    webbrowser.open(PROJECT_GITHUB_LINK)

class ProjectErrorChecker:
    """ Solve common errors, for example, the program'd crash if project_notes folder doesn't exist """
    def __init__(self):
        self.create_project_notes_folder()

    def check_if_project_notes_folder_exists(self):
        return os.path.isdir(PROJECT_NOTES_FOLDER_PATH)

    def create_project_notes_folder(self):
        """Creates a project_notes folder in case of someone delete it"""
        if not self.check_if_project_notes_folder_exists():
            print("Creating project_notes folder")
            os.mkdir(PROJECT_NOTES_FOLDER_PATH)


class ProjectManager:
    def __init__(self, master = tkinter.Tk):
        ProjectErrorChecker()
        self.master = master
        self.text_widget = tkinter.Text(self.master)

    def create_file(self, project_name, path_for_project_notes):
        """Creates txt file to store the notes"""
        with open(path_for_project_notes, 'x') as f:
            f.write(project_name.title() + "\n\n")

    def create_project(self):
        """Creates a project in the project_notes folder"""
        try:
            project_name = Widget.ask_for_project_name()

            if project_name is not None:
                file_name_for_project = f"{project_name}.txt".replace(" ", "_")
                path_for_project_notes = os.path.join(PROJECT_NOTES_FOLDER_PATH,
                                                      file_name_for_project)
                self.create_file(project_name, path_for_project_notes)

        except FileExistsError:
            if Widget.wants_to_overwrite_project():
                os.remove(path_for_project_notes)
                self.create_file(project_name, path_for_project_notes)

    def add_input_note(self):
        """Add a single note to an existing project"""
        project_note_full_path = Widget.get_project_note_full_path()

        if project_note_full_path != "":
            input_note = Widget.get_input_note()

            if input_note is not None:
                date_time = datetime.now().strftime("\U0001F4C5 %m/%d/%Y  \U0001F551 %H:%M:%S\n")
                with open(project_note_full_path, 'a', encoding="utf-8") as project_note:
                    project_note.write(date_time)
                    project_note.write(input_note + "\n\n")

                    self.insert_text_into_text_widget(project_note_full_path)
                    self.place_text_widget()
                    self.see_notes(project_note_full_path)

    def place_text_widget(self):
        self.text_widget.place(x = LABEL_NOTES_SCREEN_POSITION[0],
                               y = LABEL_NOTES_SCREEN_POSITION[1])

    def insert_text_into_text_widget(self, project_note_path : str):
        with open(project_note_path) as project_note:
            self.text_widget.insert(1.0, project_note.read())
            self.text_widget.configure(state = "disabled") # READ-ONLY TEXT

    def see_notes(self, project_note_path : str = None):
        try:
            if project_note_path is not None:
                self.insert_text_into_text_widget(project_note_path)
            else:
                project_notes = Widget.get_project_note_full_path()
                self.insert_text_into_text_widget(project_notes)

            self.place_text_widget()

        except (TypeError, FileNotFoundError) as e:
            messagebox.showwarning("Invalid input", "Select a valid file")
            return None


class Widget:
    @staticmethod
    def ask_for_project_name():
        return tkinter.simpledialog.askstring("Project name", "Insert the name of the project")

    @staticmethod
    def get_project_note_full_path():
        return tkinter.filedialog.askopenfilename(initialdir = PROJECT_NOTES_FOLDER_PATH,
                                                  filetypes=[("Text files", "*.txt")])

    @staticmethod
    def get_input_note():
        return tkinter.simpledialog.askstring("Input", "Add note to project in the dialog below:")

    @staticmethod
    def wants_to_overwrite_project() -> bool:
        return messagebox.askyesno("WARNING", "Project already exists! \nDo you want overwrite it?")
