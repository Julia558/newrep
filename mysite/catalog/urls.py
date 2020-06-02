from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from catalog import views
from django.conf.urls import url
from catalog.models import LikeDislike, Book


"""urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^addbook/$', views.addbook, name='addbook'),
url(r'^books/$', views.books, name='books'),
url(r'^enter/$', views.enter, name='enter'),
url(r'^enter/person/$', views.person, name='person'),
url(r'^inform/$', views.inform, name='inform'),
url(r'^registration/$', views.create, name='registration'),
]"""


urlpatterns = [
     path('', views.index, name='index'),
     path('books', views.books, name='books'),
     path('addbook', views.addbook, name='addbook'),
     path('enter', views.enter, name='enter'),
     path('inform', views.inform, name='inform'),
     path('inform/<int:uid>', views.bookinform, name='bookinform'),
     path('inform/<int:pk>/like/', views.VotesView.as_view(vote_type=LikeDislike.LIKE), name='book_like'),
     path('inform/<int:pk>/dislike/', views.VotesView.as_view(vote_type=LikeDislike.DISLIKE),
          name='book_dislike'),
     path('person', views.person, name='person'),
     path('favourites', views.favourites, name='favourites'),
     path('registration', views.registration, name='registration'),
]
