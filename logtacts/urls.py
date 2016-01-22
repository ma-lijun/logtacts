from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from allauth.account import views as allauth_views

from contacts.views import (
    contact_views,
    log_views,
    search_views,
)

from contacts.api import views as contact_api_views

from invitations.views import (
    CreateInviteView,
    AcceptInviteView,
    ChangePasswordView,
)

from logtacts.views import HomeView

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'logtacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/search/$', contact_api_views.ContactSearchAPIView.as_view()),
    url(
        r'^api/contacts/$',
        contact_api_views.ContactListCreateAPIView.as_view(),
    ),
    url(
        r'^api/contacts/(?P<pk>\d+)/$',
        contact_api_views.ContactDetailEditAPIView.as_view(),
    ),
    url(
        r'^api/contacts/(?P<pk>\d+)/logs/$',
        contact_api_views.LogListCreateAPIView.as_view(),
    ),
    url(r'^api/tags/$', contact_api_views.TagListCreateAPIView.as_view()),
    url(r'^', include('django.contrib.auth.urls')),
    url(
        r'^allauth_login/', allauth_views.login, name='account_login'),
    url(r'^signup/', allauth_views.signup, name='account_signup'),
    url(
        r'^hold/',
        TemplateView.as_view(template_name='signup_success.html'),
        name='account_inactive',
    ),
    url(
        r'^set-password/$',
        ChangePasswordView.as_view(),
        name='set-password',
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^search/',
        search_views.ContactSearchView.as_view(),
        name="search",
    ),
    url(r'^$', HomeView.as_view(), name='home'),
    url(
        r'^list/$',
        contact_views.ContactListView.as_view(),
        name='contacts-list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        contact_views.ContactView.as_view(),
        name='contacts-view',
    ),
    url(
        r'^new$',
        contact_views.CreateContactView.as_view(),
        name='contacts-new',
    ),
    url(
        r'^edit/(?P<pk>\d+)/$',
        contact_views.EditContactView.as_view(),
        name='contacts-edit',
    ),
    url(
        r'^delete/(?P<pk>\d+)/$',
        contact_views.DeleteContactView.as_view(),
        name='contacts-delete',
    ),
    url(
        r'^log/edit/(?P<pk>\d+)/$',
        log_views.EditLogView.as_view(),
        name='log-edit',
    ),
    url(
        r'^log/delete/(?P<pk>\d+)/$',
        log_views.DeleteLogView.as_view(),
        name='log-delete',
    ),
    url(
        r'^tags/new$',
        contact_views.CreateTagView.as_view(),
        name='tags-new',
    ),
    url(
        r'^tags/(?P<pk>\d+)/edit/$',
        contact_views.EditTagView.as_view(),
        name='tags-edit',
    ),
    url(
        r'^tags/(?P<pk>\d+)/delete/$',
        contact_views.DeleteTagView.as_view(),
        name='tags-delete',
    ),
    url(
        r'^tagged/(?P<pk>\d+)/$',
        contact_views.TaggedContactListView.as_view(),
        name='contacts-tagged',
    ),
    url(r'^invites/add$', CreateInviteView.as_view(), name='create-invite'),
    url(
        r'^invites/accept/(?P<key>[\w-]+)/$',
        AcceptInviteView.as_view(),
        name='accept-invite',
    ),
    url(r'^u/', include('profiles.urls')),
    url(
        r'^policies$', 
        TemplateView.as_view(template_name='policies.html'),
        name='policies',
    ),
]
