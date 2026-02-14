import json
from datetime import datetime
info = []
id = 0

while True:

  print("\n=== MENU DE TAREFAS ===")
  print("1. Add Task")
  print("2. Update or Delete Task")
  print("3. List All Tasks")
  print("4. Exit")

  opcao = input("Choose an Option:")

  if opcao == "1":
    print("\n=== NEW TASK ===")
    id += 1
    title = (input("Type the name task:"))
    description = (input("Type the description task:"))
    status = "todo" 
    
    info.append({
    "id": id,
    "title": title,
    "description": description,
    "status": status,
    "createdAt": datetime.now().isoformat()
    })

    print(f"Task added successfully! (ID:{id})")

  if opcao == "2":
    print ("\n=== UPDATE OR DELETE TASK ===")
    task_id = int(input("Type the ID task:"))
    
    if task_id == id:
      print("1. Update Task")
      print("2. Delete Task")
    else:
      print("Task not found.")
      continue
  
  elif opcao == "3":
    print("\n=== ALL TASKS ===")
    for i in info:
      print(i, "->", {info})

  if opcao == "4":
    print("Exiting the program...")
    break

  else:
    print("Invalid option. Please try again.")

