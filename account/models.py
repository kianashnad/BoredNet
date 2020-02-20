# Create your models here.
from BoredNet.models import BaseModel


class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        from django.utils.datetime_safe import strftime
        from time import gmtime
        import os

        ext = filename.split('.')[-1]
        showtime = strftime("_-%d_-%H-%Y_-%m-%M-%S", gmtime())

        # get filename
        if instance.pk:
            filename = '{}.{}'.format(str(instance.pk) + showtime, ext)

        else:
            from uuid import uuid4

            # set filename as random string
            filename = '{}.{}'.format(str(uuid4().hex) + showtime, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class Profile(BaseModel):
    from django.core.validators import FileExtensionValidator
    from django.db import models

    profile_picture = models.ImageField(upload_to=UploadToPathAndRename('profile_pics/'),
                                        validators=[FileExtensionValidator(['jpg'])])
    gender = models.IntegerField()
    amount_followings = models.BigIntegerField(default=0)
    amount_followers = models.BigIntegerField(default=0)
    first_name = models.CharField(blank=False, max_length=15)
    last_name = models.CharField(blank=False, max_length=15)
    date_of_birth = models.DateField()
