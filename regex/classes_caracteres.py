import re

xmas_regex = re.compile(r'\d+\s\w+')
list = xmas_regex.findall('12 drummes, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(f"Lista da regex: {list}")

#  Criando a propria classe de reges com colchetes "[]"
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_list = vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
print(f"Classe somente com vogais: {vowel_list}")

# Criando correspondencia negativa na classe
nagative_vowel_regex = re.compile(r'[^aeiouAEIOU]')
non_vowel_list = nagative_vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
print(f"Classe negativa sem vogais: {non_vowel_list}")

# Comecando com uma palavra especifica
begin_with_hello = re.compile(r'^Hello')
mo = begin_with_hello.search('Hello World!')
print(f"Regex com ^: {mo}")
mo1 = begin_with_hello.search('He said hello!')
print(f"Nao corrependicia: {mo1}")

# Terminando com caracter numerico de 0 - 9 ($)
end_with_number = re.compile(r'\d$')
mo2 = end_with_number.search('Your number is 42')
print(f"Correspondencia terminando com numero: {mo2}")
mo3 = end_with_number.search('Ypu number is forty two')
print(f"Sem Correspondencia terminando com numero: {mo3}")

# Expressoes que comecam e terminam com um ou mais caracteres nummericos
start_end_number = re.compile(r'^\d+$')
mo4 = start_end_number.search('1234567890')
print(f"Correspondencia comecando e terminando com numero: {mo4}")
mo5 = start_end_number.search('1234xyz5647890')
print(f"Nao Correspondencia comecando e terminando com numero(letra no meio): {mo5}")
mo6 = start_end_number.search('1234   5647890')
print(f"Nao Correspondencia comecando e terminando com numero(spaco no meio): {mo6}")

# Caracter Corringa
corringa_regex = re.compile(r'.at')
at_regex_list = corringa_regex.findall('The cat in the hat sat on the flat mat.')
print(f"Correspondencia com carcter coringa (.): {at_regex_list}")

# Correspondendo tudo usando ponto e asterisco (.*)
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo7 = name_regex.search('First Name: Bob Last Name: Lee')
print(f"Correspondendo tudo usando ponto e asterisco (.*) grupo 1: {mo7.group(1)}")
print(f"Correspondendo tudo usando ponto e asterisco (.*) grupo 2: {mo7.group(2)}")

# Correspondendo ao caracter quebra de linha com re.DOTALL
no_new_line_regex = re.compile(r'.*')
mo8 = no_new_line_regex.search('Server the public trust. \nProtect the innocent.\nEphold the law').group()
print(f"Correspondendo ao caracter quebra de linha sem re.DOTALL: {mo8}")

no_new_line_regex = re.compile(r'.*', re.DOTALL)
mo9 = no_new_line_regex.search('Server the public trust. \nProtect the innocent.\nEphold the law').group()
print(f"Correspondendo ao caracter quebra de linha com re.DOTALL: {mo9}")
