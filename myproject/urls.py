from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from core import views, urls
from django.core.urlresolvers import reverse_lazy, reverse

urlpatterns = [
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^registro/$', views.register, name='register'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'', include('myproject.core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
]