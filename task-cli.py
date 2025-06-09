import sys
import os
import json
from datetime import date

file_path = "sample.json"

operator = sys.argv[1]
argument = sys.argv[2] if len(sys.argv) > 2 else None
comment = sys.argv[3] if len(sys.argv) > 3 else None

desc = None
status = None
created = str(date.today())
updated = None

json_arr = []

def loadJson(file_path: str) -> list[dict]:
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return []
    else:
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    print("JSON data is not a list.")
                    return []
            except json.JSONDecodeError:
                print("Error decoding JSON.")
                return []

def createJson(argument):
    json_arr = loadJson(file_path)

    desc = argument
    status = 'Working'
    updated = str(date.today())

    content = {
        'status': status,
        'createdAt': created,
        'updatedAt': updated
    }

    template = {
        'id': len(json_arr) + 1,
        'desc': desc,
        'contents': content
    }

    json_arr.append(template)

    with open(file_path, "w") as file:
        json.dump(json_arr, file, indent=4)

def add(task_id: int, comment: str = None):
    json_arr = loadJson(file_path)
    for item in json_arr:
        if item['id'] == task_id:
            if comment:
                item['contents']['comment'] = comment
            item['contents']['updatedAt'] = str(date.today())
            break
    else:
        print(f"No task found with ID: {task_id}")

def delete(task_id: int):
    json_arr = loadJson(file_path)
    # Remove the task with the specified ID
    json_arr = [item for item in json_arr if item['id'] != task_id]
    
    # Reassign IDs to ensure they are sequential
    for index, item in enumerate(json_arr, start=1):
        item['id'] = index
    
    with open(file_path, "w") as file:
        json.dump(json_arr, file, indent=4)


def update(argument):
    json_arr = loadJson(file_path)
    task_id, new_desc = argument.split(',', 1)
    for item in json_arr:
        if item['id'] == int(task_id):
            item['desc'] = new_desc.strip()
            item['contents']['updatedAt'] = str(date.today())
            break
    with open("sample.json", "w") as file:
        json.dump(json_arr, file)

def mark(argument):
    pass

def listJson(task_id=None):
    json_arr = loadJson(file_path)
    if not json_arr:
        print("No tasks found.")
    else:
        if task_id is None:
            # List all tasks with Title + ID
            for item in json_arr:
                try:
                    print(f"Title: {item['desc']}, ID: {item['id']}")
                except (KeyError, TypeError):
                    print("Invalid task format.")
        else:
            # List detailed information for the task with the given ID
            for item in json_arr:
                try:
                    if item['id'] == task_id:
                        print(f"ID: {item['id']}, Description: {item['desc']}, Status: {item['contents']['status']}, Created At: {item['contents']['createdAt']}, Updated At: {item['contents']['updatedAt']}")
                        break
                except (KeyError, TypeError):
                    print("Invalid task format.")
            else:
                print(f"No task found with ID: {task_id}")
def main():
    match operator:
        case "add":
            createJson(argument)
        case "update":
            pass
        case "delete":
            if argument and argument.isdigit():
                task_id = int(argument)
                listJson(task_id)
                confirmation = input(f"Are you sure you want to delete task ID {task_id}? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    delete(task_id)
                    print(f"Task ID {task_id} has been deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid task ID for deletion.")
        case "mark":
            if argument and argument.isdigit():
                add(int(argument), comment)
            else:
                print("Invalid task ID for marking.")
        case "list":
            if argument and argument.isdigit():
                listJson(int(argument))
            else:
                listJson()
        case _:
            print("Invalid operator!")

if __name__ == '__main__':
  main()

