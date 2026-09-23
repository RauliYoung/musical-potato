from pathlib import Path
import sqlite3


class SQLiteStorage:
    def __init__(self, filename="tasks.db"):
        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir / "data"
        data_dir.mkdir(exist_ok=True)

        self.db_path = data_dir / filename
        self.__db = sqlite3.connect(self.db_path)

    def create_table(self):
        self.__db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                ID INTEGER PRIMARY KEY,
                Project TEXT NOT NULL,
                Task TEXT NOT NULL,
                Status TEXT NOT NULL,
                Priority TEXT NOT NULL,
                Created TEXT NOT NULL,
                Started TEXT,
                Completed TEXT,
                "Next Action" TEXT,
                Notes TEXT
            )
        """)
        self.__db.commit()
