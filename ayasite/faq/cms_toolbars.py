from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from cms.extensions.toolbar import ExtensionToolbar
from .models import IconExtension, RatingExtension
from django.utils.translation import gettext_lazy as _
from cms.utils import get_language_list


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


class IconExtensionToolbar(ExtensionToolbar):
    model = IconExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()

        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(
                    _('page icon'),
                    url=url,
                    disabled=not self.toolbar.edit_mode_active,
                    position=0,
                )


class RatingExtensionToolbar(ExtensionToolbar):
    model = RatingExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu and self.toolbar.edit_mode_active:
            sub_menu = self._get_sub_menu(
                current_page_menu,
                'submenu_label',
                'Ratings',
                position=1,
            )
            urls = self.get_title_extension_admin()
            page = self._get_page()
            title_set = page.title_set.filter(language__in=get_language_list(page.node.site_id))

            nodes = [(title_extension, url, title.title) for (
                (title_extension, url), title) in zip(urls, title_set)
                ]

            for title_extension, url, title in nodes:

                # adds toolbar items
                sub_menu.add_modal_item(
                    'Rate %s' % title, url=url, disabled=not self.toolbar.edit_mode_active
                    )


toolbar_pool.register(FaqToolbar)
toolbar_pool.register(IconExtensionToolbar)
toolbar_pool.register(RatingExtensionToolbar)
