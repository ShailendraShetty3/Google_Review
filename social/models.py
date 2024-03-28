from django.db import models

class Posts(models.Model):
    # id = models.AutoField()
    post_author = models.CharField(max_length=200)
    post_date = models.DateField(null=True, blank=True, default=None)
    post_name = models.CharField(max_length=200)
    post_status = models.CharField(max_length=200) 
    post_type = models.CharField(max_length=200) 
    comment_count = models.IntegerField() 
    like_count = models.IntegerField() 
    

    def __str__(self):
        return self.post_name