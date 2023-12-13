from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('record/<int:pk>',views.CustomerRecord, name='record'),
    path('delete/<int:pk>', views.DeletePage,name='delete'),
    path('delete_record/<int:pk>',views.DeleteRecord, name='delete_record'),
    path('add_record',views.AddRecord, name='add_record'),
    path('update_record/<int:pk>',views.UpdateRecord, name='update_record'),
]
