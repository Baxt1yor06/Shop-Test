from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name='category_nomi',max_length=100)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    title = models.CharField(verbose_name='product_nomi',max_length=100)
    description = models.TextField(verbose_name='product_haqida')
    price = models.DecimalField(verbose_name='narxi',decimal_places=2,max_digits=12)
    discount = models.PositiveSmallIntegerField(verbose_name='foizi')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name='product_rasmi',upload_to='products/',blank=True,null=True)
    count = models.PositiveIntegerField(verbose_name='product_soni',default=1)

    def discount_price(self):
        return self.price - (self.price * self.discount / 100)


    def __str__(self):
        return self.title
    

class Contact(models.Model):
    GENDER_CHOISE = (
        ('M', 'Erkak'),
        ('F', 'Ayol'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOISE, default='Erkak')
    message = models.TextField()