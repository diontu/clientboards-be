from django.urls import path

from .views.accounts.accounts_view import AccountsAPIView
from .views.block_permissions.block_permissions_view import BlockPermissionsAPIView
from .views.blocks.block_view import BlocksAPIView
from .views.subscriptions.subscription_view import SubscriptionsAPIView
from .views.users.users_view import UsersAPIView

""" 
urlpatterns is an array of endpoints that requires:
1. path location
2. view

"""
urlpatterns = [
    path('accounts/', AccountsAPIView.as_view(), name='accounts'),
    path('users/', UsersAPIView.as_view(), name='users'),
    path('subscriptions/', SubscriptionsAPIView.as_view(), name='subscriptions'),
    path('blocks/', BlocksAPIView.as_view(), name='blocks'),
    path('block_permissions/', BlockPermissionsAPIView.as_view(),
         name='block_permissions'),
]
