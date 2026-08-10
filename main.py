from storage import ExcelStorage
from task_manager import TaskManager
from cli import CLI

storage = ExcelStorage()
manager = TaskManager(storage)
cli = CLI(manager)
cli.run()

# manager.add_task(
#     project="Task Manager",
#     task="Write README",
#     priority="High",
#     notes="Remember where you left off.",
#     next_action="Go to bed.",
# )
