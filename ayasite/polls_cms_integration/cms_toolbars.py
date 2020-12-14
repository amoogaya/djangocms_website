from polls.models import Poll
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse


class PollToolbar(CMSToolbar):
    supported_apps = ['polls']

    def populate(self):
        if not self.is_current_app:
            return

        button_list = self.toolbar.add_button_list()

        button_list.add_sideframe_button(
            name='Poll list',
            url=admin_reverse('polls_poll_changelist'),
        )

        button_list.add_modal_button(
            name='Add a new poll',
            url=admin_reverse('polls_poll_add'),

        )


toolbar_pool.register(PollToolbar)
