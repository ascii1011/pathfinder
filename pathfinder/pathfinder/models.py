from django.db import models

class ModelBase(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, editable=False, db_column='DateTimeAdd')
    date_modified = models.DateTimeField(auto_now=True, editable=False, db_column='DateTimeMod')

    class Meta:
        abstract = True
