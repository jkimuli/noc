from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='Categories'
    
class Site(models.Model):
    site_code = models.CharField(max_length=15,unique=True)
    location = models.CharField(max_length=50)
    lat = models.FloatField(blank=True,null=True)
    lng = models.FloatField(blank=True,null=True)
    
    def __unicode__(self):
        return self.site_code
    
    class Meta:
        ordering = ['site_code']
    
class Region(models.Model):
    name = models.CharField(max_length=20,unique=True)
    
    def __unicode__(self):
        return self.name
    
class FieldEngineer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=15,unique=True)
    alternatePhoneNo = models.CharField(max_length=15,blank=True)
    region = models.ForeignKey(Region)
    
    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
        
    
    class Meta:
        ordering = ['first_name']
        
    
class Ticket(models.Model):
    description = models.TextField()
    site_code = models.ForeignKey(Site)
    category = models.ForeignKey(Category)
    assigned_by = models.ForeignKey(User,editable=False)
    assigned_to = models.ForeignKey(FieldEngineer)
    start_time = models.DateTimeField(auto_now_add=True)
    close_time = models.DateTimeField(blank=True,null=True,editable=False)
    status = models.CharField(max_length=15,choices=(('0','Open'),('1','Closed')),default='0')
    
    
    
    
