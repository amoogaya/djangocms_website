from cms.utils.i18n import force_language
from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool
from .forms import PollWizardForm


class PollWizard(Wizard):

    def get_success_url(self, obj, **kwargs):
        if 'language' in kwargs:
            with force_language(kwargs['language']):
                url = obj.get_absolute_url()
        else:
            url = obj.get_absolut_url()

        return url


poll_wizard = PollWizard(
    title="Poll",
    weight=200,
    form=PollWizardForm,
    description="Create a new Poll",
)

wizard_pool.register(poll_wizard)
