from django.db import models
from user.models import RandomUserModel

class Post(models.Model):
    view = models.IntegerField(default=0)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    numberOfDistribution = models.IntegerField(default=0)
    # createBy = models.ForeignKey(RandomUserModel, null=True,on_delete=models.CASCADE)

    class Meta:
        ordering = ['time']

