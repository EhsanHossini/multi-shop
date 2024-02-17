from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
# from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


# Size cart
class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'


#  Color cart article
class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="image/")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")
    category = models.ManyToManyField(Category, blank=True, null=True, related_name="categories")
    offer = models.CharField(_("offer"), max_length=50, blank=True, null=True)
    times = models.DateTimeField(_("times"), auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Information(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="information")
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    number = models.IntegerField(_("Number"))
    subject = models.CharField(_("subjects"), max_length=100)
    body = models.TextField(_("message"))

    def __str__(self):
        return self.number

# class Product(models.Model):
#     title = models.CharField(max_length=30)
#     # description = RichTextField()
#     short_description = models.TextField(blank=True)
#     price = models.IntegerField()
#     active = models.BooleanField(default=True)
#     discount = models.SmallIntegerField()
#     image = models.ImageField(upload_to='products')
#     size = models.ManyToManyField(Size, blank=True, null=True, related_name='products')
#     color = models.ManyToManyField(Color, related_name='products')
#     datetime_created = models.DateTimeField('Date Time of Creation', default=timezone.now)
#     datetime_modified = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('product_detail', args=[self.pk])
#
#
# class ActiveCommentsManger(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentsManger, self).get_queryset().filter(active=True)
#
#
# class Comment(models.Model):
#     PRODUCT_STARS = [
#         ('1', 'Very Bad'),
#         ('2', 'Bad'),
#         ('3', 'Normal'),
#         ('4', 'Good'),
#         ('5', 'Perfect'),
#     ]
#
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', )
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#         related_name='comments',
#         verbose_name='Comment author'
#     )
#     body = models.TextField(verbose_name='Comment Text')
#     stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name='What is your score?')
#
#     datetime_created = models.DateTimeField(auto_now_add=True)
#     datetime_modified = models.DateTimeField(auto_now=True)
#
#     active = models.BooleanField(default=True)
#
#     # Manager
#     objects = models.Manager()
#     active_comments_manager = ActiveCommentsManger()
#
#     def get_absolute_url(self):
#         return reverse('product_detail', args=[self.product.id])

# class Information(models.Model):
#     product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='informations')
#     text = models.TextField
#
#     def __str__(self):
#         return self.text[:30]

#
# class Contact(models.Model):
#     name = models.CharField(_("Name"), max_length=100)
#     phone = models.EmailField(_("phone"))
#     subject = models.CharField(_("subjects"), max_length=100)
#     body = models.TextField(_("message"))
#
#     def __str__(self):
#         return self.phone