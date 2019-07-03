from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.loginp),
    path('logout/', views.logout_view),
    path('ques/', include('Question.urls')),
    
]