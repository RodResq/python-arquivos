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
