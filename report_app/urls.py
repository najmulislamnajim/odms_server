from django.urls import path
from report_app import views

urlpatterns = [
    path('dashboard/<int:sap_id>', views.dashboard_report),
    path('dashboard/info/<int:sap_id>', views.dashboard_info),
    path('activity_for_map/<int:sap_id>/<str:date>', views.activity_for_map),
]