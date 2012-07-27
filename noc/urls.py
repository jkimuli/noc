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
    
    #add a new site
    
    url(r'^add_site/$',add_site),
    
    #edit existing site
    
    url(r'^edit_site/(?P<site_id>\d+)/$',edit_site),
    
    #showing engineers in a given region
    
    url(r'^region_engineers/(?P<region_id>\d+)/$',region_engineers),
    
    #showing tickets assigned to a specific engineer
    
    url(r'^engineer_tickets/(?P<engineer_id>\d+)/$',engineer_tickets),
    
    #showing tickets  belonging to a specific category
    
    url(r'^category_tickets/(?P<category_id>\d+)/$',category_tickets),
    
    #showing tickets for a specific site
    
    url(r'^site_tickets/(?P<site_id>\d+)/$',site_tickets),
)

urlpatterns += staticfiles_urlpatterns()
