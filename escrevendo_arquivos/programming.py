filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('A love programming! \n')

# Concatenado arquivos
try:
    with open(filename, 'a') as file_object:
        file_object.write("I love finding meaning in large datasets. \n")
        file_object.write("A love creating apps that can run in a browser. \n")
except FileNotFoundError:
    print("Arquivo nao encontrado!")
