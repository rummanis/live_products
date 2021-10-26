from django.db import models

class GeeksModel(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image_main=models.ImageField(upload_to='pics')
    image_1=models.ImageField(upload_to='pics')
    image_2=models.ImageField(upload_to='pics')
    image_link = models.URLField(max_length = 200)
    image_link_1 = models.URLField(max_length = 200)
    image_link_2 = models.URLField(max_length = 200)
    category = models.CharField(max_length=200, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
