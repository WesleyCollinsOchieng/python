from django.urls import path
from . import views

app_name = 'healthp'
urlpatterns=[
    path('',views.MemberListView.as_view(), name='index'),
    path('add-member',views.MemberCreateView.as_view(), name='add-member'),
    path('<int:pk>/update', views.MemberUpdateView.as_view(), name='update-members'),
    path('<int:pk>/delete', views.MemberDeleteView.as_view(), name='delete-members'),
]