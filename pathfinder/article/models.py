import hashlib
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from pathfinder.models import ModelBase

class Article(ModelBase):
    """
    Article holds all hashed articles that pertain to a certain campaign
    """
    slug = models.CharField("Campaign Slug", max_length=200, db_column="ArticleSlug")
    content = models.TextField("Article Content", null=True, db_column="ArticleContent")
    seed = models.CharField("Seed words", max_length=255, db_column="CampaignSeed")

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = r'Article'
        verbose_name = r'Article'
        verbose_name_plural = r'Article'
    
