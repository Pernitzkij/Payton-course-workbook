import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match(r'wo', text)
print('Поиск шаблона в начале строки:', result)
result = re.search(r'wo', text)
print('Поиск первого найденного совпадения по шаблону:', result)
print('Содержимое найденной подстроки:', result.group())
print('Начальная позиция:', result.start())
print('Конечная позиция:', result.end())
result = re.findall(r'wo', text)
print('Список всех упоминаний шаблона:', result)
result = re.sub(r'wo', 'ZAMENA', text)
print('Текст после замены:', result)

# 'Поиск шаблона в начале строки: None'
#
# 'Поиск первого найденного совпадения по шаблону: <re.Match object; span=(9, 11), match='wo'>'
#
# 'Содержимое найденной подстроки: wo'
#
# 'Начальная позиция: 9'
#
# 'Конечная позиция: 11'
#
# 'Список всех упоминаний шаблона: ['wo', 'wo', 'wo', 'wo', 'wo']'
#
# 'Текст после замены: How much ЗАМЕНАod ЗАМЕНАuld a ЗАМЕНАodchuck chuck if a ЗАМЕНАodchuck could chuck ЗАМЕНАod?'
