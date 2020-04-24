from django.urls import path
from . import views


urlpatterns = [

    path('institution', views.institution, name="institution"),

    path('institution_type', views.institution_type, name="institution_type"),

    path('institution_head', views.institution_head, name="institution_head"),

    path('bussiness_registeration', views.bussiness_registeration, name="bussiness_registeration"),

    path('management_registrar', views.management_registrar, name="management_registrar"),

    path('management_finance', views.management_finance, name="management_finance"),

    path('management_exam_officer', views.management_exam_officer, name="management_exam_officer"),

    path('affiliation_programme_mount', views.affiliation_programme_mount, name="affiliation_programme_mount"),

    path('affiliation_programme_department_head', views.affiliation_programme_department_head, name="affiliation_programme_department_head"),

    path('affiliation_programme_details_of_room', views.affiliation_programme_details_of_room, name="affiliation_programme_details_of_room"),

    path('affiliation_programme_library', views.affiliation_programme_library, name="affiliation_programme_library"),

    path('affiliation_programme_laboratory', views.affiliation_programme_laboratory, name="affiliation_programme_laboratory"),

    path('affiliation_programme_exam_unit', views.affiliation_programme_exam_unit, name="affiliation_programme_exam_unit"),

    path('affiliate', views.affiliate, name="affiliate"),

    path('document_upload', views.document_upload, name="document_upload"),

    path('document_upload/<int:pk>/', views.delete_document, name="delete_document"),

    path('affiliate_payment', views.affiliate_payment, name="affiliate_payment"),

    path('affiliate_payment/<int:pk>', views.delete_payment, name="delete_payment"),

    path('summary', views.summary, name="summary"),

    path('affiliation_completed', views.affiliation_completed, name="affiliation_completed"),

    # path('signup', views.signup_user, name="signup"),

    # path('logout', views.logout_user, name="logout")

]