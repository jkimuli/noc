from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noc.views.home', name='home'),
    # url(r'^noc/', include('noc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    #static_files
    
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$','issue_tracker.views.main_page'),
     
    #urls for issue_tracker app

     url(r'^ticktr/',include('issue_tracker.urls')),
    
    
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
    
    url(r'^login/$','django.contrib.auth.views.login'),

    
    
    
)

urlpatterns += staticfiles_urlpatterns()
