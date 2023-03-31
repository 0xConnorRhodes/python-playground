import json
import user  # imports user.py from the local directory

users = user.get_users_info()


def pretty_print_users():
    return json.dumps(users, sort_keys=True, indent=4)


def write_json_file(export_file):
    with open(f'{export_file}.json', 'w') as file:
        json.dump(users, file, sort_keys=True, indent=4)

def print_csv():
    print('username,user id,home directory,shell')
    for i in users:
        row = f'{i["username"]},{i["user id"]},{i["home directory"]},{i["shell"]}'
        print(row)


def write_csv_file(export_file):
    with open(f'{export_file}.csv', 'w') as file:
        file.write('username,user id,home directory,shell\n')

        for i in users:
            row = f'{i["username"]},{i["user id"]},{i["home directory"]},{i["shell"]}\n'
            file.write(row)
