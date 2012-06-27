#!/usr/bin/env python

from issue_tracker.models import Category,Site,Region,FieldEngineer,Ticket
from django.contrib import admin
from datetime import datetime

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_code','location','lat','lng')
    list_per_page = 50

class CategoryAdmin(admin.ModelAdmin):
    pass

class RegionAdmin(admin.ModelAdmin):
    pass

class FieldEngineerAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name','phoneNo','alternatePhoneNo','region')
    list_display_links = ('first_name','last_name')
    list_filter = ('region',)

class TicketAdmin(admin.ModelAdmin):
   list_display = ('description','site_code','assigned_to','category','start_time','close_time','status')
   date_hierarchy = 'start_time'
   list_per_page = 50
   radio_fields = {'status':admin.HORIZONTAL}
   list_filter = ('category','assigned_to','status')
   
   def save_model(self,request,obj,form,change):
        obj.assigned_by = request.user
        
        if form.cleaned_data['status'] == '1':
            obj.close_time = datetime.now()
        
        obj.save()
    


admin.site.register(Site,SiteAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(FieldEngineer,FieldEngineerAdmin)
admin.site.register(Ticket,TicketAdmin)
