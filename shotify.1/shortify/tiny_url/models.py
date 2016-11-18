from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string
from django.contrib.sites.models import Site #for getting the domain name
from shortify.settings import SITE_URL

# Create your models here.

AUTH_TOKEN_LENGTH=15

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name= models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    auth_token=models.CharField(max_length=40, null=True)
    def __unicode__(self):
        return self.user.username

SHORT_URL_LENGTH = 6

class Url(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    full_url=models.URLField(blank=True)
    short_code=models.CharField(unique=True, max_length=6)
    hit_count=models.IntegerField(default=0)
    def __unicode__(self):
        return self.short_code +" </br> Full url: "+ self.full_url
    
    def get_short_url(self):
        return SITE_URL+self.short_code
        
@receiver(pre_save, sender=Url)
def url_pre_save_callback(sender, instance, *args, **kwargs):
    if not instance.short_code:
        while(1):
            short = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(SHORT_URL_LENGTH))
            if not Url.objects.filter(short_code=short).exists():
                break 
        instance.short_code = short
    #return short
        
        """def get_shortened_url(self):
            current_site=Site.objects.get_current()
            domain_name=current_site.domain
            #x=request.META['HTTP_HOST']
            short_url=''
            #short_url=x+short
            #strepsil=url_pre_save_callback()
            short_url=domain_name+short"""


@receiver(pre_save, sender=UserProfile)
def auth_token_pre_save_callback(sender, instance, *args, **kwargs):
    if not instance.auth_token:
        while(1):
            a_token=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(AUTH_TOKEN_LENGTH))
            if not UserProfile.objects.filter(auth_token=a_token).exists():
                break
            
        instance.auth_token=a_token
            
        
        
        """current_site=Site.objects.get_current()
        domain_name=current_site.domain
        instance.auth_token"""
    
    
    
    
    