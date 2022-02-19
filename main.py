from pprint import pprint
import re
import csv


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


if __name__ == '__main__':

# lastname,firstname,surname,organization,position,phone,email

# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# 1 поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# 2 привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# 3 объединить все дублирующиеся записи о человеке в одну.


    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код
    pattern = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)(\s+|-?)(\d+)(\s+|-?)(\d+)"
    substitution = r"+7 \2 \3-\5-\7"
    text_phones_res = re.sub(pattern, substitution, contacts_list)
    # print(text_phones_res)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      # Вместо contacts_list подставьте свой список
      datawriter.writerows(contacts_list)