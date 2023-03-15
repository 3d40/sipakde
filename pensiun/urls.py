from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'pensiun'
urlpatterns = [
    # path('', LoginView.as_view(template_name = 'register/login.html'), name='login'),
    # path('home/', HomeView.as_view(), name='home'),
    # path('logout/', Logout.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('changepassword/', CustomPasswordChangeView.as_view(), name='password_change'),
    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    # path('pensiun/', PensiunView, name='hitungpensiun')
    path('pensiun/', PegawaiListView.as_view(), name='pensiun'),
]