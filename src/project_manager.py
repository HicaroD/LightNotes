import tkinter
from tkinter import ttk
from tkinter import messagebox, simpledialog, filedialog
from datetime import datetime
import webbrowser
import os

CURRENT_MAIN_FILE_ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_NOTES_FOLDER_PATH = os.path.join(CURRENT_MAIN_FILE_ABSOLUTE_PATH,
                                         "project_notes/")
PROJECT_GITHUB_LINK = "https://github.com/HicaroD/LightNotes"

def info():
    """A method for opening a web browser and redirect the user to the LightNotes repository"""
    webbrowser.open(PROJECT_GITHUB_LINK)

class ProjectChecker:
    """Class for checking and solving commons erros.
        - Project notes default folder might not exists and the program will try to access it.
        - User is trying to access a project that doesn't even exists
    """
    def __init__(self):
        self.create_project_notes_folder()

    def check_if_project_notes_folder_exists(self):
        return os.path.isdir(PROJECT_NOTES_FOLDER_PATH)

    def create_project_notes_folder(self):
        """Creates a project_notes folder in case of someone delete it"""
        if not self.check_if_project_notes_folder_exists():
            os.mkdir(PROJECT_NOTES_FOLDER_PATH)

    def check_if_project_exists(project) -> bool:
        return project is not None or project != ()


class ProjectManager:
    def __init__(self):
        self.project_checker = ProjectChecker()

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
                path_for_project_notes = os.path.join(PROJECT_NOTES_FOLDER_PATH, file_name_for_project)
                self.create_file(project_name, path_for_project_notes)

        except FileExistsError:
            if Widget.wants_to_overwrite_project():
                os.remove(path_for_project_notes)
                self.create_file(project_name, path_for_project_notes)

    def add_input_note(self):
        """Add a single note to an existing project"""
        project_note_full_path = Widget.get_project_note_full_path()

        if self.project_checker.check_if_project_exists():
            input_note = Widget.get_input_note()

            if(input_note is not None):
                current_time = datetime.now()
                date_time = current_time.strftime("\U0001F4C5 %m/%d/%Y  \U0001F551 %H:%M:%S\n")

                with open(project_note_full_path, 'a', encoding="utf-8") as project_note:
                    project_note.write(date_time)
                    project_note.write(input_note + "\n\n")

    def see_notes(self, master : tkinter.Tk):
        project_notes = Widget.get_project_note_full_path()

        if self.project_checker.check_if_project_exists:
            with open(project_notes, 'r') as notes:
                text = tkinter.Text(master)
                text.insert(1.0, chars = notes.read())
                text.configure(state = "disabled")
                text.pack(anchor = tkinter.constants.CENTER)


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
