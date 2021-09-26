from tkinter import messagebox, simpledialog
from datetime import datetime
from tkinter import ttk
import tkinter
import os

CURRENT_SCRIPT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_NOTES_FOLDER_PATH = os.path.join(CURRENT_SCRIPT_FILE_PATH, "project_notes/")

class ProjectManager:
    def ask_for_project_name(self):
        return tkinter.simpledialog.askstring("What is the name of project?", "Insert the name of the project")

    def create_file(self, project_name, path_for_project_notes):
        """Creates txt file to store the notes"""
        with open(path_for_project_notes, 'x') as f:
            f.write(project_name.title() + "\n")

    def create_project(self):
        try:
            project_name = self.ask_for_project_name()

            if project_name is not None:
                file_name_for_project = f"{project_name}.txt".replace(" ", "_")
                path_for_project_notes = os.path.join(PROJECT_NOTES_FOLDER_PATH, file_name_for_project)

                self.create_file(project_name, path_for_project_notes)

        except FileExistsError:
            want_to_overwrite = messagebox.askyesno("WARNING", "Project already exists! \nDo you want overwrite it?")

            if(want_to_overwrite):
                os.remove(path_for_project_notes)
                self.create_file(project_name, path_for_project_notes)

    def add_input_note(self):
        current_time = datetime.now()
        input_note = None

class Widget:
    def __init__(self, master : tkinter.Tk):                                                                                               
       self.master = master                                                                                                               

    def create_project_list_box(self):                                                                 
        projects = [project.rstrip(".txt").title() for project in os.listdir(PROJECT_NOTES_FOLDER_PATH)]     
        list_box = tkinter.Listbox(self.master, height=10, width=15, activestyle='dotbox')
        
        for project_index, project in enumerate(projects):
            list_box.insert(project_index, project)

        list_box.pack(side=tkinter.constants.TOP, anchor=tkinter.constants.NE)
