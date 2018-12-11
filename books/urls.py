from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='homie'),
    path('<int:book_id>/',views.bookdet,name='bookie'),
]
