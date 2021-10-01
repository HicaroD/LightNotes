import tkinter
from ttkbootstrap import Style
from project_manager import ProjectManager, Widget

"""
TODO:
    [X] FEATURE: Add a way to read text file using Tkinter

    [] FEATURE: Create a new button "See notes" in the top right corner
                to select a project and see all your notes

                - Create see_notes()
                - Create see_notes_button() in ButtonManager class
                    - Add select a project widget
                    - Show all notes for that particular project in the middle of the screen


    [] FEATURE: Add a "info" button in the bottom right corner to open the default
                browser of the user in the repository of LightNotes
"""


class ButtonManager():
    def __init__(self, window : tkinter.Tk):
        self.window = window
        self.project_manager = ProjectManager()

    def draw_buttons(self):
        self.add_project_button()
        self.add_input_button()
        self.add_info_button()
        self.see_notes_button()

    def create_button(self, text : str, command, style = "primary.TButton"):
        return tkinter.ttk.Button(self.window, text = text, style = style, command = command)

    def add_project_button(self):
        add_proj_bttn = self.create_button("Add project", self.project_manager.create_project)
        add_proj_bttn.pack(side = tkinter.constants.LEFT, anchor = tkinter.constants.NW)

    def add_input_button(self):
        add_input_btton = self.create_button("Add a new input", self.project_manager.add_input_note)
        add_input_btton.pack(side = tkinter.constants.LEFT, anchor = tkinter.constants.NW)

    def see_notes_button(self):
        see_notes_bttn = self.create_button("See notes", lambda: self.project_manager.see_notes(self.window))
        see_notes_bttn.pack(side = tkinter.constants.LEFT, anchor = tkinter.constants.NW)

    def add_info_button(self):
        from project_manager import info
        add_info_bttn = self.create_button("Info", style = "info.TButton", command = info)
        add_info_bttn.pack(side = tkinter.constants.RIGHT, anchor = tkinter.constants.SE)


class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.style = Style(theme="journal")
        self.master = self.style.master
        self.buttons = ButtonManager(self.master)
        self.widget = Widget()
        self.configure_gui()

    def configure_gui(self):
        self.master.title("LightNotes")
        self.master.geometry("720x480")
        self.master.resizable(False, False)
        self.buttons.draw_buttons()


def main():
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()
main()
