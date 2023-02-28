import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url, timestamp=None):
    db_name = url.split('/')[-1] # split on slashes and show the last field which will be the database name
    db_name = db_name.split('?')[0] # show only first field split on '?' which will remove any SQL query syntax that may be present
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"
