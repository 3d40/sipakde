from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormTpegawaiSapk(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = ['nip_baru','nama', 'gelar_depan', 'gelar_blk', 'gol', 'tmt_golongan', 'tgl_lhr', 'jenis_kelamin','nik', 'nomor_hp', 'email', 'alamat', 'jenis_pegawai', 'jabatan','unor', 'unor_induk']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OpdForm(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = ['unor_induk_bkd']

class ProfileSearchForm(forms.Form):
    nama = forms.CharField(required=False)

class FormTRiwayatGolongan(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FormTRiwayatGolongan, self).__init__(*args, **kwargs)
        self.fields['jenis_kp'].disabled = True
        self.fields['id_golongan'].disabled = True
        self.fields['sk_nomor'].disabled = True
        self.fields['sk_tanggal'].disabled = True
        self.fields['tmt_golongan'].disabled = True
        self.fields['mk_golongan_tahun'].disabled = True
        self.fields['mk_golongan_bulan'].disabled = True

    class Meta:
        model = TRiwayatGolongan
        fields = ['jenis_kp', 'id_golongan', 'sk_nomor', 'sk_tanggal','tmt_golongan','mk_golongan_tahun', 'mk_golongan_bulan', 'dokumen']


class FormTriwayatJabatan(ModelForm):
    class Meta :
        model = TRiwayatJabatan
        fields =('orang','unor', 'jenis_jabatan','eselon', 'tmt_jabatan', 'nomor_sk', 'tanggal_sk', 'tmt_pelantikan', 'dokumen')


class FormRiwayatSkp(ModelForm):
    class Meta :
        model = TRiwayatDp3
        fields = [
            'id_pns',
            'tahun', 
            'kesetiaan', 
            'prestasi_kerja', 
            'tanggung_jawab', 
            'ketaatan', 
            'kejujuran', 
            'kerjasama', 
            'prakarsa', 
            'kepemimpinan', 
            'jumlah', 
            'nilai_ratarata', 
            'status_pejabat_penilai', 
            'nama_pejabat_penilai', 
            'jabatan_pejabat_penilai', 
            'golongan_pejabat_penilai',
            'nama_unor_pejabat_penilai', 
            'nama_atasan_penilai', 
            'jabatan_atasan_penilai', 
            'golongan_atasan_penilai',  
            'nama_unor_atasan_penilai', 
            'dokumen'
            ]


class FormTBerkas(ModelForm):
    class Meta :
        model = TBerkas
        fields = [
            'pns_id',
            'tipe',
            'tanggal_input',
            'tanggal_update',

        ]
