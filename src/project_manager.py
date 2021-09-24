import os

project_notes_folder_path = "./project_notes/"

class ProjectManager:
    def create_project(self, project_name : str):
        file_name_for_project = f"{project_name}.txt"

        if(file_name_for_project not in os.listdir(project_notes_folder_path)):
            try:
                with open(os.path.join(project_notes_folder_path, file_name_for_project), mode="x", encoding="utf-8") as f:
                    print("Creating a new project: " + (project_notes_folder_path + file_name_for_project))

            except FileExistsError as e:
                print(e)







