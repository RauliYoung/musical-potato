import pandas as pd
from pathlib import Path
from datetime import datetime

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
        
BASE_DIR = Path(__file__).resolve().parent
WORKBOOK = BASE_DIR / "data" / "taskhandler.xlsx"

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

def create_workbook():

    WORKBOOK.parent.mkdir(parents=True, exist_ok=True)

    if WORKBOOK.exists():
        return

    df = pd.DataFrame(columns=COLUMNS)

    with pd.ExcelWriter(WORKBOOK, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Tasks", index=False)

def load_tasks():
    return pd.read_excel(WORKBOOK, sheet_name="Tasks")

def save_tasks(tasks: pd.DataFrame):
    tasks.to_excel(WORKBOOK, sheet_name="Tasks", index=False)
#Remove notes later..
def add_task(project:str, task:str, priority:str,notes:str,next_action = "" ):
    tasks = load_tasks()
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
    new_df = pd.DataFrame([new_task])
    tasks = pd.concat([tasks,new_df], ignore_index=True)
    save_tasks(tasks)

def update_task(ID:int):
    tasks = load_tasks()
    task = tasks[tasks.ID == ID]
    # How to update task, with prompt or ? with arguments? or
    pass

def delete_task(ids:int | list[int]):
    tasks = load_tasks()
    if isinstance(ids,list):
        tasks = tasks[~tasks["ID"].isin(ids)]
    else:
        tasks = tasks[tasks["ID"] != ids]
    save_tasks(tasks)
    pass