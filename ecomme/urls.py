from django.contrib import admin
from django.urls import path,include
from management.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('management/', include('management.urls')),
    path('product/', include('product.urls'))


]
