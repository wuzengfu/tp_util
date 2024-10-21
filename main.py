import json

from faker import Faker


class PeronSchema:
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


faker = Faker()

available_roles = ['President', 'Vice President', 'Admin', 'Marketing', 'Events (internal)', 'Events (external)',
                   'External Relations']
available_student_status = ['undergraduate 1', 'undergraduate 2', 'undergraduate 3', 'undergraduate 4',
                            'undergraduate 5', 'undergraduate 6', 'masters', 'phd']
output = dict()
person_list = []
total_count = 150

# name - unique name with only alphabets
# telegram_handle - unique 8-digit number
# email - unique valid email address
# student status - a random element in available_student_status
# roles - some random elements (at least one) in available_student_status
# nickname - 50% of chance to get a unique name with only one word
def generate_item() -> PeronSchema:
    name = faker.unique.name().replace('.', '').replace('\'', '')
    telegram_handle = faker.unique.random_number(8, True)
    email = faker.unique.email()
    student_status = faker.random_element(available_student_status)
    roles = faker.random_elements(available_roles,
                                  faker.random_int(1, len(available_roles)),
                                  True)
    nickname = ''
    if faker.random_digit() > 4:
        nickname = faker.unique.name()
    return PeronSchema(name, str(telegram_handle), email, student_status, roles, nickname)


if __name__ == '__main__':
    for i in range(total_count):
        item = generate_item().toDict()
        person_list.append(item)
    output['persons'] = person_list
    json.dump(output, open('addressbook.json', 'w'), indent=2)
