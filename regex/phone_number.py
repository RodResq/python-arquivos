import re
# Criando grupos com () em regex
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242')
print(f"Somente Codigo de area: {mo.group(1)}")
print(f"Somente Numero telefone: {mo.group(2)}")
print(f'Phone number complet found: ' + mo.group())

# Obtendo todos os grupos de uma vez
print(f"Todos os grupos de uma vez: {mo.groups()}")

area_code, phone_number = mo.groups()
print(f"Codigo de area {area_code}")
print(f"Phone number: {phone_number}")

# Escapando caracter () em regex
phone_number_regex2 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo2 = phone_number_regex2.search('My number is  (415)-555-4242')
print(f"Codigo de area com parenteses: {mo2.group(1)}")
print(f"Apenas numero de telefone: {mo2.group(2)}")

# Correspodencia opcional com o "?"
phone_number_regex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phone_number_regex2.search('My number is  415-555-4242')
print(f"Codigo como opcional, caso positivo: {mo3.group()}")
mo4 = phone_number_regex2.search('My number is  555-4242')
print(f"Codigo como opcional, caso negativo: {mo4.group()}")

# Metodo search() retorna somente primeira instancia correspondente a regex
phone_number_regex3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo5 = phone_number_regex3.search('cell: 415-555-9999 Work: 212-555-0000')
print(f"Retorna somente a primeira instancia encontrada: {mo5.group()}")

phone_number_regex4 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo6_list = phone_number_regex3.findall('cell: 415-555-9999 Work: 212-555-0000')
print(f"Metodo findall() retorna uma lista correspondente a regex: {mo6_list}")

# Metodo findall() com grupo na regex e retonado uma lista de tuplas
phone_number_regex_tupla = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # com grupos
mo7_list = phone_number_regex_tupla.findall('cell: 415-555-9999 Work: 212-555-0000')
print(f"Metodo findall() retorna uma lista de tuplas correspondente a regex: {mo7_list}")
