import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField()
    is_featured = models.BooleanField(default=False)
    sold = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.sold > 20
        
    def increment_sold(self):
        self.sold += 1
        self.stock -= 1
        self.save()

    def add_stock(self):
        self.stock += 1
        self.save()