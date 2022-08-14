from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# a Post model use for database (kind of one table of Post)
# to query all post object (in the table) we do Post.objects.all()
# to access first object from query we do query_obj.first()
# to filter, <model_name>.objects.filter(<model_field>="<value>")
# to get all post by user, we do user.post_set.all()

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return "{} by {}".format(self.title, self.author.username)