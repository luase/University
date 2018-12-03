from django.urls import path
from . import views

app_name = 'unimng'
urlpatterns = [

    # ex: /unimgn/
    path('', views.IndexView.as_view(), name='index'),

    # ex: /unimgn/course/5
    path('course/<int:pk>/', views.CourseView.as_view(), name='course'),

    # ex: /unimgn/professor
    path('professor/', views.ProfessorList.as_view(), name='professors'),

    # ex: /unimng/professor/3
    path('professor/<int:pk>/', views.ProfessorDetail.as_view(), name='professor'),

    # ex: /unimng/schedule/2
    path('schedule/<int:pk>/', views.ScheduleDetail.as_view(), name='schedule'),

    # ex: /unimng/department/
    path('department/', views.DepartmentList.as_view(), name='departments'),

    # ex: /unimng/professor/3
    path('department/<int:pk>/',
         views.DepartmentDetail.as_view(), name='department'),

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
