PostgreSQL backup script
===

CLI for backup up remote PostgreSQL databases locally or to S3 object storage

Development Environment
---
1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone the repository
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Avtivate virtualenv: ``pipenv shell``

Usage
---
Pass in a full database URL, the storage driver, and destination.

Example with S3:

::
    $ pgbackup postgres://user@example.com:5432/db_one --driver s3 backups

Local example:

::
    $ pgbackup postgres://user@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
---

Run tests locally using ``make`` (virtualenv must be active):

::
    $ make

If the virtualenv is not active:

::
    $ pipenv run make

