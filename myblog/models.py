from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


from ckeditor.fields import RichTextField


class Category(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
        # return reverse('article-detail',args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio =  models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url = models.CharField(max_length=255,null=True,blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')




class Post(models.Model):
    title=models.CharField(max_length=30)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField(null=True,max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(max_length=300,blank=True,null=True)
    #body=models.TextField()
    post_date=models.DateField(null=True,auto_now_add=True)
    category=models.CharField(max_length=300,default='coding')
    snippet=models.CharField(max_length=300)
    likes=models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        #return reverse('article-detail',args=(str(self.id)))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateField(null=True,auto_now_add=True)




    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)