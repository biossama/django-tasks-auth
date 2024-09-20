from django.urls import path, include
from . import views

app_name='tasks'

urlpatterns = [
    path('', views.index, name='home'),

    path('update/<int:pk>', views.update_task, name='update-task'),
    path('delete/<int:pk>', views.remove_task, name='remove-task'),

    path('add-task/', views.add_task, name='add-task'),

#    path('accounts/', include('django.contrib.auth.urls')),

#    path('register/', views.register, name='register'),

#    path('login/', views.login_user, name='login'),

#    path('logout/', views.logout_user, name='logout'),
]
