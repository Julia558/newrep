from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Book, Person, LikeDislike
import json
from django.views import View
from django.contrib.contenttypes.models import ContentType


# Create your views here.


def index(request):
    return render(request, 'index.html')


def addbook(request):
    if request.method == "POST":
        book = Book()
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_date = request.POST.get("publication_date")
        book.publisher = 'АСТ'
        book.possibility = request.POST.get("possibility")
        book.wishes = request.POST.get("wish")
        lg = request.POST.get("phone")
        psw = request.POST.get("password")
        per = Person.objects.filter(phone='89066109491')
        book.personid = per[0]
        book.save()
        return render(request, "person.html", {"person": person})
    else:
        return render(request, "addbook.html")


def person(request):
    return render(request, 'person.html')


def favourites(request):
    return render(request, 'favourites.html')


def books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', {'book_list': book_list})


def enter(request):
    if request.method == "POST":
        lg = request.POST.get("phone")
        psw = request.POST.get("password")
        per = Person.objects.filter(phone=lg, password=psw)
        print(per)
        if per.exists():
            return render(request, 'person.html', {'per': per})
        else:
            return render(request, 'enter.html')
    else:
        return render(request, 'enter.html')


def inform(request):
    book = Book.objects.get(id=2)
    pers = Person.objects.get(id=book.personid_id)
    return render(request, 'inform.html', {"book": book, "pers": pers})


def bookinform(request, uid=0):
    book = Book.objects.get(id=uid)
    pers = Person.objects.get(id=book.personid_id)
    return render(request, 'inform.html', {"book": book, "pers": pers})


def registration(request):
    if request.method == "POST":
        per = Person()
        per.surname = request.POST.get("lastname")
        per.name = request.POST.get("name")
        per.phone = request.POST.get("phone")
        per.city = request.POST.get("city")
        per.mail = request.POST.get("mail")
        per.password = request.POST.get("password")
        per.save()
        return render(request, 'person.html', {'per': per})
    else:
        return render(request, 'registration.html')


class VotesView(View):
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        print("gkgyututut7t1132143254635")
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(object_id=obj.id)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )
