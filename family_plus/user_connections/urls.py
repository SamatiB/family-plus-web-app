"""family_plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    connections_view,
    search_page_view,
    search_family_view,
    search_username_view,
    pending_requests_view,
)

urlpatterns = [
    path('<int:user_id>/', connections_view, name="connections-view"),
    path('search/', search_page_view, name="search-page"),
    path('families/search_results/', search_family_view, name="search-family"),
    path('users/search_results/', search_username_view, name="search-username"),
    path('requests/', pending_requests_view, name="pending-requests"),
]
