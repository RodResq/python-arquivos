import re

hero_regex = re.compile(r'Batman|Tina Fey')
mo = hero_regex.search('Batman and Tina Fey')
mo2 = hero_regex.search('Tina Fey and Batman')
print(f"Hero: {mo.group()}")
print(f"Hero 2: {mo2.group()}")

# Usando Prefixo
options = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = options.search('Batmobile lost a whel')
print(f"Correspodencia: {mo3.group()}")
print(f"Correspondecia dentro do grupo: {mo3.group(1)}")
