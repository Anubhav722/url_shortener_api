from django.conf.urls import url, include
from tiny_url import views


urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^shorten/$', views.short, name='shorten'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^shorten/(?P<short>[0-9,a-z,A-Z]+)/$', views.redirect_short_url, name='redirect_short_url'),
    
    url(r'^api/shorten$', views.api_short, name='api_shorten'),
    url(r'^api/list$', views.short_user_list, name='short_user_list'),
    url(r'^api/longer/(?P<short>[0-9,a-z,A-Z]+)/$', views.short_to_long, name='short_to_long'),
    #url(r'^api/)
]