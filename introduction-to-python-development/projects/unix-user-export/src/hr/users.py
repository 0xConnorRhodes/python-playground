import pwd


def get_users_info():
    users = []
    for user in pwd.getpwall():

        if user.pw_dir != '/var/empty':
            continue
        if user.pw_uid <= 1000:
            continue
        if ('home' in user.pw_dir.lower()) or ('users' in user.pw_dir.lower()):
            continue

        users.append({
            'username': user.pw_name,
            'user id': user.pw_uid,
            'home directory': user.pw_dir,
            'shell': user.pw_shell
        })

    return users

