from django.views.generic.base import TemplateView
from django.apps import apps

# TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls', 'books']
        dictVerbose = {}
        
        # get_app_configs() loads the list registered in INSTALLED_APPS from settings.py
        for app in apps.get_app_configs():
            # 'site-packages' is the part of settings, so we need to exclude this in relative directories
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        # When doen with for loop above, put the dictVerbose to the context in verbose_dict
        context['verbose_dict'] = dictVerbose
        
        return context