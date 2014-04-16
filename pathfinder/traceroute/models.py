import hashlib
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from pathfinder.models import ModelBase

class Traceroute(ModelBase):
    """
    Traceroute handles the resulting trace and content analysis
    """
    slug = models.CharField("Campaign Slug", max_length=200, db_column="CampaignSlug")
    result = models.TextField("Campaign Result", null=True, db_column="CampaignResult")
    seedblob = models.TextField("Seed word blob", db_column="CampaignSeedBlob")

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('traceroute-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = r'Traceroute'
        verbose_name = r'Traceroute'
        verbose_name_plural = r'Traceroute'
    
