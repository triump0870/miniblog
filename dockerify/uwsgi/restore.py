import logging
from os import environ, rename
from subprocess import call

from boto.s3.connection import S3Connection


def restore():
    conn = S3Connection(environ.get('AWS_ACCESS_KEY_ID'),
                        environ.get('AWS_SECRET_ACCESS_KEY'),
                        host=environ.get('AWS_S3_HOST'))
    bucket = conn.get_bucket(environ.get('AWS_S3_BUCKET'))
    print("Downloading the latest backup file from S3...")
    for sql_file in bucket.list():
        print('.', end="")
    try:
        sql_file.get_contents_to_filename(sql_file.name)
        print("\n%s was downloaded from S3" % sql_file.name)
        rename(sql_file.name, "miniblog.sql")
        call("sh ./dockerify/uwsgi/restore.sh", shell=True)
        print("\nDatabase restoration was successful\n")
    except Exception as e:
        logging.error(sql_file.name + ":" + "FAILED")
        print("Error occurred: %s" % e)
        exit(1)


if __name__ == '__main__':
    restore()
