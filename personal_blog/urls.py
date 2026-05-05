from django.contrib import admin
# from django.contrib.auth import views as auth_views  # TODO: uncomment when adding auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # TODO: auth later
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # TODO: auth later
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
