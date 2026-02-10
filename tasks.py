import datetime

task_list = []
id_counter = 1

while True:

  print("\n=== MENU DE TAREFAS ===")
  print("1. Add Task")
  print("2. Update Task")
  print("3. Delete Task")
  print("4. List All Tasks")
  print("5. Exit")

  opcao = input("Choose an Option:")

  if opcao == "1":
    print("\n=== NEW TASK ===")
    task = (input("Type the name task: "))
    description = (input("Type the description task:"))
    status = "todo"

  elif opcao == "2":
    print ("\n=== UPDATE TASK ===")
    id_task_update = int(input("Type the id task to update:"))

  task_list.append ({
      "task": task,
      "description": description,
      "id": id_counter,
      "status": status,
      "createdAt": datetime.now(),
      "updatedAt": datetime.now()
    })
