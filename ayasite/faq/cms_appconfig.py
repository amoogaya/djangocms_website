from django import forms
from django.db import models
from app_data import AppDataForm
from aldryn_apphooks_config.utils import setup_config
from aldryn_apphooks_config.models import AppHookConfig
from django.utils.translation import gettext_lazy as _


class FaqConfig(AppHookConfig):
    paginate_by = models.PositiveIntegerField(
        verbose_name=_('paginate size'),
        blank=False,
        default=5,
    )


class FaqConfigForm(AppDataForm):
    title = forms.CharField()


setup_config(FaqConfigForm, FaqConfig)

