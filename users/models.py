from django.db import models
from django.contrib.auth.models import User

from PIL import Image
# Create your models here.
# to create custom profile need to extend default User models
# to access this via user 
# we can just do user.profile because one-to-one
class Profile(models.Model):
    
    # one profile one user (vice-versa)
    # CASCASE (if user deleted, profile deleted) [one-way]
    # but if profile deleted, user not deleted 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    # profile pics is directory that images will be uploaded to (for image field)
    image = models.ImageField(upload_to='profile-pics',default='default.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        
        # open image from path
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            # overwrite the image on path
            img.save(self.image.path)
        
        
    
# accessing image we use image location: image.url attribute