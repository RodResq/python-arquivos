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

# Correspodencia opcional com o "?"
bat_regex = re.compile(r'Bat(wo)?man')
mo4 = bat_regex.search('The adventure of Batman')
print(f"The men: {mo4.group()}")

mo5 = bat_regex.search('The adventure of Batwoman')
print(f"The woman: {mo5.group()}")

# Correspondencia de zero ou mais vezes
bat_regex = re.compile(r'Bat(wo)*man')
mo5 = bat_regex.search('The adventure of Batman')
print(f"The men,  Correspondencia de zero vezes: {mo5.group()}")

mo7 = bat_regex.search('The adventure of Batwoman')
print(f"The woman, Correspondencia 1 veze: {mo7.group()}")

mo6 = bat_regex.search('The adventure of Batwowowowowoman')
print(f"The woman, Correspondencia 4 vezes: {mo6.group()}")

# Correspondencia de uma ou mais vezes
bat_regex = re.compile(r'Bat(wo)+man')
mo8 = bat_regex.search('The adventure of Batwoman')
print(f"The men,  Correspondencia de uma vez: {mo8.group()}")

mo9 = bat_regex.search('The adventure of Batwowowowowoman')
print(f"The woman, Correspondencia 4 vezes: {mo9.group()}")

mo10 = bat_regex.search('The adventure of Batman')
resultado = mo10 is None
print(f"Sem Correspondencia, minimo 1 vez: {resultado}")

# Correspondencia e repeticoes de um numero de vezes especificas usando chave "{}"
ha_regex = re.compile(r'(Ha){3}')
mo11 = ha_regex.search('HaHaHa')
print(f"Numero especifico de vezes repetidas: {mo11.group()}")
mo12 = ha_regex.search('Ha')
result_ha = mo12 is None
print(f"\"Ha\" Sem correspondencia: {result_ha}")

# Correspondencias greedy(gulosa) e nongreedy(nao gulosa)
greedy_regex = re.compile(r'(Ha){3,5}')
mo13 = greedy_regex.search('HaHaHaHaHa')
print(f"Correspondencia greedy: {mo13.group()}")

nongreedy_regex = re.compile(r'(Ha){3,5}?')
mo14 = nongreedy_regex.search('HaHaHa')
print(f"Correspondencia nongreedy: {mo14.group()}")







