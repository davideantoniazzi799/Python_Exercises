#Crea un programma che permette all'utente di:
#- aggiungere compiti
#- rimuovere compiti
#- visualizzare la lista

def add_to_do(a, task):
    a.append(task)

def remove_to_do(a, task):
    if task in a:
        a.remove(task)
        print("To-do removed.")
    else:
        print("No to-do found in the list.")

def print_to_do_list(a):
    if not a:
        print("Empty list at the moment.")
    else:
        for i, task in enumerate(a, start=1):
            print(f"{i}. {task}")

valid_commands = ["add", "rem", "pri", "exit"]
to_do_list = []

while True:
    user_request = input(
        "Type ADD, REM, PRI or EXIT:\n"
    ).lower()

    if user_request not in valid_commands:
        print("Wrong input. Type again.")
        continue

    if user_request == "exit":
        break

    if user_request == "pri":
        print_to_do_list(to_do_list)
        continue

    task = input("Indicate the task: ")

    if user_request == "add":
        add_to_do(to_do_list, task)

    elif user_request == "rem":
        if not to_do_list:
            print("Empty list at the moment.")
        else:
            remove_to_do(to_do_list, task)