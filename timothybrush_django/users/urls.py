from django.urls import path
from .views import *

# app_name = "users"

urlpatterns = [
    # path('',view=home,name="home"),
    path('vechicle/',view=vechicle_info,name="vechicle_info"),
    path('events/',view=events_info,name="events_info"),
    path('memorabilia/',view=memorabilia_info,name="memorabilia_info"),
    path('',view=memorabilia_info,name="home"),
    path('payment/',view=payment_info,name="payment_info"),

    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<int:pk>/", view=user_detail_view, name="detail"),
]
