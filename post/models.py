from django.db import models
from user.models import RandomUser
# from django.contrib.auth.models import User
class Post(models.Model):
    view = models.IntegerField(default=0)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    numberOfDistribution = models.IntegerField(default=0)
    createBy = models.ForeignKey(RandomUser, null=True,on_delete=models.CASCADE, related_name='createBy')
    distributeUser = models.ManyToManyField(RandomUser, related_name='distributeUser')

    @property
    def getComment(self):
        print(self.comment_set.all())
        return self.comment_set.all()

    class Meta:
        ordering = ['time']

    


# class DistributePost(models.Model):
#     post_id = 
