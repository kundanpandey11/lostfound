from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
    path('', views.index),
    path('lostform/', views.createlostitem, name="createlostitem"),
    path('foundform/', views.createfounditem, name="createfounditem"),
    path('about/', views.about, name='about'),
    path('lostitem/<int:id>/', views.lostitemdetails, name="lostitemdetails"),
    path('founditem/<int:id>/', views.founditemdetails, name="founditemdetails"),
    path('<int:pk>/delete/lostitem/', views.deletelostitems.as_view(), name="deletelostitem"),
    path('delete/<int:pk>/founditem/', views.deletefounditems.as_view(), name="deletefounditem"),



    path('founditem/', views.founditemlist, name='founditemlist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)