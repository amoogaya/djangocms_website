from cms.menu_bases import CMSAttachMenu
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from menus.menu_pool import menu_pool
from menus.base import NavigationNode, Menu
from polls.models import Poll


class PollsMenu(CMSAttachMenu):
    name = _("Polls Menu")

    def get_nodes(self, request):

        nodes = []
        for poll in Poll.objects.all():
            node = NavigationNode(
                title=poll.question,
                url=reverse('polls:detail', args=(poll.pk,)),
                id=poll.pk,
                attr={'visible_for_anonymous': False}
            )
            nodes.append(node)

        return nodes


menu_pool.register_menu(PollsMenu)
