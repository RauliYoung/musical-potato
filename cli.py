class CLI:
    def __init__(self, manager):
        self.manager = manager

    # manager CRUD for the tasks..
    def print_logo(self):
        print("=============")
        print("Task Manager ")
        print("=============")

    def show_menu(self):
        self.print_logo()
        while True:
            print("1. Projects")
            print("2. Quit")
            print("\n")
            choice = input(">")
            if not self.input_handler(choice):
                break

    def run(self):
        self.show_menu()

    def input_handler(self, choice: str):
        # Think how actions could be made...
        actions = {"1": self.manager, "2": self.quit, "3": "", "4": "", "5": ""}

        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Invalid choice")
            return True
