from django.urls import path
from .views import *

# app_name = "users"

urlpatterns = [
    path('',view=MultiStepFormWizard.as_view(),name='home'),
    path('signup/',view=signup_view,name='signup')

    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<int:pk>/", view=user_detail_view, name="detail"),
]
