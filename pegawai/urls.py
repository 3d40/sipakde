from django.urls import path
from .views import *

app_name = 'pegawai'
urlpatterns = [
    path('', LoginView, name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('changepassword/', CustomPasswordChangeView.as_view(), name='password_change'),
    #Pegawai
    path('intaian/pegawailist', HomePageView.as_view(), name='pegawailist'),
    path('intaian/profile/<str:pk>', PegawaiDetailView.as_view(), name='profile'),

    #Golongan
    path('intaian/pegawai/golongan/<str:nip_baru>', GolonganListView, name='rwgolongan'),
    path('pegawai/input/pangkat/<str:id>', InputPangkatView, name='inputpangkat'),




]