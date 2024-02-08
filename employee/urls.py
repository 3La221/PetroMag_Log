from django.urls import path,include
from .views import home , test,read


urlpatterns = [
    path('',home,name="home"),
    path('test/',test,name="test"),
    path('read/',read , name="read")
]
