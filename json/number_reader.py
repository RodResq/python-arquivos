import json

filename = 'numbers.json'

try:
    with open(filename, 'r') as file_object:
        readers = json.load(file_object)
except FileNotFoundError:
    print("Arquivo nao encontrado")
else:
    print(readers)
