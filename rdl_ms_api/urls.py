
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/app_info',views.app_info),
    path('api/v1/', include('user_app.urls')),
    path('api/v1/attendance/', include('attendance_app.urls')),
    path('api/v1/reports/', include('report_app.urls')),
    path('api/v1/delivery/', include('delivery_app.urls')),
    path('api/v1/cash_collection/', include('collection_app.urls')),
    path('api/v1/customer_location/', include('customer_location_app.urls')),
    path('api/v1/conveyance/', include('conveyance_app.urls')),
    path('api/v1/visit/', include('visit_app.urls')),
    path('api/v1/sap/', include('sap_app.urls')),
    path('api/v1/overdue/', include('overdue_app.urls')),
    path('web_view/v1/', include('web_view_app.urls')),
    path('mobile_app/v1/', include('mobile_app_control.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
