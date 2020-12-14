from .cms_appconfig import FaqConfig
from aldryn_apphooks_config.app_base import CMSConfigApp
from django.utils.translation import gettext_lazy as _
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class FaqApp(CMSConfigApp):
    name = _("Faq App")
    app_name = "faq"
    app_config = FaqConfig

    def get_urls(self, page=None, language=None, **kwargs):
        return ["faq.urls"]

