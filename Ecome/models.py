from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category_Type =(
        ('Electronics','Electronics'),
        ('Clothing','Clothing'),
        ('Home Appliances','Home Appliances'),
        ('Books','Books'),
        ('Furniture','Furniture'),
        ('Sports','Sports'),
        ('Others','Others'),
    )
    category = models.CharField(max_length=50, choices=category_Type, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="Ecome/images", default="")

    def __str__(self):
        return self.product_name
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    prodect = models.ForeignKey(Product, on_delete=models.CASCADE)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111)
