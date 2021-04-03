from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    class Post_type(models.TextChoices):
        BOAST = "Boast", _("Boast")
        ROAST = "Roast", _("Roast")

    post_type = models.CharField(
        max_length=10,
        choices=Post_type.choices,
        default=Post_type.BOAST,
    )

    body = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)
    DisplayFields = ["body", "upvotes", "downvotes", "post_date", "overall_votes"]

    def __str__(self):
        return self.post_type

    @property
    def overall_votes(self):
        return self.upvotes - self.downvotes
