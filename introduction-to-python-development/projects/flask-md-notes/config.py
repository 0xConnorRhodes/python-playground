import os

# pull default variables from os envirionment
# and specify default values if unset in environment
db_host = os.environ.get('DB_HOST', default='localhost')
db_name = os.environ.get('DB_NAME', default='notes')
db_user = os.environ.get('DB_USERNAME', default='db_user')
db_password = os.environ.get('DB_PASSWORD', default='')
db_port = os.environ.get('DB_PORT', default='5432')

# remove warnings from output
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

