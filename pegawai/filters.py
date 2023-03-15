import django_filters
from .models import *
from django import forms

class PegawaiFilter (django_filters.FilterSet):
    umur = forms.DateField( )
    
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
