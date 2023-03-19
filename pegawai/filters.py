import django_filters
from django_filters import DateRangeFilter,DateFilter
from .models import *
from django import forms

class PegawaiFilter (django_filters.FilterSet):
    class Meta:
        model = TPegawaiSapk
        fields = { 
            'nip_baru': ['exact'], 
            'nama': ['icontains'], 
            'jenis_kelamin': ['exact'], 
            # 'agama':['exact'], 
            'nomor_hp':['exact'], 
            'email':['startswith'], 
            'alamat':['startswith'],  
            'bpjs':['icontains'], 
            # 'jenis_pegawai':['exact'],   
            'gol':['exact'], 
            'jenis_jabatan':['exact'], 
            'jabatan':['exact'], 
            'tingkat_pendidikan':['exact'], 
            # 'pendidikan':['exact'], 
            'unor_induk_bkd':['exact'],
        }


class PensiunFilter(django_filters.FilterSet):
    start_date = DateFilter(name='tmt_pensiun',lookup_type=('gt'),)
    end_date = DateFilter(name='tmt_pensiun',lookup_type=('lt'))
    date_range = DateRangeFilter(name='tmt_pensiun')

    class Meta:
        model = TPegawaiSapk
        fields = ['tmt_pensiun',]
