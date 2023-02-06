from django.urls import path
from .views import *
from django.conf.urls.static import static

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
    path('intaian/pegawai/golongan/', GolonganListView.as_view(), name='rwgolongan'),
    path('intaian/pegawai/input/golongan/<str:pk>', PangkatEditView.as_view(), name='editpangkat'),

    #Jabatan
    path('intaian/pegawai/jabatan/', JabatanListView.as_view() , name='rwjabatan'),
    path('intaian/pegawai/input/jabatan/<str:pk>', JabatanEditView.as_view(), name='editjabatan'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)