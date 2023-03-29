import json
import user  # imports user.py from the local directory

users = user.get_users_info()


def pretty_print_users():
    return json.dumps(users, sort_keys=True, indent=4)


def write_json_file(export_file):
    with open(f'{export_file}.json', 'w') as file:
        json.dump(users, file, sort_keys=True, indent=4)


def write_csv_file():
    pass


write_json_file('test')