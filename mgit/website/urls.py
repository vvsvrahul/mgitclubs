from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [

        path('',views.home,name='home1'),
        path('Home',views.Home,name='home'),
        path('spotlight',views.spotlight,name='spotlight'),
        path('dop',views.photo,name='dop'),
        path('literary',views.literary,name='literary'),
        path('login/',views.userlogin,name='login'),
        # path('user/<int:pk>/',views.userinfo,name='user'),
        path('user/',views.userinfo1,name='userinfo'),
        path('logout/',views.userlogout,name='logout'),
        path('registraion/',views.registration,name='signup'),
        path('literary/newpost/',views.newposter,name='newpost'),
        path('literary/newpost/comment/<int:pk>/',views.comments,name='comments'),
        path('literary/publish/<int:pk>/',views.publish,name='publish'),
        path('music/',views.comming,name='comming'),
        path('dance/',views.comming,name='comming1'),




]
