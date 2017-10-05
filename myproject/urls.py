from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	# Login/Logout URLs
    # url(r'^myapp/$', HomeView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'', include('myproject.core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
]