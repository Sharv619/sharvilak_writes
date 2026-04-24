from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Built-in Django User model

class Post(models.Model):
    # 1. Heading (like a VARCHAR in SQL)
    title = models.CharField(max_length=200)
    
    # 2. The body of the blog (Unlimited text)
    content = models.TextField()
    
    # 3. Timestamps (automatically handled)
    date_posted = models.DateTimeField(default=timezone.now)
    
    # 4. Relationship (JS equivalent: foreign key/reference)
    # If the user is deleted, their posts are deleted (on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """This tells Django what to print in the Admin panel (The Title)"""
        return self.title