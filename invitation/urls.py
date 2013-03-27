from django.conf.urls.defaults import *

from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from app_settings import INVITE_ONLY

from invitation import views

urlpatterns = patterns('',
    url(r'^invitation/$',
        TemplateView.as_view(template_name='invitation/invitation_home.html'),
        {'template': 'invitation/invitation_home.html'},
        name='invitation_home'),
    url(r'^invitation/invite/$',
        views.invite,
        name='invitation_invite'),
    url(r'^invitation/invite/complete/$',
        TemplateView.as_view(template_name='invitation/invitation_complete.html'),
        {'template': 'invitation/invitation_complete.html'},
        name='invitation_complete'),
    url(r'^invitation/invite/unavailable/$',
        TemplateView.as_view(template_name='invitation/invitation_unavailable.html'),
        {'template': 'invitation/invitation_unavailable.html'},
        name='invitation_unavailable'),
    url(r'^invitation/accept/complete/$',
        TemplateView.as_view(template_name='invitation/invitation_registered.html'),
        {'template': 'invitation/invitation_registered.html'},
        name='invitation_registered'),
    url(r'^invitation/accept/(?P<invitation_key>.+)/$',
        views.register,
        name='invitation_register'),
)

if INVITE_ONLY:
    urlpatterns += patterns('',
        url(r'^register/$',
            'django.views.generic.simple.redirect_to',
            {'url': '../invitation/invite_only/', 'permanent': False},
            name='registration_register'),
        url(r'^invitation/invite_only/$',
            TemplateView.as_view(template_name='invitation/invite_only.html'),
            {'template': 'invitation/invite_only.html'},
            name='invitation_invite_only'),
        url(r'^invitation/reward/$',
            views.reward,
            name='invitation_reward'),
)
