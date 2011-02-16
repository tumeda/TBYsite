from django.conf import settings
from django.conf.urls.defaults import patterns, include, \
    url
from django.contrib import admin
from django import forms
from example.joinform import views
from example.joinform import forms
from example.joinform import preview

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'^join-form/$', views.join),
    (r'^post/$', preview.SomeModelFormPreview(forms.JoinForm)),
    #(r'^search/$', views.search),
    # just for testing - native way to sampleapp urls 
    # (r'^sampleapp-native/', include('sampleapp.urls')),
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CMS_MEDIA_ROOT, 'show_indexes': True}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
