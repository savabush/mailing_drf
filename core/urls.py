from . import views
from django.urls import path


urlpatterns = [
    path('clients/', views.GetClientsOrCreateClientView.as_view(), name='client-create'),
    path('clients/<client_id>', views.UpdateOrDeleteClientView.as_view(), name='client-update-delete')
]