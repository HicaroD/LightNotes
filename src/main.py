import tkinter
from ttkbootstrap import Style
from project_manager import ProjectManager, Widget

"""
TODO:
    [] BUG: When I insert a new entry in any project note, the changes don't show up immediately, I need to
            to insert another one or re-open the app to make previous changes appear
"""

TOP_LEFT_CORNER_POSITIONS = {"side" : tkinter.constants.LEFT, "anchor" : tkinter.constants.NW}

class ButtonManager():
    def __init__(self, window : tkinter.Tk):
        self.window = window
        self.project_manager = ProjectManager(window)

    def draw_buttons(self):
        self.add_project_button()
        self.add_input_button()
        self.add_info_button()
        self.see_note_button()

    def create_button(self, text : str, command, style = "primary.TButton"):
        return tkinter.ttk.Button(self.window, text = text, style = style, command = command)

    def add_project_button(self):
        add_proj_bttn = self.create_button("Add project", self.project_manager.create_project)
        add_proj_bttn.pack(side = TOP_LEFT_CORNER_POSITIONS["side"],
                           anchor = TOP_LEFT_CORNER_POSITIONS["anchor"])

    def add_input_button(self):
        add_input_btton = self.create_button("Add a new input", self.project_manager.add_input_note)
        add_input_btton.pack(side = TOP_LEFT_CORNER_POSITIONS["side"],
                             anchor = TOP_LEFT_CORNER_POSITIONS["anchor"])

    def add_info_button(self):
        from project_manager import info
        add_info_bttn = self.create_button("Info", style = "info.TButton", command = info)
        add_info_bttn.pack(side = tkinter.constants.RIGHT, anchor = tkinter.constants.SE)

    def see_note_button(self):
        see_note_bttn = self.create_button("See notes", self.project_manager.see_notes)
        see_note_bttn.pack(side = TOP_LEFT_CORNER_POSITIONS["side"],
                           anchor = TOP_LEFT_CORNER_POSITIONS["anchor"])


WINDOW_THEME = "journal"

class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.style = Style(theme=WINDOW_THEME)
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
