import hashlib
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from pathfinder.models import ModelBase

STATUS_CHOICES=(
    ('100', 'Has not been started'),
    ('200', 'Generating seed data'),
    ('300', 'Spidering'),
    ('400', 'Archiving Data'),
    ('500', 'Analyzing Data'),
    ('1000', 'Errors'),
    )


class Campaign(ModelBase):
    """
    Campaigns represent a process spawned off of the words provided in the CampaignSeed field.
    
    Current CampaignSeed field intention is simple, comma delimited, words; 
    A notion of weight as you progress from left to right.
    Future implementations may become a complex json structure with varying types of "weight" and direction.
    """
    slug = models.SlugField("Unique Slug", max_length=200, db_column="CampaignSlug", db_index=True, editable=False, unique=True)
    name = models.CharField("Campaign Name", max_length=255, db_column="CampaignName")
    desc = models.TextField("Campaign Description", blank=True, null=True, db_column="CampaignDescription")
    seed = models.CharField("Campaign Seed words", max_length=255, db_column="CampaignSeed")
    onoff = models.BooleanField("On/Off", blank=False, default=False, db_column="CampaignOnOff")
    status = models.CharField("Campaign Status", max_length=20, choices=STATUS_CHOICES, blank=False, db_column="CampaignStatus")

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('campaign-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            m = hashlib.md5()
            m.update( str( datetime.now() ) )
            self.slug = slugify(self.name[:100])+'_'+str(m.hexdigest()).replace('-','_')
        super(Campaign, self).save(*args, **kwargs)

    class Meta:
        db_table = r'Campaign'
        verbose_name = r'Campaign'
        verbose_name_plural = r'Campaign'
    