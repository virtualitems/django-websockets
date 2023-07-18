"""
classic http request/response handlers
"""

from django.views import generic


class IndexView(generic.TemplateView):
    """Index page view"""
    template_name = 'index.html'
