from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from incidents.views import (
    dashboard,
    create_incident,
    incident_list,
    update_incident,
    delete_incident
)

from users.views import login_view, logout_view

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', login_view, name='login'),

    path('dashboard/', dashboard, name='dashboard'),

    path('incidents/', incident_list, name='incidents'),

    path('create/', create_incident, name='create_incident'),

    path('update/<int:pk>/', update_incident, name='update_incident'),

    path('delete/<int:pk>/', delete_incident, name='delete_incident'),

    path('logout/', logout_view, name='logout'),
    path('', include('users.urls')),
    path('', include('incidents.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)