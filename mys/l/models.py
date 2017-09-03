from django.db import models

# Create your models here.

# Image Classes

# TODO: change image_name to be primary key
class ImageDetails(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=100,default='')
    char_names = models.CharField(max_length=50,default='')
    time_added = models.DateTimeField()
    path = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.path
    
class ImageTag(models.Model):
    image_id = models.ForeignKey(ImageDetails,on_delete=models.CASCADE)
    tag = models.CharField(max_length=20,default='')
    def __str__(self):
        return str(self.image_id)


# User Classes

class User(models.Model):
      username = models.CharField(max_length=20,unique=True)
      password = models.CharField(max_length=20)

# Related Classes

class ImageComment(models.Model):
    image_id = models.ForeignKey(ImageDetails,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User)
    comment = models.CharField(max_length=300,default='')

