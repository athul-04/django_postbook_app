from django.db import models
import uuid
import datetime

class User(models.Model):
    id=models.BigAutoField(primary_key=True)
    user_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    image=models.ImageField(default='default.png',upload_to='profile.pics')
    premium=models.IntegerField(default=0)


    def __str__(self):
        return self.user_name
class UserBio(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio_name=models.CharField(max_length=20,default="bio_name")
    bio=models.CharField(max_length=30,default="bio")
    links=models.CharField(max_length=30,default="links")

    def __str__(self):
        return "{}'s Bio".format(self.user.user_name)



class Uploads(models.Model):

    upload_id=models.BigAutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="user_uploads")
    content=models.CharField(max_length=50)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return "{}' s upload".format(self.user.user_name)

class Like(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upload=models.ForeignKey(Uploads,on_delete=models.CASCADE)

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    upload=models.ForeignKey(Uploads,on_delete=models.CASCADE)
    comments=models.CharField(max_length=20)
    

class Audio_uploads(models.Model):
    
    audio_id=models.BigAutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    audio=models.FileField(upload_to="audio_uploads")
    audio_name=models.CharField(max_length=50)

    def __str__(self):
        return "{}' s audio_upload".format(self.user.user_name)







