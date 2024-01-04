from django.db import models  # noqa: D100


# Create your models here.
class TimeStampedModel(models.Model):
    """TimeStampedModel.

    When creating any model in this project `YOU MUST INHERIT THIS MODEL`.

    Atributes
    ---------
    created_at: models.DateTimeField
        when model instance was created

    updated_at: models.DateTimeField
        when model instance was updated
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  # noqa: WPS306 D106
        abstract = True
