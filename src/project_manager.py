import tkinter
from tkinter import messagebox, simpledialog
import os


class ProjectManager:
    def __init__(self):
        self.project_notes_folder_path = "project_notes/"

    def ask_for_project_name(self):
        return tkinter.simpledialog.askstring("What is the name of project?", "Insert the name of the project")

    def create_project(self):
        try:
            project_name = self.ask_for_project_name()

            if project_name is not None:
                file_name_for_project = f"{project_name}.txt".replace(" ", "_")
                path_for_project_notes = os.path.join(self.project_notes_folder_path, file_name_for_project)

                with open(path_for_project_notes, 'x') as f:
                    f.write(project_name.title())

        except FileExistsError:
            messagebox.showwarning("WARNING", "Project already exists")
