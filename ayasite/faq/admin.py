from django.contrib import admin
from .models import Entry, IconExtension, RatingExtension
from .cms_appconfig import FaqConfig
from aldryn_apphooks_config.admin import ModelAppHookConfig, BaseAppHookConfig
from cms.extensions import PageExtensionAdmin, TitleExtensionAdmin


# Register your models here.
class EntryAdmin(ModelAppHookConfig, admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'app_config',
    )
    list_filter = (
        'app_config',
    )


class FaqConfigAdmin(BaseAppHookConfig, admin.ModelAdmin):

    def get_config_fields(self):
        return (
            'paginate_by',
            'config.title',
        )


class IconExtensionAdmin(PageExtensionAdmin):
    pass


class RatingExtensionAdmin(TitleExtensionAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
admin.site.register(FaqConfig, FaqConfigAdmin)
admin.site.register(IconExtension, IconExtensionAdmin)
admin.site.register(RatingExtension, RatingExtensionAdmin)
