import json
from datetime import datetime
info = []
id = 1

while True:

  print("\n=== MENU DE TAREFAS ===")
  print("1. Add Task")
  print("2. Update or Delete Task")
  print("3. List All Tasks")
  print("4. Exit")

  opcao = input("Choose an Option:")

  if opcao == "1":
    print("\n=== NEW TASK ===")
    title = (input("Type the name task: "))
    description = (input("Type the description task:"))
    status = "todo"
    id += 1 
    print(f"Task added successfully! (ID:{id})")
    
    info.append({
    "id": id,
    "title": title,
    "description": description,
    "status": status,
    "createdAt": datetime.now().isoformat()
    })


  if opcao == "2":
    print ("\n=== UPDATE OR DELETE TASK ===")
    task_id = int(input("Type the ID task:"))
    
    if task_id == id:
      print("1. Update Task")
      print("2. Delete Task")
    else:
      print("Task not found.")
      continue
  
  elif opcao == "4":
    print("\n=== ALL TASKS ===")
    for task in info:
      print(f"-> {info}")

  if opcao == "5":
    print("Exiting the program...")
    break

