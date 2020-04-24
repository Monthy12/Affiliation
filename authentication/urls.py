from django.urls import path
from .import views
from django.conf.urls import url

urlpatterns = [

    path('login', views.login_user, name="login"),

    path('signup', views.signup_user, name="signup"),

    path('logout', views.logout_user, name="logout"),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    views.activate_account, name='activate'),

]
