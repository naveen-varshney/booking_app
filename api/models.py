from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class BaseModel(models.Model):
    """
    Base class for common fields
    """
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Movie(BaseModel):
    title   = models.CharField(max_length=200)
    director =  models.CharField(max_length=200,null=True,blank=True)
    duration = models.CharField(max_length=200,null=True,blank=True)
    cast = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)


    class Meta:
        app_label           = 'api'
        verbose_name        = "Movie"
        verbose_name_plural = "Movies"
        ordering            = ('-created',)

    def __str__(self):
        return ("{} : {} : {}" .format(self.id,self.title,self.description))

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','director','cast','duration','created')
    search_fields = ('id','title','director',)
    readonly_fields = ('created', 'modified',)

admin.site.register(Movie,MovieAdmin)


class Auditorium(BaseModel):
    name   = models.CharField(max_length=200)
    no_of_sheets = models.PositiveIntegerField(default=0)


    class Meta:
        app_label           = 'api'
        verbose_name        = "Auditorium"
        verbose_name_plural = "Auditoriums"
        ordering            = ('-created',)

    def __str__(self):
        return ("{} : {} : {}" .format(self.id,self.name,self.no_of_sheets))

class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('id','name','no_of_sheets','modified')
    search_fields = ('id','name',)
    readonly_fields = ('created', 'modified',)

admin.site.register(Auditorium,AuditoriumAdmin)

class Screen(BaseModel):
    auditorium   = models.ForeignKey(Auditorium,on_delete=models.CASCADE,related_name='screens')
    movie =  models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movie_screens')
    screen_start = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label           = 'api'
        verbose_name        = "Screen"
        verbose_name_plural = "Screens"
        ordering            = ('-created',)

    def __str__(self):
        return ("{} : {} : {}" .format(self.id,self.auditorium.name,self.movie.title))

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('id','auditorium','movie','screen_start','created')
    search_fields = ('id','auditorium_id','movie_id',)
    readonly_fields = ('created', 'modified',)

admin.site.register(Screen,ScreenAdmin)

class Seat(BaseModel):
    auditorium   = models.ForeignKey(Auditorium,on_delete=models.CASCADE,related_name='sheets')
    row =  models.CharField(max_length=5)
    number = models.CharField(max_length=5)

    class Meta:
        app_label           = 'api'
        verbose_name        = "Seat"
        verbose_name_plural = "Seats"
        ordering            = ('-created',)

    def __str__(self):
        return ("{} : {} : {}-{}" .format(self.id,self.auditorium.name,self.row,self.number))


class SeatAdmin(admin.ModelAdmin):
    list_display = ('id','auditorium','row','number','created')
    search_fields = ('id','auditorium_id',)
    readonly_fields = ('created', 'modified',)

admin.site.register(Seat,SeatAdmin)


class Booking(BaseModel):

    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True,blank=True, related_name='my_bookings')
    screen =  models.ForeignKey(Screen,on_delete=models.CASCADE, related_name='screen_bookings')
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE, related_name='booked_sheets')
    active = models.BooleanField(default=False)

    class Meta:
        app_label           = 'api'
        verbose_name        = "Booking"
        verbose_name_plural = "Bookings"
        ordering            = ('-created',)

    def __str__(self):
        return ("{} : {}" .format(self.id,self.screen))


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','user','screen','active','created')
    search_fields = ('id','user__username','screen_id')
    readonly_fields = ('created', 'modified',)

admin.site.register(Booking,BookingAdmin)
