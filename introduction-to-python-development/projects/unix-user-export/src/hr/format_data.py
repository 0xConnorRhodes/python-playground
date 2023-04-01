import json
import hr.users  # imports user.py from the local directory

users = hr.users.get_users_info()


def print_json():
    print(json.dumps(users, sort_keys=True, indent=4))


def write_json_file(export_file):
    # if the filename doesn't end in the file extension, add it automatically
    if not export_file.split('.')[-1] == 'json':
        export_file = export_file + '.json'

    with open(f'{export_file}', 'w') as file:
        json.dump(users, file, sort_keys=True, indent=4)

def print_csv():
    print('username,user id,home directory,shell')
    for i in users:
        row = f'{i["username"]},{i["user id"]},{i["home directory"]},{i["shell"]}'
        print(row)


def write_csv_file(export_file):
    # if the filename doesn't end in the file extension, add it automatically
    if not export_file.split('.')[-1] == 'csv':
        export_file = export_file + '.csv'

    with open(f'{export_file}', 'w') as file:
        file.write('username,user id,home directory,shell\n')

        for i in users:
            row = f'{i["username"]},{i["user id"]},{i["home directory"]},{i["shell"]}\n'
            file.write(row)
