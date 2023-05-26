from django.db import models

# Create your models here.
"""A store will be linked to a niche and a category will be linked to a niche as well 
example niche :clothing items
categories under clothing items -> footwears, bodywears.
when a user clicks on the create store button they give it a name and they a
preset set of niches available to choose from if not available they can add it 
"""
class Niche(models.Model):
    name = models.CharField(max_length = 50)
    no_of_merchants = models.IntegerField()
class Store(models.Model):
    owner = models.CharField(max_length=100)
    niche = models.ForeignKey(Niche,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length = 100)
    niche = models.ForeignKey(Niche,on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    def isEmpty(self):
        return self.no_of_items == 0
    orderCount = models.IntegerField()

    
class Cart(models.Model):
    # this variable will serve as the name of the shopper so we can have a reciept when someone is done shopping we can ge the name, the items they bought, the total price all from this model in the spirit of getting a transaction history we should probably save all of this information in a reciept model
    shopper = models.CharField(max_length = 200 )
    no_of_items = models.IntegerField()
    total_price = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    """active variable acts as a shopping session
    so we don't need the session model when a shopper checks out we declare
    the cart inactive so we only create a new cart if there is no inactive 
    cart and we delete carts every now and then"""
    active = models.BooleanField()
class Receipt(models.Model):
    shopper = models.CharField(max_length = 200)
    no_of_items = models.IntegerField()
    total_price = models.IntegerField()
    
class Item(models.Model):
    name = models.CharField(max_length = 200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    associated_cart = models.ManyToManyField(Cart)
    price  = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField()

#instanceofstore.

