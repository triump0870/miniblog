import os

from django.core.management.base import BaseCommand
from django.apps import apps
from django.db.models import Q
from django.conf import settings
from django.db.models import FileField

from boto.s3.connection import S3Connection, Key
from utils.colors import bcolors


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--info',
            action='store_true',
            default=False,
            help="List the files to be deleted"
        )

    help = "This command deletes all media files from the MEDIA_ROOT " \
           "directory which are no longer referenced by any of the " \
           "models from installed_apps"

    def handle(self, *args, **options):
        all_models = apps.get_models()
        physical_files = set()
        db_files = set()

        # Get all files from the database
        for model in all_models:
            file_fields = []
            filters = Q()
            for f_ in model._meta.fields:
                if isinstance(f_, FileField):
                    file_fields.append(f_.name)
                    is_null = {'{}__isnull'.format(f_.name): True}
                    is_empty = {'{}__exact'.format(f_.name): ''}
                    filters = Q(**is_null) | Q(**is_empty)
            # only retrieve the models which have non-empty, non-null file fields
            if file_fields:
                files = model.objects.exclude(filters).values_list(*file_fields).distinct()
                for file in files:
                    db_files.update(file)

        # Get all files from the MEDIA_ROOT, recursively
        media_root = getattr(settings, 'MEDIA_URL', None)
        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, host=settings.AWS_S3_HOST)
        bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        if media_root is not None:
            for key in bucket.list("media"):
                physical_files.add(key.name[6:])

        # Compute the difference and delete those files
        deletables = physical_files - db_files
        deletables = list(filter(None, deletables))

        if options['info']:
            for i in deletables:
                print(i, end="\n")

        if len(deletables):
            print("These files are not associated with any object. Are you sure "
                  "you want to delete these files?\n"
                  "If you're unsure answer 'no'.", end="\n")
            res = input(bcolors.WARNING + bcolors.BOLD + "Type 'yes' to continue, or 'no' to cancel: " + bcolors.ENDC)
            if res == 'yes':
                for file_ in deletables:
                    k = Key(bucket, "media/")
                    k.key = "media/" + file_
                    print(k.delete())
            else:
                print(bcolors.FAIL + bcolors.BOLD + "The last operation was cancelled" + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + bcolors.BOLD + "Nothing to delete" + bcolors.ENDC)
