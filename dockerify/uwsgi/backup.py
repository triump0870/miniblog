from boto.s3.connection import S3Connection, Key
from os.path import join, exists
from os import environ
import sys


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


try:
    backup_file = environ.get("BACKUP_FILE")
    backup_file += ".sql"
    file = join("./", backup_file)
    print("backup file path: %s" % backup_file)
    if exists(file):
        conn = S3Connection(environ.get('AWS_ACCESS_KEY_ID'),
                            environ.get('AWS_SECRET_ACCESS_KEY'),
                            host=environ.get('AWS_S3_HOST'))
        bucket = conn.get_bucket("miniblog-backup")
        k = Key(bucket)
        k.key = backup_file
        print("uploading %s to s3" % backup_file)
        k.set_contents_from_filename(backup_file,replace=True, cb=percent_cb, num_cb=15)
        print("\nupload was complete")

except Exception as e:
    print("Error occurred: %s" % e)
    exit(1)
