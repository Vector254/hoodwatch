from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('register/', views.register, name='register'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/', views.profile, name='profile'),
    url('hoods/', views.hoods, name='hoods'),
    url(r'join/(\d+)', views.join, name='join-hood'),
    url(r'leave/(\d+)', views.leave, name='leave-hood'),
    url(r'hood/(\d+)', views.my_hood, name='my-hood'),
    url(r'business/(\d+)', views.business, name='hood-business'),
    url(r'contacts/(\d+)', views.contacts, name='hood-contacts'),
    url(r'announcements/(\d+)', views.announcements, name='announcements'),
    url(r'^search/', views.search_results, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
