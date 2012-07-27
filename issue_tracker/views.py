# Create your views here.

from datetime import datetime
from django.contrib.auth.models import User
from issue_tracker.models import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from issue_tracker.forms import TicketForm,SiteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login


def main_page(request):
    
    tickets = Ticket.objects.order_by('-start_time').filter(status = '0')[:50]
       
            
    variables = RequestContext(request,{
        'tickets' : tickets,
        'user' : request.user,
        
    })
    return render_to_response('home.html',variables)
    
def logout_page(request):
    logout(request)
    
    return HttpResponseRedirect('/')
    
def login_page(request):
    login(request,request.POST)
    
    return HttpResponseRedirect('/')
    
    
@login_required   
def save_page(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST)
        
        if form.is_valid():
            ticket = form.save(commit=False)
            
            ticket.assigned_by = request.user
            
            ticket.save()
            
            return HttpResponseRedirect('/')
                
                
        
    
    else:
        form = TicketForm()
        
    variables = RequestContext(request,{
        'form' : form,
        'add':True
    })
        
    return render_to_response('save_ticket.html',variables)
    

@login_required    
def edit_page(request,ticket_id):
    #get existing ticket from database
    
    ticket = get_object_or_404(Ticket,pk=ticket_id)
    
    if request.method == 'POST':
        form = TicketForm(instance = ticket,data=request.POST)
        
        if form.is_valid():
            
            
            ticket = form.save(commit=False)
            
            if request.POST['status'] == '1':
                ticket.close_time = datetime.now()
                
                ticket.save()
                
            
            return HttpResponseRedirect('/')
            
    else:
        form = TicketForm(instance=ticket)
        
    variables = RequestContext(request,{
        'form':form,
        'add':False
    })
    
    return render_to_response('save_ticket.html',variables)
        
           

def category_page(request):
    types = Category.objects.all()
    
    variables = RequestContext(request,{
        'types':types
    })
    
    return render_to_response('categories.html',variables)


def region_page(request):
    regions = Region.objects.all()
    
    variables = RequestContext(request,{
        'regions':regions,
        'show_results':False
    })
    
    return render_to_response('regions.html',variables)


def site_page(request):
    #Retrieve sites in database
    
    sites = Site.objects.all()
    
    variables = RequestContext(request,{
        'sites':sites
    })
    
    return render_to_response('sites.html',variables)

def engineers_page(request):
    #retrieve all engineers we have in the database
    
    engineers = FieldEngineer.objects.all()
    
    variables = RequestContext(request,{
        'engineers':engineers
    })
    
    return render_to_response('engineers.html',variables)
 
@login_required   
def add_site(request):
    if request.method == 'POST':
        form = SiteForm(data = request.POST)
        
        if form.is_valid():
            site = form.save()
            
            return HttpResponseRedirect('/sites/')
            
    else:
        form = SiteForm()
        
    variables = RequestContext(request,{
        'form':form,
        'add':True
    })
    
    return render_to_response('add_site.html',variables)

@login_required   
def edit_site(request,site_id):
    site = get_object_or_404(Site,pk=site_id)
    
    if request.method == 'POST':
        form = SiteForm(instance = site,data=request.POST)
        
        if form.is_valid():
            site = form.save()
            
            return HttpResponseRedirect('/sites/')
            
    else:
        form = SiteForm(instance=site)
        
    variables = RequestContext(request,{
        'form':form,
        'add':False
    })
    
    return render_to_response('add_site.html',variables)
    
def region_engineers(request,region_id):
    region = get_object_or_404(Region,pk=region_id)
    
    #retrieve engineers in given region
    
    engineers = region.fieldengineer_set.all()
    
    variables = RequestContext(request,{
        'engineers':engineers,
        
        
    })
    
    return render_to_response('engineers.html',variables)
    
def engineer_tickets(request,engineer_id):
    engineer = get_object_or_404(FieldEngineer,pk=engineer_id)
    
    #retrieve tickets assigned to the engineer
    
    tickets = engineer.ticket_set.all()
    
    variables = RequestContext(request,{
        'tickets':tickets
    })
    
    return render_to_response('ticket_list.html',variables)
    
def site_tickets(request,site_id):
    site = get_object_or_404(Site,pk=site_id)
    
    #retrieve tickets belonging to a given site
    
    tickets = site.ticket_set.all()
    
    variables = RequestContext(request,{
        'tickets':tickets
    })
    
    return render_to_response('ticket_list.html',variables)
    
def category_tickets(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    
    #retrieve tickets belonging to a specific category
    
    tickets = category.ticket_set.all()
    
    variables = RequestContext(request,{
        'tickets':tickets
    })
    
    return render_to_response('ticket_list.html',variables)
    

        
    

