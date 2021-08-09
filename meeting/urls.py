from django.urls import path
from .views import SendAgenda, send_done

app_name = 'meeting'

urlpatterns = [
    path('send/', SendAgenda.as_view(), name='send_agenda'),
    path('send_done/', send_done, name='send_done'),
 
]
