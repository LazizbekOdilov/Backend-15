from django.contrib import admin
from django.urls import path
from malumot.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('hamma_yonalishlar/', hamma_yonalishlar),
    path('hamma_fanlar/', hamma_fanlar),
    path('hamma_ustozlar/', hamma_ustozlar),

    path('fan_ochir/<int:son>/', fan_ochir),
    path('yonalish_ochir/<int:son>/', yonalish_ochir),

    path('fan_update/<int:son>/', fan_update),
    path('yonalish_update/<int:son>/', yonalish_update),
    path('ustoz_update/<int:son>/', ustoz_update),
]
