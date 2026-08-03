from storage import ExcelStorage
from task_manager import TaskManager


storage = ExcelStorage()
manager = TaskManager(storage)

manager.add_task(
    project="Task Manager",
    task="Write README",
    priority="High",
    notes="Remember where you left off.",
    next_action="Go to bed.",
)