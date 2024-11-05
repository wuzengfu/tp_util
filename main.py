import json
from random import shuffle

from faker import Faker


class PeronSchema:
    PRESIDENT_ROLE = 'President'
    max_president = 1
    available_roles = ['Vice President', 'Admin', 'Marketing', 'Events (internal)', 'Events (external)',
                       'External Relations']
    available_student_status = ['undergraduate 1', 'undergraduate 2', 'undergraduate 3', 'undergraduate 4',
                                'undergraduate 5', 'undergraduate 6', 'masters', 'phd']

    def __init__(self, name, telegram_handle, email, student_status, roles, nickname):
        self.name = name
        self.telegramHandle = telegram_handle
        self.email = email
        self.studentStatus = student_status
        self.roles = roles
        self.nickname = nickname

    def toDict(self):
        output = dict()
        output['name'] = self.name
        output['telegramHandle'] = self.telegramHandle
        output['email'] = self.email
        output['studentStatus'] = self.studentStatus
        output['roles'] = self.roles
        output['nickname'] = self.nickname
        return output

'''
name - unique name with only alphabets and spaces
telegram_handle - unique telegram handle with at least one alphabet and 4 digits
email - unique valid email address
student status - a random element in available_student_status
roles - 1 to 2 roles from available_roles
nickname - 30% of chance to get a unique name only alphabets and spaces
'''
def generate_item(faker) -> PeronSchema:
    name = faker.unique.name().replace('.', '').replace('\'', '')
    telegram_handle = faker.unique.first_name().lower() + str(faker.random_number(4,True))
    email = faker.unique.email()
    student_status = faker.random_element(PeronSchema.available_student_status)
    roles = faker.random_elements(PeronSchema.available_roles,
                                  faker.random_int(1, min(2, len(PeronSchema.available_roles))),
                                  True)
    nickname = ''
    if faker.random_digit() > 6:
        nickname = faker.unique.name()
    return PeronSchema(name, str(telegram_handle), email, student_status, roles, nickname)

def output_to_json(person_list, path = 'addressbook.json'):
    shuffle(person_list)
    output = dict()
    output['contacts'] = person_list
    json.dump(output, open(path, 'w'), indent=2)

def generate_persons(total_count = 150, convert_to_dict = True):
    faker = Faker()
    person_list = []

    if total_count == 0:
        return person_list

    contact = generate_item(faker)
    contact.roles = [PeronSchema.PRESIDENT_ROLE]
    person_list.append(contact)

    if total_count <= 1:
        return person_list

    for i in range(1, total_count):
        item = generate_item(faker)
        person_list.append(item)

    if convert_to_dict:
        for i in range(len(person_list)):
            person_list[i] = person_list[i].toDict()

    shuffle(person_list)
    return person_list

if __name__ == '__main__':
    person_list = generate_persons()
    output_to_json(person_list)
