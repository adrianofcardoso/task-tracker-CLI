import json
from datetime import datetime
now = datetime.now()
format_date = now.strftime("%Y-%m-%d %H:%M:%S")
info = []

while True:

  print("\n=== MENU DE TAREFAS ===")
  print("1. Add Task")
  print("2. Update or Delete Task")
  print("3. List Status Tasks")
  print("4. Exit")

  opcao = int(input("Choose an Option: "))

  if opcao == 1:
    print("\n=== NEW TASK ===")
    title = (input("Type the name task: "))
    description = (input("Type the description task: "))
    status = "todo" 
    novo_id = len(info) + 1
    print(f"Task added successfully! (ID:{novo_id})")
    
    info.append({
    "id": novo_id,
    "title": title,
    "description": description,
    "status": status,
    "createdAt": format_date
    })

  elif opcao == 2:
    while True:
      print ("\n=== UPDATE OR DELETE TASK ===")
      print ("0. Back to Main Menu")
      print ("1. Update Task")
      print ("2. Delete Task")
      
      try:
        option_id = int(input("\nChoose your option: "))
      except ValueError:
        print("Invalid input. Please enter a number.")
        continue
      #criar condição de linha vazias para não dar erro de index 
      
      if option_id == 0:
        break
      
      elif option_id == 1 or option_id == 2:
        print ("\n=== ALL TASKS ===\n")
        
        if len(info) == 0:
          print("No tasks found or list is empty. Add a task to the list.")
          continue
        
        for i in info:
          print (f"{i}")
    
        while True:
          try:
            task_id = int(input(f"\nType the ID of the task you want to {('update' if option_id == 1 else 'delete')}: "))
          except ValueError:
            print("Invalid input. Please enter a number.")
            continue
          task_found = False
          task_to_modify = None 
          for i in info:
            if i["id"] == task_id:
              task_found = True
              task_to_modify = info.index(i)
              break
          if task_found:
            break
          else:
            print("Task not found. Please enter a valid task ID.")
      
        if option_id == 1: 
          for i in info:
            if i["id"] == task_id:
              i["title"] = input("\nType the new name task: ")
              i["description"] = input("Type the new description task: ")
              i["status"] = input("Type the new status task (todo, in-progress, done): ")
              i["updatedAt"] = format_date
              print("Task updated successfully!")
              print ("\n=== ALL TASKS ===\n")
          for i in info:
            print (f"{i}")
          continue
      
        elif option_id == 2:  
          print("\n=== DELETE TASK ===")
          print (f"\n=== ALL TASKS ===\n{i}")
          info.remove(i)
          counter = 1
          for i in info:
            i ["id"] = counter
            counter += 1
          print("Task deleted successfully!")
          break
    
      print("\nInvalid option. Please choose a valid option.")
      continue
    
  elif opcao == 3:
    while True:
      print("\n=== LIST STATUS TASKS ===")
      print("0. Back to Main Menu")
      print("1. List All Tasks")
      print("2. List Only Tasks To Do ")
      print("3. List Only Tasks In Progress ")
      print("4. List Only Tasks Done ")
      
      try:
        option_list = int(input("Choose an option: "))
      except ValueError:
        print("Invalid input. Please enter a number.")
        continue
          
      if len(info) == 0:
          print("\n=== LIST STATUS TASKS ===")
          print("No tasks found or list is empty. Add a task to the list.")
          break 
      
      try:
        if option_list == 0:
          break 

        for t in info:
          if option_list == 1:
            print(f"{t}")
          elif option_list == 2 and t ["status"] == "todo":
            print(f"{t}")
          elif option_list == 3 and t ["status"] == "in-progress":
            print(f"{t}")
          elif option_list == 4 and t ["status"] == "done":
            print(f"{t}")
      except ValueError:
        print("\nInvalid option. Please choose a valid option.")
        continue
        
  elif opcao == 4:
    print("Exiting the program...")
    break
  
  else:
    print("\nInvalid option. Please choose a valid option.")