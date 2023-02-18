# PostgreSQL backup script
*CLI for backing up remote PostgreSQL databases locally or to S3 object storage*

## Usage

Pass in a full database URL, the storage driver, and destination.

Example with S3:
```sh
pgbackup postgres://user@example.com:5432/db_one --driver s3 backups
```

Local example:
```sh
pgbackup postgres://user@example.com:5432/db_one --driver local /var/local/db_one/backups
```
