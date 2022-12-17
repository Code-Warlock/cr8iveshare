from django.db import models
# from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from accounts.models import Account


class PageContents(models.Model):
    page_name = models.CharField(max_length=20, default="SplitUnity")
    navbar_logo = models.ImageField(
        upload_to='page_contents/', null=True, blank=True, default="https://dummyimage.com/99x24")
    footer_logo = models.ImageField(
        upload_to='page_contents/', null=True, blank=True, default="https://dummyimage.com/99x24")
    footer_description = models.CharField(
        max_length=500, null=True, blank=True, default="Lorem ipsum dolor sit amet consectetur adipiscing elit platea convallis tortor, et laoreet posuere nisi suspendisse mollis gravida facilisi fusce cras, augue dictumst tempor imperdiet lacus risus neque elementum nisl.")
    footer_address = models.CharField(
        max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet consectetur, adipiscing elit platea nec.")
    footer_phone = models.CharField(max_length=20, null=True, blank=True, default="+123456789")
    footer_email = models.CharField(max_length=50, null=True, blank=True, default="lorem@lorem.com")
    social_icon_1 = models.CharField(
        max_length=30, null=True, blank=True, default="twitter")
    social_icon_url_1 = models.URLField(
        max_length=200, default='https://google.com')
    social_icon_2 = models.CharField(
        max_length=30, null=True, blank=True, default="facebook")
    social_icon_url_2 = models.URLField(
        max_length=200, default='https://google.com')
    social_icon_3 = models.CharField(
        max_length=30, null=True, blank=True, default="youtube")
    social_icon_url_3 = models.URLField(
        max_length=200, default='https://google.com')
    social_icon_4 = models.CharField(
        max_length=30, null=True, blank=True, default="instagram")
    social_icon_url_4 = models.URLField(
        max_length=200, default='https://google.com')
    updated = models.DateTimeField(auto_now=True)
    footer_social_icon_1 = models.CharField(
        max_length=30, null=True, blank=True, default="facebook-f")
    footer_social_icon_url_1 = models.URLField(
        max_length=200, default='https://google.com')
    footer_social_icon_2 = models.CharField(
        max_length=30, null=True, blank=True, default="twitter")
    footer_social_icon_url_2 = models.URLField(
        max_length=200, default='https://google.com')
    footer_social_icon_3 = models.CharField(
        max_length=30, null=True, blank=True, default="instagram")
    footer_social_icon_url_3 = models.URLField(
        max_length=200, default='https://google.com')
    footer_social_icon_4 = models.CharField(
        max_length=30, null=True, blank=True, default="youtube")
    footer_social_icon_url_4 = models.URLField(
        max_length=200, default='https://google.com')
    updated = models.DateTimeField(auto_now=True)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    tag = models.CharField(max_length=100, blank=True)
    caption = models.TextField()
    created_at = models.DateTimeField(
        verbose_name='date created', auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        slug = self.caption
        if not self.slug:
            self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class DisLikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    followers = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class ViewsCount(models.Model):
    followers = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"{self.user}  ---  {self.comment}"

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = self.name
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
