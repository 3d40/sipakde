from django.shortcuts import render, HttpResponse

# Create your views here.
from pegawai.models import TPegawaiSapk
from django.views.generic.list import ListView

# def PensiunView(request):
#     pegawai = TPegawaiSapk.objects.all()

#     return HttpResponse(pegawai)
 

class PegawaiListView(ListView):
    model = TPegawaiSapk
    template_name= 'pensiun/PensiunTPegawaiSapk_list.html'


