import pandas as pd
from storage import ExcelStorage


class TaskManager:
    def __init__(self, storage: ExcelStorage):
        self.storage = storage

    def add_task(self, project: str, task_data: dict) -> None:
        """Add a task to a project."""
        tasks = self.storage.load_tasks(project)
        new_task = pd.DataFrame([task_data])
        tasks = pd.concat([tasks, new_task], ignore_index=True)
        self.storage.save_tasks(tasks, project)

    def update_task(self, project: str, task_id: int, updates: dict) -> None:
        """Update a task in a project."""
        tasks = self.storage.load_tasks(project)
        for key, value in updates.items():
            tasks.loc[tasks["ID"] == task_id, key] = value
        self.storage.save_tasks(tasks, project)

    def delete_task(self, project: str, task_id: int) -> None:
        """Delete a task from a project."""
        tasks = self.storage.load_tasks(project)
        tasks = tasks[tasks["ID"] != task_id]
        self.storage.save_tasks(tasks, project)

    def get_tasks(self, project: str) -> pd.DataFrame:
        """Get all tasks from a project."""
        return self.storage.load_tasks(project)

    def get_projects(self) -> list:
        """Get all projects."""
        return self.storage.get_projects()

    def create_project(self, name: str) -> None:
        """Create a new project."""
        self.storage.create_project(name)
