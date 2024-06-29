from django.urls import path

from .views.accounts.accounts_view import AccountsAPIView
from .views.block_permissions.block_permissions_view import BlockPermissionsAPIView
from .views.blocks.block_view import BlocksAPIView
from .views.logins.login_view import LoginAPIView
from .views.logins.signup_view import SignupAPIView
from .views.subscriptions.subscription_view import SubscriptionsAPIView
from .views.users.users_view import UsersAPIView

""" 
urlpatterns is an array of endpoints that requires:
1. path location
2. view

"""
urlpatterns = [
    path('account/', AccountsAPIView.as_view(), name='accounts'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # modify to be the logout class
    path('logout/', LoginAPIView.as_view(), name='logout'),
    path('users/', UsersAPIView.as_view(), name='users'),
    path('subscriptions/', SubscriptionsAPIView.as_view(), name='subscriptions'),
    path('blocks/', BlocksAPIView.as_view(), name='blocks'),
    path('block_permissions/', BlockPermissionsAPIView.as_view(),
         name='block_permissions'),
]
