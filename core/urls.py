from . import views
from django.urls import path


urlpatterns = [
    path('clients/', views.CreateClientView.as_view(), name='client-create'),
    path('clients/<client_id>', views.UpdateClientView.as_view(), name='client-update')
]