import task_manager

def main():
    task_manager.create_workbook()
    task_manager.add_task(
        project="Task Manager",
        task="Write README so you remember where you left.",
        priority="High",
        next_action="Go to bed.",
        notes = "Remember to think for yourself, you are not always in a terrible hurry."
  
    )
    task_manager.update_task(2)
    # task_manager.delete_task(4)
    task_manager.delete_task([2,3,4])
    # print(task_manager.load_tasks())
    task_manager.delete_task(999)
if __name__ == "__main__":
    main()