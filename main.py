import re
import csv

phone_pattern = r'(\+7|8)\s*(\s?\()*(\d{3})[\s\)-]*(\d{3})[\)\s-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\3)\4-\5-\6 \7\8'


# TODO 1: выполните пункты 1-3 ДЗ
def main_func(phonebook_list):
    """Функция для приведения справочника к стандартному формату (ФИО к Ф+И+О и номера к +7(999)999-99-99 доб.9999)"""
    new_list = list()
    for item in phonebook_list:
        # print(item)
        # print('1_______________')
        # print(item[:3])
        # print('2_______________')
        full_name = ' '.join(item[:3]).split(' ')
        # print(full_name)
        # print('3_______________')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(phone_pattern, phone_sub, item[5]),
                  item[6]]
        new_list.append(result)
        # print(full_name[0])
        # print(full_name[1])
        # print(full_name[2])
        # print(item[3])
        # print(item[4])
        # print(item[5])
        # print(item[6])
    return string_join(new_list)


def string_join(contacts):
    """Функция поиска и объединения строк для дублей ФИО"""
    for contact in contacts:
        firstname = contact[0]
        lastname = contact[1]
        surname = contact[2]
        for new_contact in contacts:
            new_firstname = new_contact[0]
            new_lastname = new_contact[1]
            new_surname = new_contact[2]
            if firstname == new_firstname and \
               lastname == new_lastname and \
               (surname == new_surname or surname == "" or new_surname == ""):
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]

    result_list = list()
    for elem in contacts:
        if elem not in result_list:
            result_list.append(elem)

    return result_list


if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(main_func(contacts_list))
