import re




text='How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
result = re.findall(R'\\wwood\+\?', text)
print('Список всех упоминаний шаблона:', result)