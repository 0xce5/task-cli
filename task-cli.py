import sys
import os
import json
from datetime import date

filepath = "sample.json"

operator = sys.argv[1]
argument = sys.argv[2] if len(sys.argv) > 2 else None
comment = sys.argv[3] if len(sys.argv) > 3 else None

desc = None
status = None
created = str(date.today())
updated = None

json_arr = []

def loadJson(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return json_arr
    else:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                json_arr = data if isinstance(data, list) else [data]
        except json.JSONDecodeError:
            json_arr = []

        return json_arr

def createJson(argument):
    json_arr = loadJson(filepath)

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

    with open("sample.json", "w") as file:
        json.dump(json_arr, file)

def add(argument):
    json_arr = loadJson(filepath)
    for item in json_arr:
        if item['id'] == int(argument):
            item['contents']['comment'] = comment
            item['contents']['updatedAt'] = str(date.today())
            break
    with open("sample.json", "w") as file:
        json.dump(json_arr, file)

def delete(argument):
    json_arr = loadJson(filepath)
    json_arr = [item for item in json_arr if item['id'] != int(argument)]
    with open("sample.json", "w") as file:
        json.dump(json_arr, file)


def update(argument):
    json_arr = loadJson(filepath)
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

def list(argument):
    pass

def main():
    match operator:
        case "add":
            if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
                createJson(argument)
            else:
                add(argument)
        case "update":
            pass
        case "delete":
            pass
        case "mark ":
            add(argument)
        case "list":
            print(loadJson(filepath))
        case _:
            print("Invalid operator!")
            


if __name__ == '__main__':
  main()

