from storage import ExcelStorage
from task_manager import TaskManager
import pandas as pd

MAIN_MENU = ["Projects", "Quit"]


class CLI:
    def __init__(self, task_manager: TaskManager):
        self.manager = task_manager

    def print_logo(self):
        print("=============")
        print(" Task Manager")
        print("=============")

    def add_task(self, project):
        title = input("Task: ")
        priority = input("Priority: ")
        next_action = input("Next action: ")
        notes = input("Notes: ")
        
        task_data = {
            "ID": None,
            "Project": project,
            "Task": title,
            "Status": "Pending",
            "Priority": priority,
            "Created": pd.Timestamp.now(),
            "Started": None,
            "Completed": None,
            "Next Action": next_action,
            "Notes": notes,
        }
        self.manager.add_task(project, task_data)
        print("Task added.")

    def edit_task(self, project, task_id):
        title = input("Task (leave blank to skip): ") or None
        priority = input("Priority (leave blank to skip): ") or None
        next_action = input("Next action (leave blank to skip): ") or None
        notes = input("Notes (leave blank to skip): ") or None
        status = input("Status (leave blank to skip): ") or None
        
        updates = {}
        if title:
            updates["Task"] = title
        if priority:
            updates["Priority"] = priority
        if next_action:
            updates["Next Action"] = next_action
        if notes:
            updates["Notes"] = notes
        if status:
            updates["Status"] = status
        
        if updates:
            self.manager.update_task(project, task_id, updates)
            print("Task updated.")
        else:
            print("No changes made.")

    def create_project(self):
        name = input("Give project name: ")
        if len(name) >= 3:
            self.manager.create_project(name)
            print(f"Project '{name}' created.")
        else:
            print("Project name must be at least 3 characters.")

    def show_menu(self, title, options):
        self.print_logo()
        print(title)
        print()

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
            
        while True:
            choice = input("> ")

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= len(options):
                    return choice

            print("Invalid choice.")

    def print_task_details(self, task):
        self.print_logo()
        for key, value in task.items():
            print(f"{key}: {value}")
        print()

    def show_task_menu(self, task):
        while True:
            choice = self.show_menu(
                task["Task"],
                [
                    "View Details",
                    "Complete",
                    "Edit",
                    "Delete",
                    "Back",
                ],
            )

            if choice == 1:
                self.print_task_details(task)
                input("Press Enter...")

            elif choice == 2:
                self.manager.update_task(task["Project"], task["ID"], {"Status": "Completed", "Completed": pd.Timestamp.now()})
                print("Task marked as completed.")
                return

            elif choice == 3:
                self.edit_task(task["Project"], task["ID"])
                return

            elif choice == 4:
                self.manager.delete_task(task["Project"], task["ID"])
                print("Task deleted.")
                return

            elif choice == 5:
                return

    def show_tasks_menu(self, project):
        while True:
            tasks = self.manager.get_tasks(project)

            if tasks.empty:
                print("No tasks.")
                input("Press Enter...")
                return

            task_titles = tasks["Task"].tolist()
            task_titles.append("Back")

            choice = self.show_menu("Tasks", task_titles)

            if choice == len(task_titles):
                return

            task = tasks.iloc[choice - 1].to_dict()
            self.show_task_menu(task)

    def show_project_menu(self, project):
        while True:
            choice = self.show_menu(
                project,
                [
                    "View Tasks",
                    "Add Task",
                    "Back",
                ],
            )

            if choice == 1:
                self.show_tasks_menu(project)

            elif choice == 2:
                self.add_task(project)

            elif choice == 3:
                return

    def show_projects_menu(self):
        while True:
            projects = self.manager.get_projects()
            options = projects + ["New Project", "Back"]

            choice = self.show_menu("Projects", options)

            if choice <= len(projects):
                project = projects[choice - 1]
                self.show_project_menu(project)

            elif choice == len(projects) + 1:
                self.create_project()

            else:
                return

    def run(self):
        self.print_logo()
        while True:
            choice = self.show_menu("Main Menu", MAIN_MENU)

            if choice == 1:
                self.show_projects_menu()

            elif choice == 2:
                print("Goodbye!")
                return


if __name__ == "__main__":
    storage = ExcelStorage()
    manager = TaskManager(storage)
    cli = CLI(manager)
    cli.run()
