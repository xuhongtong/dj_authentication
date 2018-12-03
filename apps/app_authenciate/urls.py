from django.conf.urls import url

from apps.app_authenciate import views

urlpatterns = [
    url('login/',views.LoginView.as_view()),
    url('register/',views.RegisterView.as_view()),
    url('logout/',views.LogoutView.as_view()),
    url('mail/',views.sendmail),
    url('active/',views.active)
]