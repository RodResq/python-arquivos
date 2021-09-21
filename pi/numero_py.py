with open('pi_digits.txt', 'r') as file_object:
    content = file_object.read()
    # print(content.rstrip())

# Lendo Linha a Linha
file_name = 'pi_digits.txt'

# with open(file_name, 'r') as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Armazenando linhas do arquivo em uma variavel

with open(file_name, 'r') as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string +=  line.strip()

print(pi_string)
print(len(pi_string))
