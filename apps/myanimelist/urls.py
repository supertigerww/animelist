from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$',views.success),
    url(r'^logout$',views.logout),
	url(r'^anime/(?P<id>\d+)$',views.show),
	url(r'^addcommentprocess/(?P<id>\d+)$',views.addcommentprocess),
	url(r'^addwatchlistprocess/(?P<id>\d+)$',views.addwatchlistprocess),
	url(r'^mywatchlist$',views.mywatchlist),
	url(r'^profile/(?P<id>\d+)$',views.userwatchlist),
	url(r'^delete/(?P<id>\d+)$',views.deletereview)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)