from datetime import datetime


class TaskManager:
    def __init__(self, storage):
        self.storage = storage

    def add_task(
        self,
        project: str,
        task: str,
        priority: str,
        notes: str,
        next_action: str = "",
    ):
        tasks = self.storage.load_tasks(project)

        today = datetime.now().strftime("%d-%m-%Y")

        if tasks.empty:
            next_id = 1
        else:
            next_id = tasks["ID"].max() + 1

        new_task = {
            "ID": next_id,
            "Project": project,
            "Task": task,
            "Status": "Todo",  # Figure out a statussystem, also state of task? How to do this.
            "Priority": priority,
            "Created": today,
            "Started": None,  # Add handling to start taskk
            "Completed": None,  # Add handling to complet task
            "Next Action": next_action,
            "Notes": notes or "",
            # Calculate duration from start to finnish, this could be an interesting task..
        }

        tasks.loc[len(tasks)] = new_task
        self.storage.save_tasks(tasks, project)

    def complete_task(self, project, task_id):
        tasks = self.storage.load_tasks(project)
        tasks = tasks.loc[tasks["ID"] == task_id, "Completed"] = (
            datetime.now().strftime("%d-%m-%Y")
        )
        self.storage.save_tasks(tasks, project)
        # Add some kind of better handling so that it gives some data from started and ended and so on.

    def delete_task(self, project, task_id):
        tasks = self.storage.load_tasks(project)
        tasks = tasks[tasks["ID"]] != task_id
        self.storage.save_tasks(tasks, project)

    def update_task(self, project, task_id, updates: dict) -> None:
        tasks = self.storage.load_tasks(project)
        for key, value in updates.items():
            tasks.loc[tasks["ID"] == task_id, key] = value
        self.storage.save_tasks(tasks, project)

    def get_tasks(self, project):
        df = self.storage.load_tasks(project)
        return df.to_dict(orient="records")

    def get_projects(self) -> list[str]:
        return self.storage.get_projects()

    def create_project(self, project_name):
        name = project_name
        self.storage.create_project(name)
