
from django.urls import path
from mysite.views import  mydata, sentdata ,removedata

urlpatterns = [
    path('removedata/',removedata, name='removedata'),
    path('mydata/',mydata, name='mydata'),
    path('sentdata/',sentdata, name='sentdata'),
]