import pandas as pd
from pathlib import Path


class ExcelStorage:
    COLUMNS = [
        "ID",
        "Project",
        "Task",
        "Status",
        "Priority",
        "Created",
        "Started",
        "Completed",
        "Next Action",
        "Notes",
    ]

    # TODO: Add handling so that overwrites do not destroy, now it is apparently ok. could be by project, so sheet per project.
    def __init__(self, filename="taskhandler.xlsx"):
        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir / "data"
        data_dir.mkdir(parents=True, exist_ok=True)

        self.workbook = data_dir / filename

        self.create_workbook()

    def create_workbook(self):
        if self.workbook.exists():
            return

        df = pd.DataFrame(columns=self.COLUMNS)

        with pd.ExcelWriter(self.workbook, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)

    def load_tasks(self, project):
        return pd.read_excel(self.workbook, sheet_name=project)

    def save_tasks(self, tasks: pd.DataFrame):
        tasks.to_excel(self.workbook, sheet_name="Tasks", index=False)

    def get_projects(self):
        xl = pd.ExcelFile(self.workbook)
        return xl.sheet_names

    def create_project(self, name):
        with pd.ExcelWriter(self.workbook, engine="openpyxl", mode="a") as writer:
            df = pd.DataFrame(columns=self.COLUMNS)
            df.to_excel(writer, sheet_name=name, index=False)
