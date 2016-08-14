from django.conf.urls import url
from django.views.generic import TemplateView

from .views import RSVPCreateView

urlpatterns = [
    url(r'^$', RSVPCreateView.as_view(), name='create'),
    url(r'^thanks/$', TemplateView.as_view(template_name='rsvp/thanks.html'), name='thanks'),
]
