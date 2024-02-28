import datetime
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.humanize.templatetags import humanize



class Service(models.Model):
     service = models.CharField(max_length=100)
     def __str__(self):
      return f"{self.service}"
class State(models.Model):
    State = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"{self.State}"

class postads(models.Model):
    name = models.CharField(max_length=300,)
    email = models.EmailField( max_length=254,null=False, blank=False )
    number = PhoneNumberField(blank=False, null=False )
    whatsapp = PhoneNumberField(blank=True, null=True )
    telegram = PhoneNumberField(blank=True, null=True )
    main = models.ImageField(null=False, blank=False)
    picture1 = models.ImageField(null=False, blank=False)
    picture2 = models.ImageField(null=False, blank=False)
    picture3 = models.ImageField(null=False, blank=False)
    bio = models.TextField(max_length=3000)
    State = models.ForeignKey(State, on_delete=models.CASCADE, null=False, blank=False)
    date_post = models.DateTimeField(auto_now=True)
    shot_time = models.DecimalField(max_digits=10, decimal_places=2)
    full_night = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    view_count = models.PositiveIntegerField(default=0)
    video = models.FileField(blank=True, null=True, upload_to='videos/')
    service = models.ManyToManyField(Service)
    suspended = models.BooleanField(default=False)
    verification = models.BooleanField(default=False)
    def formatted_shot_time(self):
        return humanize.intcomma(self.shot_time)

    def formatted_full_night(self):
        return humanize.intcomma(self.full_night)
    
    def __str__(self):
       return f"{self.name} - Posted by {self.author}"
class verify_Post(models.Model):
    Post = models.ForeignKey(postads, on_delete=models.CASCADE)
    Picture_With_ID = models.ImageField(null=False, blank=False)
    ID_Front = models.ImageField(null=False, blank=False)
    def __str__(self):
       return f" verification for {self.Post}"
    
    
class adsvideos(models.Model):
    name = models.CharField(max_length=300,)
    email = models.EmailField( max_length=254,null=False, blank=False )
    number = PhoneNumberField(blank=False, null=False )
    whatsapp = PhoneNumberField(blank=True, null=True )
    telegram = PhoneNumberField(blank=True, null=True )
    video = models.FileField(blank=True, null=True, upload_to='videos/')
    bio = models.TextField(max_length=3000)
    State = models.ForeignKey(State, on_delete=models.CASCADE, null=False, blank=False)
    date_post = models.DateTimeField(auto_now=True)
    shot_time = models.DecimalField(max_digits=10, decimal_places=2)
    full_night = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    service = models.ManyToManyField(Service)
    view_count = models.PositiveIntegerField(default=0)
    suspended = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.name}''''Posted by''''{self.author}"

    
class review(models.Model):
    ads = models.ForeignKey(postads, related_name='reviews',  on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    body = models.TextField(max_length=1000)
    date_post = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s - %s' %(self.ads.name, self.name)
    
    
class videosreview(models.Model):
    video = models.ForeignKey(adsvideos, related_name='videoreviews',  on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    body = models.TextField(max_length=1000)
    date_post = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s - %s' %(self.video.name, self.name)

class Report(models.Model):
    name = models.CharField(max_length=300)
    reported_post = models.ForeignKey(postads, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
class slide(models.Model):
    list = models.CharField(max_length=300)
    picture = models.ImageField()
    
    def __str__(self):
        return self.list
      
class slide2(models.Model):
    list = models.CharField(max_length=300)
    picture = models.ImageField()
    
    def __str__(self):
        return self.list
class slide3(models.Model):
    list = models.CharField(max_length=300)
    picture = models.ImageField()
    
    def __str__(self):
        return self.list
           
