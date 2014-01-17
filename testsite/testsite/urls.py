from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from testsite.views import hello, current_datetime

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^admin/', include(admin.site.urls)),
)
