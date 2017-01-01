from django.conf import settings
from storages.backends.s3boto import S3BotoStorage
from django.core.files.storage import get_storage_class
from os.path import splitext


class StaticStorage(S3BotoStorage):
    """uploads to 'mybucket/static/', serves from 'cloudfront.net/static/'"""
    location = settings.STATICFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')


class MediaStorage(S3BotoStorage):
    """uploads to 'mybucket/media/', serves from 'cloudfront.net/media/'"""
    location = settings.MEDIAFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(MediaStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')


class CacheS3BotoStorage(S3BotoStorage):
    """
    django-compressor uses this class to gzip the compressed files and send
    them to s3. These files are then saved locally, which ensures that they
    only create fresh copies when they need to.
    """

    def __init__(self, *args, **kwargs):
        super(CacheS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class('compressor.storage.CompressorFileStorage')

    def save(self, filename, content, max_length=None):
        filename = super(CacheS3BotoStorage, self).save(filename, content)
        self.local_storage._save(filename, content)
        return filename
