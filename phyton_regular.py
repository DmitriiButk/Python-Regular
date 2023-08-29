import re
import csv
from pprint import pprint


with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=",")
    contacts_list = list(reader)


phone_pattern = r"(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[\s-]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?"
phone_subst = r"+7(\2)\3-\4-\5\7\8\9"

correct_phone_list = []

for contact in contacts_list:
    string_ = ','.join(contact)
    correct_string = re.sub(phone_pattern, phone_subst, string_)
    split_string = correct_string.split(',')
    correct_phone_list.append(split_string)

new_contacts_list = []

for contact in correct_phone_list:
    correct_name_list = ' '.join(contact[0:3]).split()
    if len(correct_name_list) != 3:
        correct_name_list.append("")
    result = correct_name_list + contact[3:]
    new_contacts_list.append(result)

final_contact_list = []

for el in new_contacts_list:
    for contact in final_contact_list:
        if contact[:1] == el[:1]:
            final_contact_list.remove(contact)
            el = [x if x != "" else y for x, y in zip(contact, el)]
    final_contact_list.append(el)


with open('phonebook.csv', 'w', encoding='utf-8') as file:
    datawriter = csv.writer(file, delimiter=',')
    datawriter.writerows(final_contact_list)
