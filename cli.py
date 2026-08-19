from datetime import datetime

MAIN_MENU = ["Projects", "Quit"]


class CLI:
    def __init__(self, manager):
        self.manager = manager

    def print_logo(self):
        print("=============")
        print(" Task Manager")
        print("=============")

    def add_task(self, project):
        title = input("Task: ")
        priority = input("Priority: ")
        next_action = input("Next action: ")
        notes = input("Notes: ")

        self.manager.add_task(
            project=project,
            task=title,
            priority=priority,
            notes=notes,
            next_action=next_action,
        )

    def edit_task(self, project, task_id):
        title = input("Task (Leave blank to skip): ") or None
        priority = input("Priority (Leave blank to skip): ") or None
        next_action = input("Next action (Leave blank to skip): ") or None
        notes = input("Notes (Leave blank to skip): ") or None
        status = input("Status (Leave blank to skip): ") or None
        updates = {}
        if title:
            updates["Task"] = title
        if priority:
            updates["Priority"] = priority
        if next_action:
            updates["Next_action"] = next_action
        if notes:
            updates["Notes"] = notes
        if status:
            updates["Status"] = status
        if updates:
            self.manager.update_task(
                project, task_id, updates
            )  # This needs updates in manager and prolly storage.
        else:
            print("No changes made.")

    def create_project(self):
        name = input("Give project name\n>")
        if len(name) >= 3:
            self.manager.create_project(name)

    def show_menu(self, title, options):
        self.print_logo()
        print(title)
        print()

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
            # Add divider for projcets menu..
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
                    "View task details",
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
                self.manager.update_task(
                    task["Project"],
                    task["ID"],
                    {
                        "Status": "Completed",
                        "Completed": datetime.now().strftime("%d-%m-%Y"),
                    },
                )
                print("Task marked as completed.")
                return

            elif choice == 3:
                self.edit_task(task["Project"], task["ID"])
                return

            elif choice == 4:
                self.manager.delete_task(task["Project"].task["ID"])
                return

            elif choice == 5:
                return

    def show_tasks_menu(self, project):
        while True:
            tasks = self.manager.get_tasks(project)

            if not tasks:
                print("No tasks.")
                input("Press Enter...")
                return

            task_titles = [task["Task"] for task in tasks]
            task_titles.append("Back")

            choice = self.show_menu("Tasks", task_titles)

            if choice == len(task_titles):
                return

            task = tasks[choice - 1]
            self.show_task_menu(task)

    def show_project_menu(self, project):
        while True:
            choice = self.show_menu(
                project,
                [
                    "View Tasks",
                    "Add Task",
                    "Rename Project",
                    "Delete Project",
                    "Back",
                ],
            )

            if choice == 1:
                self.show_tasks_menu(project)

            elif choice == 2:
                self.add_task(project)

            elif choice == 3:
                # Not manager, but self rename -> then call manager to updated project.
                self.manager.rename_project(project)

            elif choice == 4:
                self.manager.delete_project(project)
                return

            elif choice == 5:
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
        while True:
            choice = self.show_menu("Main Menu", MAIN_MENU)

            if choice == 1:
                self.show_projects_menu()

            elif choice == 2:
                return
