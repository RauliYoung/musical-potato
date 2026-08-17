import pandas as pd
from openpyxl import load_workbook
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
        """Create workbook with initial sheet using openpyxl."""
        if self.workbook.exists():
            return

        wb = load_workbook()
        ws = wb.active
        ws.title = "Welcome To Task Hassler"
        ws.append(self.COLUMNS)
        wb.save(self.workbook)

    def load_tasks(self, project: str) -> pd.DataFrame:
        """Load tasks from specific project sheet."""
        return pd.read_excel(self.workbook, sheet_name=project)

    def save_tasks(self, tasks: pd.DataFrame, project: str) -> None:
        """Save tasks to specific project sheet."""
        with pd.ExcelWriter(self.workbook, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            tasks.to_excel(writer, sheet_name=project, index=False)

    def get_projects(self) -> list:
        """Get list of all project sheet names."""
        xl = pd.ExcelFile(self.workbook)
        return [sheet for sheet in xl.sheet_names if sheet != "Welcome To Task Hassler"]

    def create_project(self, name: str) -> None:
        """Create new project sheet using openpyxl."""
        wb = load_workbook(self.workbook)
        if name not in wb.sheetnames:
            ws = wb.create_sheet(name)
            ws.append(self.COLUMNS)
            wb.save(self.workbook)
