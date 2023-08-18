from django.urls import path
from . import views

# all the url paths user can go to 
urlpatterns =[
    path('', views.home, name='homepage'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/delete/<int:card_id>/', views.delete_card, name='delete_card'),
    path('accounts/profile/', views.add_card, name='add_card'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
]