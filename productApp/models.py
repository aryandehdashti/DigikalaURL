from django.db import models
import requests
import json
# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.title 


    def GetProducts(url):
        for i in url.split("/"):
            if i.startswith("category-"):
                category = i[9:]
        api = f'https://api.digikala.com/v1/categories/{category}/search/'
        r = requests.get(api)
        data = json.loads(r.text)
        jsonProducts = data['data']['products']
        for jsonproduct in jsonProducts:
            p1 = Product(title=jsonproduct['title_fa'],
                    brand=jsonproduct['data_layer']['brand'],
                    price=jsonproduct['default_variant']['price']['selling_price'])
            p1.save()
      