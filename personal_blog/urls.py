from django.contrib import admin
# from django.contrib.auth import views as auth_views  # TODO: uncomment when adding auth
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # TODO: auth later
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # TODO: auth later
    path('', include('blog.urls')),
]
