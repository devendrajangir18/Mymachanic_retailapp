from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "GoMechanic Admin"
admin.site.site_title = "GoMechanic Admin Portal"
admin.site.index_title = "Welcome to GoMechanic Community"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
