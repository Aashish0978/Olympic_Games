from django.db import models
from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    message = models.TextField()

class Gallery(models.Model):
    image = models.ImageField(upload_to='galleryimage/')
    
class About(models.Model):
    image = models.ImageField(upload_to='aboutimage/')
    title= models.CharField(max_length=100)
    description=RichTextField()
    ordering = models.PositiveIntegerField()

    class Meta:
        ordering=['id']

    def __str__(self):
        return self.title

class SportsCategory(models.Model):
    category_name= models.CharField(max_length=150)
    ctg_slug= AutoSlugField(populate_from='category_name',unique=True,blank=True)
    order_number= models.IntegerField()

    class Meta:
        ordering=['id']

    def __str__(self):
        return self.category_name


class Sport(models.Model):
    catagory  = models.ForeignKey(SportsCategory, on_delete=models.CASCADE, related_name='category' )
    title= models.TextField(max_length=100)
    image= models.ImageField(upload_to='blogimage/')
    description= models.TextField(max_length=10000)
    created_date= models.DateField(auto_now=True)
    blog_slug= AutoSlugField(populate_from='title',unique=True,default=None)

class News(models.Model):
    title= models.TextField(max_length=100)
    image= models.ImageField(upload_to='blogimage')
    description= models.TextField(max_length=2000)
    created_date= models.DateField(auto_now=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title

class Match(models.Model):
    sport  = models.ForeignKey(SportsCategory, on_delete=models.CASCADE, related_name='sport' )
    team_1 = models.CharField(max_length=255)
    team_2 = models.CharField(max_length=255)
    team1_image = models.ImageField(upload_to='matchimage')
    team2_image = models.ImageField(upload_to='matchimage')
    location = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
     
    class Meta:
        ordering=['id']

    # def __str__(self):
    #     return self.sport
    
class Atheletes(models.Model):
    atheletes  = models.ForeignKey(SportsCategory, on_delete=models.CASCADE, related_name='atheletes' )
    name= models.TextField(max_length=100)
    image= models.ImageField(upload_to='atheletesimage/')
    description= models.TextField(max_length=10000)
    atheletes_slug= AutoSlugField(populate_from='name',unique=True,default=None)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.name

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_detail')
    email =models.EmailField(unique=True)

class Blogs(models.Model):
    title= models.TextField(max_length=200)
    image= models.ImageField(upload_to='blogsimage')
    description= models.TextField(max_length=10000)
    date= models.DateField(auto_now=True)
    details_slug= AutoSlugField(populate_from='title',unique=True,default=None)

    class Meta:
        ordering=['id']

    def __str__(self):
        return self.title
    
class ResultsAndHighlights(models.Model):
    game=models.ForeignKey(SportsCategory, on_delete=models.CASCADE, related_name='game' )
    name=models.CharField(max_length=100)
    date=models.DateField()
    gold=models.CharField(max_length=100)
    silver=models.CharField(max_length=100)
    bronze=models.CharField(max_length=100)
    fourth=models.CharField(max_length=100)
    fifth=models.CharField(max_length=100)
    sixth=models.CharField(max_length=100)
    seventh=models.CharField(max_length=100)
    eighth=models.CharField(max_length=100)
    nineth=models.CharField(max_length=100)
    tenth=models.CharField(max_length=100)

    
class Booking(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=150)
    phone=models.PositiveIntegerField()
    email=models.EmailField()
    person =models.PositiveIntegerField()
    
class Streaming(models.Model):
    title = models.CharField(max_length=150)
    video_url = models.URLField()
    # video = models.FileField(upload_to='video')


    class Meta:
        ordering =['-id']

    def _str_(self):
        return self.title
    
class Comment(models.Model):
    video = models.ForeignKey(Streaming, on_delete=models.CASCADE, related_name='videos')
    person =models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    comments = models.TextField()


    class Meta:
        ordering =['-id']




    



