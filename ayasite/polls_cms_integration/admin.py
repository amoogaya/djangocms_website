from .models import MyModel
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin


class MyModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ['my_placeholder']


# Register your models here.
admin.site.register(MyModel, MyModelAdmin)
