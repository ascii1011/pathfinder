import hashlib
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from pathfinder.models import ModelBase


TYPE_CHOICES=(
    ('page', 'static page'),
    ('search', 'search engine'),
    )

class Source(ModelBase):
    slug = models.SlugField("Unique Slug", max_length=200, db_column="SourceSlug", db_index=True, editable=False, unique=True)
    name = models.CharField("Source Name", max_length=255, db_column="SourceName")
    desc = models.TextField("Source Description", blank=True, null=True, db_column="SourceDescription")
    loc = models.CharField("Source Location", max_length=255, db_column="SourceLocation") 
    tipe = models.CharField("Source Type", max_length=20, choices=TYPE_CHOICES, blank=False, db_column="SourceStatus")

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('source-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            m = hashlib.md5()
            m.update( str( datetime.now() ) )
            self.slug = slugify(self.name[:100])+'_'+str(m.hexdigest()).replace('-','_')
        super(Source, self).save(*args, **kwargs)

    class Meta:
        db_table = r'Source'
        verbose_name = r'Source'
        verbose_name_plural = r'Source'
    