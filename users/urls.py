#Django
from django.urls import path
from django.views.generic import TemplateView

#Views
from users import views

urlpatterns = [



    path(
        route='landing/',
        view=TemplateView.as_view(template_name='users/detail.html'),
        name='landing'
    ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='register/',
        view=views.SignupView.as_view(),
        name='register'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),

    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]
