from django.urls import path, include
from . import views


urlpatterns = [
    path('mentor', views.mentor, name="mentor"),

    path('mount_programme', views.mount_programme, name="mount_programme"),

    path('department_head', views.department_head, name="department_head"),

    path('room_detail', views.room_detail, name="room_detail"),

    path('library', views.library, name="library"),

    path('laboratory', views.laboratory, name="laboratory"),

    path('examination_unit', views.examination_unit, name="examination_unit"),

    path('mount_document', views.mount_document, name="mount_document"),

    path('mount_document/<int:pk>/', views.delete_documents, name="delete_documents"),

    path('mount_payment', views.mount_payment, name="mount_payment"),

    path('mount_payment/<int:pk>', views.delete_payments, name="delete_payments"),

    path('mount_summary', views.mount_summary, name="mount_summary"),

    path('mounted_completed', views.mounted_completed, name="mounted_completed"),



]
