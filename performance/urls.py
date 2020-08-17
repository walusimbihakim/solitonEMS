from django.urls import path

from performance import views

urlpatterns = [
    path("manage_department_kpi_page", views.manage_department_kpi, name="manage_department_kpi_page"),
    path("edit_performance_kpi_page/<int:kpi_id>", views.edit_performance_kpi_page, name="edit_performance_page"),
    path("delete_performance_kpi/<int:kpi_id>", views.delete_performance_kpi, name="delete_performance_kpi"),
]