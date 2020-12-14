from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse


class FaqToolbar(CMSToolbar):
    supported_apps = ['faq']

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu(
            key='faq',
            verbose_name='Frequency question',
        )

        menu.add_sideframe_item(
            name=' faq list',
            url=admin_reverse('faq_entry_changelist'),
        )

        menu.add_break(identifier='Frequency_question_section')

        submenu = menu.get_or_create_menu(
            key='faq',
            verbose_name='Frequency question submenu',
        )


toolbar_pool.register(FaqToolbar)
