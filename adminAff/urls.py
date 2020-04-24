from django.urls import path, include
from . import views


urlpatterns = [

    path('admin_dashboard', views.home, name="admin_home"),

    path('affiliation', views.admin_affiliation, name="admin_affiliation"),

    path('client/<str:id>', views.client_details, name="client_details"),

    path('programme', views.admin_programme, name="admin_programme"),

    path('decline/<str:id>', views.decline, name="decline"),

    path('programme_client/<str:id>',views.programme_client_details, name="programme_client_details")

    # path('department_head', views.department_head, name="department_head")


]
