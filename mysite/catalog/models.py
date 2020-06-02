from django.db import models
from django.contrib.auth.models import User
# Required to assign User as a borrower
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import Sum
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.


class Person(models.Model):
    """ Модель, представляющая человека, пользователя сайта. """
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=128)
    mail = models.EmailField(max_length=128)
    password = models.CharField(max_length=128, default="")

    def get_absolute_url(self):
        """Возвращает url - адрес для доступа к определенному экземпляру person."""
        return reverse('person-detail', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта модели."""
        return '%s, %s' % (self.surname, self.name)


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def books(self):
        return self.get_queryset().all()


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )
    vote = models.SmallIntegerField(choices=VOTES)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    objects = LikeDislikeManager()


class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512, default="HHHH")
    publication_date = models.PositiveSmallIntegerField(null=True, blank=True)
    publisher = models.TextField(max_length=512)
    possibility = models.TextField(max_length=64, default="есть")
    wishes = models.CharField(max_length=512, default="")
    personid = models.ForeignKey('Person', on_delete=models.CASCADE)
    votes = GenericRelation(LikeDislike, related_query_name='books')

    def get_absolute_url(self):
        """Возвращает url - адрес для доступа к определенному экземпляру book."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта модели."""
        return self.title

