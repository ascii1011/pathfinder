from django.db import models
from django.template.defaultfilters import slugify

from pathfinder.models import ModelBase


class Campaign(ModelBase):
    slug = models.SlugField("Unique Slug", max_length=200, db_column="CampaignSlug", db_index=True, editable=False, unique=True)
    name = models.CharField("Campaign Name", max_length=255, db_column="CampaignName")
    desc = models.TextField("Campaign Description", blank=True, null=True, db_column="CampaignDescription")
    seed = models.CharField("Campaign Seed words", max_length=255, db_column="CampaignSeed")

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('campaign_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.id:
            m = hashlib.md5()
            m.update( str( datetime.now() ) )
            self.slug = slugify(self.name[:100])+'_'+str(m.hexdigest()).replace('-','_')
        super(Campaign, self).save(*args, **kwargs)

    class Meta:
        db_table = r'Campaign'
        verbose_name = r'Campaign'
        verbose_name_plural = r'Campaign'
    