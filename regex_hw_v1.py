import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)


# # TODO 1: выполните пункты 1-3 ДЗ

# 1. Перенос Фамилии, Имени и Отчество человека в поля lastname, firstname и surname соответственно.

name_pattern = re.compile(r"(\w+)(\W*)?(\w+)(\W*)?(\w+)?")
name_substitution = r'\1,\3,\5'

for i in contacts_list[1:]:
    text = i[0] + ' ' + i[1] + ' ' + i[2]
    # print(text)
    result = name_pattern.sub(name_substitution, text.strip())
    result_list = result.split(',')
    i[0] = result_list[0]
    i[1] = result_list[1]
    i[2] = result_list[2]

# for new_i in contacts_list:
#     print(new_i)


# 2. Приведение всех телефонов в формат
# +7(999)999-99-99.
# +7(999)999-99-99 доб.9999 - Если есть добавочный номер.

phone_pattern = re.compile(
    r"(\+7|8)\s?\(?(\d{3})\)?(\s|[-])?(\d{3})(\s|[-])?(\d{2})(\s|[-])?(\d{2})(\s\(?(\S*)\s(\w*)\)?)?")
phone_substitution = r'+7(\2)\4-\6-\8 \10\11'
for column in contacts_list[1:]:
    phone_result = phone_pattern.sub(phone_substitution, column[-2])
    column[-2] = phone_result
    # print(phone_result)

# for new_format in contacts_list:
#     print(new_format)

# pprint(contacts_list)


# 3. Объединение всех дублирующиеся записи о человеке в одну.

new_contacts_list = contacts_list.copy()
count = 2

for contact in contacts_list[1:]:  # Переборка контактов в скиске контактов
    # print(contact)
    print(f"Ищу дубль контакта {contact[0]} {contact[1]}")
    search_contact_id = count
    for search_contact in contacts_list[count:]: # Переборка скиска контактов для поиска дублей
        search_contact_id += 1
        # print(f'Запись номер {search_contact_id}: {search_contact}')
        if contact[0] == search_contact[0] and contact[1] == search_contact[1]:
            print(f"Я нашёл дубль контакта {contact[0]} {contact[1]}")
            if contact[2] == '':
                new_contacts_list[count-2][2] = search_contact[2]
            if contact[3] == '':
                new_contacts_list[count-2][3] = search_contact[3]
            if contact[4] == '':
                new_contacts_list[count-2][4] = search_contact[4]
            if contact[5] == '':
                new_contacts_list[count-2][5] = search_contact[5]
            if contact[6] == '':
                new_contacts_list[count-2][6] = search_contact[6]
            new_contacts_list.remove(search_contact)
    count += 1

for sorted_format in new_contacts_list:
    print(sorted_format)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)


