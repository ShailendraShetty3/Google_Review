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
    

class Post_Meta(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=200)
    meta_value = models.CharField(max_length=200)  


class Users(models.Model):
    # id = models.AutoField()
    user_login = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200) 
    user_email = models.EmailField()  
    user_password = models.CharField(max_length=200) 
    # user_status = models.BinaryField(default=False) 


class Comment(models.Model):
    # id = models.AutoField()
    comment_date = models.DateField(null=True, blank=True, default=None)
    post_name = models.CharField(max_length=200)
    # comment_post_id = models.ManyToManyField(Posts, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=200) 
    comment_author_email = models.EmailField() 
    comment_post = models.ForeignKey(Posts, on_delete=models.CASCADE)  # Assuming you meant ForeignKey instead of ManyToManyField
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    


