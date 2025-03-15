import sys
import json

operator = sys.argv[1]
argument = sys.argv[2] if len(sys.argv) > 2 else None
comment = sys.argv[3] if len(sys.argv) > 3 else None

def getJson():
    pass

def createJson():
    pass

def add(argument):
    pass

def delete(argument):
    pass


def update(argument):
    pass

def mark(argument):
    pass

def list(argument):
    pass

def main():
    match operator:
        case "add":
            add(argument)
        case "update":
            pass
        case "delete":
            pass
        case "mark ":
            add(argument)
        case "list":
            pass
        case _:
            print("Invalid operator!")
            


if __name__ == '__main__':
  main()

