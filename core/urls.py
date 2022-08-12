from . import views
from django.urls import path


urlpatterns = [
    path('clients/', views.GetClientsOrCreateClientView.as_view(), name='client-create'),
    path('clients/<client_id>', views.UpdateOrDeleteClientView.as_view(), name='client-update-delete'),
    path('mailinglist/', views.GetMailingListOrCreateMailing.as_view(), name='mailing-create'),
    path('mailinglist/<mailing_id>', views.UpdateOrDeleteMailingListView.as_view(), name='mailing-update-delete'),
]
