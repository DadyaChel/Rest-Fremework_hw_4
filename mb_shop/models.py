from django.db import models


class Firma(models.Model):
    name = models.CharField(max_length=99)
    address = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=99)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=99)
    product_sum = models.IntegerField()
    firm = models.ForeignKey(Firma, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Firma(models.Model):
#     name = models.CharField(max_length=99)
#     address = models.CharField(max_length=222)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     category_name = models.CharField(max_length=99)
#
#     def __str__(self):
#         return self.category_name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=99)
#     product_sum = models.IntegerField()
#     firm = models.ForeignKey(Firma, on_delete=models.CASCADE, verbose_name='firma')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
#
#     def __str__(self):
#         return self.name
