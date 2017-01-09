import logging
from os import environ, rename, remove
from subprocess import call

from boto.s3.connection import S3Connection


def restore():
    conn = S3Connection(environ.get('AWS_ACCESS_KEY_ID'),
                        environ.get('AWS_SECRET_ACCESS_KEY'),
                        host=environ.get('AWS_S3_HOST'))
    bucket = conn.get_bucket("miniblog-backup")
    print("Downloading the latest backup file from S3...")
    for i in bucket.list():
        print('.', end="")
    print("\n%s was downloaded from S3" % i.name)
    try:
        i.get_contents_to_filename(i.name)
        rename(i.name, "miniblog.sql")
        call("sh ./dockerify/uwsgi/restore.sh", shell=True)
        print("\nDatabase restoration was successful\n")
        remove("*.sql")
    except Exception as e:
        logging.error(i.name + ":" + "FAILED")
        print("Error occurred: %s" % e)
        remove("*.sql")
        exit(1)


if __name__ == '__main__':
    restore()
