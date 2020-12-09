from .models import PollPluginModel
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import gettext as _


@plugin_pool.register_plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel
    module = _("Polls")
    name = _("poll plugin")
    render_template = "polls_cms_integration/poll_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

