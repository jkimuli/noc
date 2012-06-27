# Create your views here.

from datetime import datetime
from django.contrib.auth.models import User
from issue_tracker.models import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from issue_tracker.forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login


def main_page(request):
    
    tickets = Ticket.objects.all()
    
    editable = True
    
    for ticket in tickets:
        if ticket.status =='1':
            editable = False
            
    variables = RequestContext(request,{
        'tickets' : tickets,
        'user' : request.user,
        'editable':editable
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
        form = TicketForm(request.POST)
        
        if form.is_valid:
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
        form = TicketForm(instance=ticket,data=request.POST)
        
        #update the ticket in database
        
        if form.is_valid():
            ticket = form.save(commit=False)
            
            if request.POST['status'] == '1':
                #close ticket by setting close time
                
                ticket.close_time = datetime.now()
                
                ticket.save()
            
            #redirect to home page
            
            return HttpResponseRedirect('/')
            
    else:
        form = TicketForm(instance = ticket)
        
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
        'regions':regions
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
    

