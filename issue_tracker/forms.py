#!/usr/bin/env python

from issue_tracker.models import Ticket
from django.forms import ModelForm

class TicketForm(ModelForm):
    class Meta:
        model = Ticket




