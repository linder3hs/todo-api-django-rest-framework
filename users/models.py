from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    realname = models.CharField(max_length=100)
    is_verify = models.BooleanField(default=False)
    code = models.CharField(max_length=4, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"
    
