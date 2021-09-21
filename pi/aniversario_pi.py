file_digits = 'pi_million_digits.txt'

with open(file_digits, 'r') as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
print(f'{pi_string[:50]}...')
aniversario = input('Digete sua data de nascimento no formato mmddyy: ')
if aniversario in pi_string:
    print(f'Seu aniversario esta contido no primeiro milhao do numero pi: {aniversario}')
else:
    print('Seu aniversario nao esta contido no primeiro milhao do numero pi!')
