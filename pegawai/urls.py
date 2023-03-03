from django.urls import path
from .views import *
from django.conf.urls.static import static
from .views import RegisterView, ActivateAccount

app_name = 'pegawai'
urlpatterns = [
    path('', LoginView.as_view(template_name = 'register/login.html'), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('changepassword/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

    #Pegawai

    # path('intaian/profile/<str:pk>', PegawaiDetailView.as_view(), name='profile'),
    path('intaian/profile/<str:id>', PegawaiDetailView, name='profile'),
    path('intaian/profile/<str:id>/golongan', GolonganListView, name='rwgolongan'),
    path('intaian/profile/<str:id>/jabatan', JabatanListView, name='rwjabatan'),
    # path('intaian/profile/<id>/jabatan', JabatanEditView, name='editjabatan'),
    path('intaian/profile/<str:id>/jabatan/input', JabatanInputView.as_view(), name='inputjabatan'),
    path('intaian/profile/<str:id>/skp', RiwayatSkpList, name='rwskp'),
    path('intaian/profile/<str:id>/skp/input', SkpInputView.as_view(), name='inputskp'),
    path('intaian/profile/<str:id>/pendidikan', RiwayatPendidikanList, name='rwpendidikan'),
    path('intaian/profile/<str:id>/pendidikan/edit/', PendidikanEditView.as_view(), name='editpendidikan'),
    path('intaian/profile/<str:id>/hukdis', RiwayatHukdisList, name='rwhukdis'),
    path('intaian/profile/<str:id>/kursus', RiwayatKursusList, name='kursus'),
    
    
    
    # path('intaian/pegawailist/', PegawaiList.as_view(), name='pegawailist'),
    path('intaian/pegawailist/', PegawaiList, name='pegawailist'),

    #Golongan
    # path('intaian/profile/<str:pk>/golongan', GolonganListView.as_view(), name='rwgolongan'),
    
    path('intaian/pegawai/update/golongan/<str:pk>', PangkatEditView.as_view(), name='editpangkat'),

    #Jabatan
    # path('intaian/pegawai/jabatan/', JabatanListView.as_view() , name='rwjabatan'),
    
    path('intaian/pegawai/edit/jabatan/<str:id>', JabatanEditView, name='editjabatan'),
    # path('intaian/pegawai/input/jabatan/', JabatanInputView.as_view(), name='inputjabatan'),


    #skp
    # path('intaian/pegawai/skp/', RiwayatSkpList.as_view() , name='rwskp'),
    
    path('intaian/pegawai/edit/skp/<pk>', SkpEditView.as_view(), name='editskp'),
    # path('intaian/pegawai/input/skp/', SkpInputView.as_view(), name='inputskp'),

    #pendidikan
    

    #Hukdis
   


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)