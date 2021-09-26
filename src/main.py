import tkinter
from project_manager import ProjectManager, Widget

"""
TODO:
    [X] FEATURE: Add a way to make the user insert a name for the project and
                 create a new one (without passing a parameter for the name)

    [X] FEATURE: Add a button for inserting a input

    [] FEATURE: Insert a current datetime for each note input in the project

    [] FEATURE: Add a way to read text file using Tkinter

    [X] FEATURE: Add a better way to handle / manage the button creation (or leave it like that)
"""


class ButtonManager():
    def __init__(self, window : tkinter.Tk):
        self.window = window
        self.project_manager = ProjectManager()

    def create_button(self, text : str, command):
        return tkinter.Button(self.window, text = text, command = command, width=12, height=5)

    def add_project_button(self):
        add_proj_bttn = self.create_button("Add project", self.project_manager.create_project)
        add_proj_bttn.pack(side=tkinter.constants.LEFT, anchor=tkinter.constants.NW)

    def add_input_button(self):
        # TODO: Create add_input method and insert in the button bellow
        add_input_btton = self.create_button("Add a new input")
        add_input_btton.pack(side=tkinter.constants.LEFT, anchor=tkinter.constants.NW)


class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.buttons = ButtonManager(self.master)
        self.widget = Widget(self.master)
        self.configure_gui()

    def configure_gui(self):
        self.master.title("LightNotes")
        self.master.geometry("720x480")
        self.master.resizable(False, False)
        self.buttons.add_project_button()
        self.buttons.add_input_button()
        self.widget.create_project_list_box()


def main():
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()

main()
