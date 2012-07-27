#!/usr/bin/env python

from issue_tracker.models import Ticket,Site
from django.forms import ModelForm

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        
    
class SiteForm(ModelForm):
    class Meta:
        model = Site
        




