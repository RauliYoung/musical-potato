from storage import ExcelStorage
from task_manager import TaskManager
from cli import CLI
from sqlite_storage import SQLiteStorage

storage = ExcelStorage()
manager = TaskManager(storage)
cli = CLI(manager)
cli.run()

storage = SQLiteStorage()
storage.create_table()
