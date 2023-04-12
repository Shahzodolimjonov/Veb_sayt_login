from  django.urls import path

from configapp.views import index, category, detail, n_del,loginPase,registerPage,logoutUser

urlpatterns = [
    path('index/', index,name='home'),
    path('category/<int:pk>/', category,name='category'),
    path('detail/<int:pk>/', detail,name='detail'),
    path('n_del/<int:pk>/', n_del, name='n_del'),
    path('register/', registerPage, name='register'),
    path('login/', loginPase, name='login'),
    path('logout/', logoutUser, name='logout'),
]