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

  opcao = input("Choose an Option: ")

  if opcao == "1":
    print("\n=== NEW TASK ===")
    title = (input("Type the name task: "))
    description = (input("Type the description task: "))
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

  elif opcao == "2":
    print ("\n=== UPDATE OR DELETE TASK ===")
    print ("\n1. Update Task")
    print ("2. Delete Task")
    
    update = int(input("\nChoose your option: ")) 
    if update == 1:
      print ("\n=== ALL TASKS ===\n")
      for item in info:
        print (f"{item}") 
      
      while True:  
        task_id = int(input("\nType the ID of the task you want to update: "))
        
        for item in info:              
          if item["id"] == task_id:
            item["title"] = input("\nType the new name task: ")
            item["description"] = input("Type the new description task: ")
            item["status"] = input("Type the new status task (todo, doing, done): ")
            item["updatedAt"] = datetime.now().isoformat()
            print("Task updated successfully!")

            print(f"\n=== ALL TASKS ===\n")
            for item in info:
              print(f"{item}")
            
            print("\n0. Back to menu")
            back = int(input("\nChoose your option: "))
            if back == 0:
              break
          
        else:
          print("Task not found. Type a valid ID.")
          continue
        break
              
    if update == 2:  
      print("\n=== DELETE TASK ===")
      print (f"\n=== ALL TASKS ===\n{info}")
      info.remove(item)
      print("Task deleted successfully!")
  
  elif opcao == "3":
    print("\n=== ALL TASKS ===")
    for item in info:
      print(f"{item}")

  elif opcao == "4":
    print("Exiting the program...")
    break
  
  else:
    print("\nInvalid option. Please choose a valid option.")