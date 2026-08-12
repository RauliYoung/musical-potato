from storage import ExcelStorage
from task_manager import TaskManager
from cli import CLI

storage = ExcelStorage()
manager = TaskManager(storage)
cli = CLI(manager)
cli.run()
1
