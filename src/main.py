import tkinter
from project_manager import ProjectManager

"""
TODO:
    [] BUG: Program is not throwing an exception when I try to create a new project, but it already exists

    [] FEATURE: Implement a way to make the user insert a name for the project
                and create a new one (without passing a parameter for the name)

    [] FEATURE: Find a way to read text file using Tkinter
"""


class Button():
    @staticmethod
    def create_button(master : tkinter.Tk, text : str, command):
        return tkinter.Button(master, text = text, command = command)


class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.project_manager = ProjectManager()
        self.configure_gui()

    def configure_gui(self):
        self.master.title("LightNotes")
        self.master.geometry("720x480")
        self.master.resizable(False, False)
        self.add_project_button()

    def add_project_button(self):
        add_proj_bttn = Button.create_button(self.master, "Add project", self.project_manager.create_project("teste"))
        add_proj_bttn.pack(side=tkinter.constants.LEFT, anchor=tkinter.constants.NW)



def main():
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()

main()
