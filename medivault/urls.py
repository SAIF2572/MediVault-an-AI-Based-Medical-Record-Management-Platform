from django.contrib import admin
from django.urls import path, include
from patients import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('', include('patients.urls')),

    path('patient/', include('patients.urls')),

    path('hospital/', include('hospitals.urls')),

    path('lab/', include('reports.urls')),

    path('accounts/', include('accounts.urls')),

    path('doctor/', include('doctors.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)