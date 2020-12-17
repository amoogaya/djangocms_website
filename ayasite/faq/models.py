from django.db import models
from aldryn_apphooks_config.fields import AppHookConfigField
from aldryn_apphooks_config.managers import AppHookConfigManager
from .cms_appconfig import FaqConfig
from django.utils.translation import gettext_lazy as _
from cms.extensions import PageExtension, TitleExtension
from cms.extensions.extension_pool import extension_pool


# Create your models here.
class Entry(models.Model):
    app_config = AppHookConfigField(FaqConfig)
    question = models.TextField(blank=True, default='')
    answer = models.TextField()

    object = AppHookConfigManager()

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')


class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')


class RatingExtension(TitleExtension):
    rating = models.IntegerField()


extension_pool.register(IconExtension)
extension_pool.register(RatingExtension)
