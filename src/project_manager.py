import tkinter
from tkinter import messagebox, simpledialog
import os


class ProjectManager:
    def __init__(self):
        self.project_notes_folder_path = "project_notes/"

    def ask_for_project_name(self):
        return tkinter.simpledialog.askstring("What is the name of project?", "Insert the name of the project")

    def create_file(self, project_name, path_for_project_notes):
        """Creates txt file to store the notes"""
        with open(path_for_project_notes, 'x') as f:
            f.write(project_name.title())

    def create_project(self):
        try:
            project_name = self.ask_for_project_name()

            if project_name is not None:
                file_name_for_project = f"{project_name}.txt".replace(" ", "_")
                path_for_project_notes = os.path.join(self.project_notes_folder_path, file_name_for_project)

                self.create_file(project_name, path_for_project_notes)

        except FileExistsError:
            want_to_overwrite = messagebox.askyesno("WARNING", "Project already exists! \nDo you want overwrite it?")

            if(want_to_overwrite):
                os.remove(path_for_project_notes)
                self.create_file(project_name, path_for_project_notes)
