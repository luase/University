from django.urls import path
from . import views

app_name = 'unimng'
urlpatterns = [

    # ex: /unimgn/
    path('', views.IndexView.as_view(), name='index'),

    # # ex: /events/user/23
    # path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    #
    # # ex: /events/user/23/followers
    # path('user/<int:pk>/followers',
    #      views.UserViewFollowers.as_view(), name='user_followers'),
    #
    # # ex: /events/user/23/following
    # path('user/<int:pk>/following',
    #      views.UserViewFollowing.as_view(), name='user_following'),
    #
    # # ex: /events/84
    # path('<int:pk>/', views.MeetUpView.as_view(), name='meetup'),
    #
    # # # ex: /events/user/create
    # # path('user/<int:pk>/create', views.Create, name='create'),

]
