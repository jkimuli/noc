from django.conf.urls import patterns,url,include


urlpatterns  = patterns('issue_tracker.views',

    #main_page

    url(r'^$','main_page'),
         
    #submit ticket form

    url(r'^save_ticket/$','save_page'),
    
    #edit existing ticket
    
    url(r'^edit/(?P<ticket_id>\d+)/$','edit_page'),
    
    #show list of categories
    
    url(r'^categories/$','category_page'),
    
    #show list of engineers
    
    url(r'^engineers/$','engineers_page'),
    
    #show list of regions
    
    url(r'^regions/$','region_page'),
    
    #show list of sites
    
    url(r'^sites/$','site_page'),
    
    #add a new site
    
    url(r'^add_site/$','add_site'),
    
    #edit existing site
    
    url(r'^edit_site/(?P<site_id>\d+)/$','edit_site'),
    
    #showing engineers in a given region
    
    url(r'^region_engineers/(?P<region_id>\d+)/$','region_engineers'),
    
    #showing tickets assigned to a specific engineer
    
    url(r'^engineer_tickets/(?P<engineer_id>\d+)/$','engineer_tickets'),
    
    #showing tickets  belonging to a specific category
    
    url(r'^category_tickets/(?P<category_id>\d+)/$','category_tickets'),
    
    #showing tickets for a specific site
    
    url(r'^site_tickets/(?P<site_id>\d+)/$','site_tickets'),
)
          
