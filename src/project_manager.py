from tkinter import messagebox, simpledialog, filedialog
from datetime import datetime
from tkinter import ttk
import tkinter
import os

CURRENT_SCRIPT_FILE_ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_NOTES_FOLDER_PATH = os.path.join(CURRENT_SCRIPT_FILE_ABSOLUTE_PATH, "project_notes/")

class ProjectManager:
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
            wants_to_overwrite_project = messagebox.askyesno("WARNING", "Project already exists! \nDo you want overwrite it?")

            if(wants_to_overwrite_project):
                os.remove(path_for_project_notes)
                self.create_file(project_name, path_for_project_notes)

    def add_input_note(self):
        """Add a single note to an existing project"""
        try:
            current_time = datetime.now()
            project_note_full_path = Widget.get_project_note_full_path()

            if project_note_full_path is not None or project_note_full_path != ():
                input_note = Widget.get_input_note("Input", "Add note to project in the dialog below:")
                print(input_note)

                if(input_note is not None):
                    with open(project_note_full_path, 'a', encoding="utf-8") as project_note:
                        date_time = current_time.strftime("\U0001F4C5 %m/%d/%Y || \U0001F551 %H:%M:%S\n")
                        project_note.write(date_time)
                        project_note.write(input_note + "\n\n")

        except Exception as e:
            # TODO: Create a better error handling soon
            print(e)

class Widget:
    @staticmethod
    def ask_for_project_name():
        return tkinter.simpledialog.askstring("What is the name of project?", "Insert the name of the project")

    @staticmethod
    def get_project_note_full_path():
        return tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    @staticmethod
    def get_input_note(dialog_title : str, dialog_label : str):
        return tkinter.simpledialog.askstring(dialog_title, dialog_label)
