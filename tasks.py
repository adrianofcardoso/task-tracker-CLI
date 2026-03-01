import json
from datetime import datetime
info = []

def current_date():
  '''
  Função para retornar a data e a hora atual da criação ou atualização da tarefa, formatada como "YYYY-MM-DD HH:MM:SS".
  '''
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def listar_tarefas (info):
  '''
  Função para listar as tarefas, formatando a saída em colunas e destacando o status "done" em verde e "in-progress" em vermelho.
  '''  
  w_id = len("id")
  w_title = len("title")
  w_description = len("description")
  w_status = len("status")
  w_createdAt = len("createdAt")
  w_updatedAt = len("updatedAt")

  for t in info:
    w_id = max (w_id, len(str(t.get("id", ""))))
    w_title = max (w_title, len(str(t.get("title", ""))))
    w_description = max(w_description, len(str(t.get("description", ""))))
    w_status = max(w_status, len(str(t.get("status", ""))))
    w_createdAt = max(w_createdAt, len(str(t.get("createdAt", ""))))
    w_updatedAt = max(w_updatedAt, len(str(t.get("updatedAt", ""))))

  RED = "\033[31m"
  GREEN = "\033[32m"
  RESET = "\033[0m"

  
  column = f"{'id':<{w_id}} | {'title':<{w_title}} | {'description':<{w_description}} | {'status':<{w_status}} | {'createdAt':<{w_createdAt}} | {'updatedAt':<{w_updatedAt}}"
  print("\n" + " TASKS LIST ".center(len(column), "="))
  print(column)
  print("-" * len(column))

  for t in info:
    status = t.get("status", "")

    if status == "done":
      colored_status = f"{GREEN}{status}{RESET}"
      status_col = colored_status + " " * (w_status - len(status))
    
    elif status == "in-progress":
      colored_status = f"{RED}{status}{RESET}"
      status_col = colored_status + " " * (w_status - len(status))
    
    else:
      status_col = f"{status:<{w_status}}"

    row = f"{str(t.get('id', '')):<{w_id}} | {str(t.get('title', '')):<{w_title}} | {str(t.get('description', '')):<{w_description}} | {status_col} | {str(t.get('createdAt', '')):<{w_createdAt}} | {str(t.get('updatedAt', '')):<{w_updatedAt}}"
    print(row)

  print("="*len(column))

def list_empty():
  '''
  Função para verificar se a lista de tarefas está vazia, exibindo uma mensagem apropriada caso não haja tarefas para listar.
  '''
  if not info:
    print("\nNo tasks found. Please add a task first.")
    return True
  return False

def new_task():
  '''
  Função para adicionar uma nova tarefa, solicitando ao usuário o título e a descrição da tarefa, e atribuindo um ID único e o status "todo" por padrão.
  '''
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
    "createdAt": current_date(),
    })

def update_task():
  '''
  Função para atualizar uma tarefa, solicitando ao usuário o ID da tarefa a ser atualizada e as informações a serem modificadas (título, descrição ou status).
  '''
  for t in info:
    if t["id"] == task_id:
        print("\n=== UPDATE TASK OPTIONS===")
        print("1. Update Task Title")
        print("2. Update Task Description")
        print("3. Update Task Title and Description")
        print("4. Update Task Status")

        try:
          update_option = int(input("\nChoose an option to update: "))
        except ValueError:
          print("Invalid input. Please enter a number.")
          return

        if update_option in [1, 2, 3, 4]: 
          if update_option == 1:
            t["title"] = input("\nType the new title task: ")
          elif update_option == 2:
            t["description"] = input("Type the new description task: ")
          elif update_option == 3:
            t["title"] = input("\nType the new title task: ")
            t["description"] = input("Type the new description task: ")
          elif update_option == 4:
            t["status"] = input("Type the new status task (todo, in-progress, done): ")
          t["updatedAt"] = current_date()
          print("Task updated successfully!")
          listar_tarefas(info)
        else:
          print("\nInvalid option. Please choose a valid option.")
          return

def delete_task():
  '''
  Função para deletar uma tarefa, solicitando ao usuário o ID da tarefa a ser deletada e removendo-a da lista de tarefas.
  '''
  for t in info:
    if t["id"] == task_id:
      info.remove(t)
      print("Task deleted successfully!")
      return
  
  print("Task not found. Please enter a valid task ID.")

while True:

  print("\n=== MENU DE TAREFAS ===")
  print("1. Add Task")
  print("2. Update or Delete Task")
  print("3. List Status Tasks")
  print("4. Exit")

  opcao = int(input("Choose an Option: "))

  if opcao == 1:
    new_task()

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
        #verificação de lista vazia para não dar erro de index e solicitar ao usuário para adicionar uma tarefa primeiro, caso a lista esteja vazia
        if list_empty():
          break
        else:
          listar_tarefas(info)
    
        #Verificação de ID para update ou delete, caso o ID não exista, solicitar novamente até que seja digitado um ID válido
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
          update_task()
          continue
        
        elif option_id == 2:  
          delete_task()
      
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
      
      try:
        if option_list == 0:
          break 

        if option_list == 1:
            listar_tarefas(info)

        for t in info:
          if option_list == 2 and t ["status"] == "todo":
            listar_tarefas([t])
          elif option_list == 3 and t ["status"] == "in-progress":
            listar_tarefas([t])
          elif option_list == 4 and t ["status"] == "done":
            listar_tarefas([t])
      except ValueError:
        print("\nInvalid option. Please choose a valid option.")
        continue
        
  elif opcao == 4:
    print("Exiting the program...")
    break
  
  else:
    print("\nInvalid option. Please choose a valid option.")