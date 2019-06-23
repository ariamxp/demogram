# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Local
from platzigram import views as local_views
from users import views as user_view


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('numeros_1/', local_views.numeros_1, name='sort'),
    path('numeros_2/', local_views.numeros_2, name='sort_2'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

    #path('login/', user_view.login_view, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
