from django.contrib import admin
from . models import (Contact, About, 
                      Sport, SportsCategory, 
                      News, Match, Comment,
                      Atheletes, Blogs, 
                      Booking,Gallery, Streaming,ResultsAndHighlights, UserDetails )
# Register your models here.
admin.site.register(SportsCategory)

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    list_display=['id','name','message']
admin.site.register(Contact,ContactAdmin)

class GalleryAdmin(admin.ModelAdmin):
    model=Gallery
    list_display=['id','image']
admin.site.register(Gallery,GalleryAdmin)

class AboutAdmin(admin.ModelAdmin):
    model=About
    list_display=['id','image', 'title', 'description']
admin.site.register(About,AboutAdmin)

class SportAdmin(admin.ModelAdmin):
    model=Sport
    list_display = ['id', 'title', 'catagory', 'image', 'description', 'created_date']
admin.site.register(Sport,SportAdmin)

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ['id', 'title', 'image', 'description', 'created_date']
admin.site.register(News,NewsAdmin)

class MatchAdmin(admin.ModelAdmin):
    model = Match
    list_display = ['sport', 'team_1', 'team_2', 'team1_image', 'team2_image', 'location', 'date']
admin.site.register(Match,MatchAdmin)

class ResultsAndHighlightsAdmin(admin.ModelAdmin):
    model= ResultsAndHighlights
    list_display=['id', 'game','name', 'gold','silver','bronze','fourth','fifth','sixth','seventh','eighth','nineth','tenth']
admin.site.register(ResultsAndHighlights,ResultsAndHighlightsAdmin)

class AtheletesAdmin(admin.ModelAdmin):
    model = Atheletes
    list_display = ['name', 'image', 'atheletes', 'description']
admin.site.register(Atheletes,AtheletesAdmin)

class BlogsAdmin(admin.ModelAdmin):
    model = Blogs 
    list_display = ['title', 'image', 'description', 'date']
admin.site.register(Blogs,BlogsAdmin)

class BookingAdmin(admin.ModelAdmin):
    model = Booking 
    list_display = ['id', 'firstname', 'lastname', 'country', 'city', 'phone', 'email','person']
admin.site.register(Booking, BookingAdmin)

class StreamingAdmin(admin.ModelAdmin):
    model= Streaming
    list_display=['id','title','video_url']
admin.site.register(Streaming,StreamingAdmin)

class UserDetailsAdmin(admin.ModelAdmin):
    model= UserDetails
    list_display=['id','user','email']
admin.site.register(UserDetails,UserDetailsAdmin)

class CommentAdmin(admin.ModelAdmin):
    model= Comment
    list_display=['video','person']
admin.site.register(Comment,CommentAdmin)