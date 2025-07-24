# Simple CLI TODO
tasks = []

while True:
    command = input("Enter [add/show/exit]: ").strip().lower()

    if command == 'add':
        task = input("Enter task: ")
        tasks.append(task)
    elif command == 'show':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif command == 'exit':
        print("Exiting TODO app.")
        break
    else:
        print("Invalid command.")
