from django.urls import path, include
from .views import *

urlpatterns = [
    path("", main),
    path("secret_reference/", secret_reference, name="secret_reference"),
    path("<reference>/", enter_pin_code, name="enter_pin_code"),

]
