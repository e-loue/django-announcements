# Django 1.6 fix
try:
    from django.conf.urls import *
except ImportError:
    from django.conf.urls.defaults import *
from django.views.generic import DetailView

from announcements.models import Announcement
from announcements.views import *


announcement_detail_info = {
    "queryset": Announcement.objects.all(),
}

urlpatterns = patterns("",
    url(r"^(?P<object_id>\d+)/$", DetailView.as_view(),
        announcement_detail_info, name="announcement_detail"),
    url(r"^(?P<object_id>\d+)/hide/$", announcement_hide,
        name="announcement_hide"),
    url(r"^$", AnnouncementList.as_view(), name="announcement_home"),
)
