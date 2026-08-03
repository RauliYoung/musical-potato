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
        tasks = self.storage.load_tasks()

        today = datetime.now().strftime("%d-%m-%Y")

        if tasks.empty:
            next_id = 1
        else:
            next_id = tasks["ID"].max() + 1

        new_task = {
            "ID": next_id,
            "Project": project,
            "Task": task,
            "Status": "Todo",
            "Priority": priority,
            "Created": today,
            "Started": None,
            "Completed": None,
            "Next Action": next_action,
            "Notes": notes or "",
        }

        tasks.loc[len(tasks)] = new_task
        self.storage.save_tasks(tasks)

    def delete_task(self, ids: int | list[int]):
        tasks = self.storage.load_tasks()

        if isinstance(ids, list):
            tasks = tasks[~tasks["ID"].isin(ids)]
        else:
            tasks = tasks[tasks["ID"] != ids]

        self.storage.save_tasks(tasks)

    def update_task(self, task_id: int):
        tasks = self.storage.load_tasks()

        task = tasks[tasks["ID"] == task_id]

        # TODO: implement updating

        self.storage.save_tasks(tasks)