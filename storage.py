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
            df.to_excel(writer, sheet_name="Tasks", index=False)

    def load_tasks(self):
        return pd.read_excel(self.workbook, sheet_name="Tasks")

    def save_tasks(self, tasks: pd.DataFrame):
        tasks.to_excel(self.workbook, sheet_name="Tasks", index=False)