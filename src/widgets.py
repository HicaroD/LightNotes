from tkinter import simpledialog, filedialog, messagebox

class Widget:
    def ask_for_project_name(self):
        return simpledialog.askstring("Project name", "Insert the name of the project")

    def get_project_note_full_path(self):
        return filedialog.askopenfilename(initialdir = PROJECT_NOTES_FOLDER_PATH,
                                                  filetypes=[("Text files", "*.txt")])

    def get_input_note(self):
        return simpledialog.askstring("Input", "Add note to project in the dialog below:")

    def wants_to_overwrite_project(self) -> bool:
        return messagebox.askyesno("WARNING", "Project already exists! \nDo you want overwrite it?")

    def show_warning_for_empty_project_notes(self):
        messagebox.showwarning("Folder is empty", "You should create a project first")

    def show_warning_for_invalid_input(self):
        messagebox.showwarning("Invalid input", "Select a valid file")
