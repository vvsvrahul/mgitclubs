from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class BlogContent(models.Model):
#         user = models.OneToOneField(User,on_delete=models.CASCADE)
#         Title = models.CharField(max_length = 20)
#         content = models.CharField(max_length=5000)
#         def __str__():
#             return self.user.username
#

class Mgituser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Roll_number = models.CharField(max_length = 10)

    def __str__(self):
        return self.Roll_number

class BlogContent11(models.Model):


    user  = models.ForeignKey(User,related_name='stories',on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    story = models.CharField(max_length=5000)
    publish = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


class PublishUser(models.Model):
    title = models.CharField(max_length = 50)
    story = models.CharField(max_length=5000)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class CommentUser(models.Model):
    post = models.ForeignKey(PublishUser,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    def __str__(self):
        return self.post.title
