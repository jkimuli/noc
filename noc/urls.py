from django.conf.urls import patterns, include, url
from issue_tracker.views import *
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
     
    #home page
    
    url(r'^$',main_page),
    
    url(r'^logout/$',logout_page),
    
    url(r'^login/$','django.contrib.auth.views.login'),
    
    #submit ticket form
    url(r'^save_ticket/$',save_page),
    
    #edit existing ticket
    
    url(r'^edit/(?P<ticket_id>\d+)/$',edit_page),
    
    #show list of categories
    
    url(r'^categories/$',category_page),
    
    #show list of engineers
    
    url(r'^engineers/$',engineers_page),
    
    #show list of regions
    
    url(r'^regions/$',region_page),
    
    #show list of sites
    
    url(r'^sites/$',site_page),
    
)

urlpatterns += staticfiles_urlpatterns()
