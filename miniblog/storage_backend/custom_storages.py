from logging import getLogger

from django.conf import settings
from django.core.files.storage import get_storage_class
from storages.backends.s3boto import S3BotoStorage
from storages.backends.s3boto3 import S3Boto3Storage

logger = getLogger("blog")


class StaticStorage(S3Boto3Storage):
    location = 'static'
    access_key = settings.AWS_S3_USER_KEY
    secret_key = settings.AWS_S3_USER_SECRET

    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = settings.AWS_CLOUDFRONT_DOMAIN
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    access_key = settings.AWS_S3_USER_KEY
    secret_key = settings.AWS_S3_USER_SECRET
    file_overwrite = True
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    custom_domain = settings.AWS_CLOUDFRONT_DOMAIN
    default_acl = 'public-read'


# class MediaStorage(S3BotoStorage):
#     """uploads to 'mybucket/media/', serves from 'cloudfront.net/media/'"""
#     location = settings.MEDIAFILES_LOCATION
#
#     access_key = settings.AWS_CLOUDFRONT_USER_KEY
#     secret_key = settings.AWS_CLOUDFRONT_USER_SECRET
#
#     def __init__(self, *args, **kwargs):
#         kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
#         super(MediaStorage, self).__init__(*args, **kwargs)
#         # self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')
#
#
class CacheS3BotoStorage(S3BotoStorage):
    """
    django-compressor uses this class to gzip the compressed files and send
    them to s3. These files are then saved locally, which ensures that they
    only create fresh copies when they need to.
    """

    def __init__(self, *args, **kwargs):
        super(CacheS3BotoStorage, self).__init__(*args, **kwargs)
        # self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')

    def save(self, filename, content, max_length=None):
        filename = super(CacheS3BotoStorage, self).save(filename, content)
        self.local_storage._save(filename, content)
        return filename
