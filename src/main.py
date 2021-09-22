import tkinter

"""
TODO:
    [] Add button in the top-left corner to add a new project
    [] Find a way to read text file in Tkinter
"""


class Button():
    @staticmethod
    def create_button(master : tkinter.Tk, text : str, command):
        return tkinter.Button(master, text = text, command = command)


class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure_gui()
        self.add_project_button()

    def configure_gui(self):
        self.master.title("LightNotes")
        self.master.geometry("720x480")
        self.master.resizable(False, False)


def main():
    root = tkinter.Tk()
    app = Application(root)
    root.mainloop()

main()
