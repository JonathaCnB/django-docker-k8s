from decouple import config

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'django_k8s.cdn.backends.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'django_k8s.cdn.backends.StaticRootS3BotoStorage'
# AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
# AWS_LOCATION = "https://django-k8s.nyc3.digitaloceanspaces.com"
