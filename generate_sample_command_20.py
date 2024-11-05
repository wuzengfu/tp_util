from main import generate_persons, PeronSchema


def output_as_command(person_list: list[PeronSchema]):
    output = '        return new Contact[] {'
    output += '\n'
    row_schema = """            new Contact(new Name("{0}"), new TelegramHandle("{1}"),\n                new Email("{2}"),\n                new StudentStatus("{3}"),\n                getRoleSet({4}),\n                new Nickname("{5}")),\n"""
    for person in person_list:
        roles = ', '.join(f'"{w}"' for w in person.roles)
        row = row_schema.format(person.name, person.telegramHandle, person.email, person.studentStatus, roles,
                                person.nickname)
        output += row
    if len(person_list) > 0:
        output = output[:-2]
    output += '};'

    with open('addressbook_command.txt', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    total_count = 20
    person_list = generate_persons(total_count, False)
    output_as_command(person_list)
