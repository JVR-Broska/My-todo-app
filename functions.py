FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Tries to get the saved todo list. Create
    a new file in case there is n other. """
    try:
        with open(filepath, 'r') as file_local:
            todos_local =  file_local.readlines()
            return todos_local
    except:
        print("Creatin a 'Todo' file...")
        local_file = open(filepath, 'w')
        local_file.close()
        return []


def write_todos(todos_arg, filepath=FILEPATH):
    """ Save the edited todo list """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


if __name__ == "__name__":
    print("Hello")
    print()