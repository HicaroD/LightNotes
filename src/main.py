import tkinter
from project_manager import ProjectManager

"""
TODO:
    [X] FEATURE: Add a way to make the user insert a name for the project and
                 create a new one (without passing a parameter for the name)

    [] FEATURE: Add a way to read text file using Tkinter

    [] FEATURE: Add a better way to handle / manage the button creation (or leave it like that)
"""


class ButtonManager():
    def __init__(self, master : tkinter.Tk):
        self.master = master
        self.project_manager = ProjectManager()

    def create_button(self, text : str, command):
        return tkinter.Button(self.master, text = text, command = command)

    def add_project_button(self):
        add_proj_bttn = self.create_button("Add project", self.project_manager.create_project)
        add_proj_bttn.pack(side=tkinter.constants.LEFT, anchor=tkinter.constants.NW)


class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.buttons = ButtonManager(self.master)
        self.configure_gui()

    def configure_gui(self):
        self.master.title("LightNotes")
        self.master.geometry("720x480")
        self.master.resizable(False, False)
        self.buttons.add_project_button()


def main():
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()

main()
