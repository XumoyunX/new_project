from django.db import models




class Categoriya(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Productos(models.Model):
    NEW = 0
    OLD = 1

    category = models.ForeignKey(Categoriya, on_delete=models.CASCADE, null=True)
    img =  models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_de = models.BooleanField()

    def __str__(self):
        return self.name
    account_type = models.SmallIntegerField(choices=(
        (NEW, "Yangi"),
        (OLD, "Eski ")

    ), blank=True, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
