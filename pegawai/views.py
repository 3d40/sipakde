from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, get_list_or_404,reverse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import Q
from .filters import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView, UpdateView
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import AuthenticationForm
import json
from django.views.generic import View
from django.template.loader import render_to_string
from .token import AccountActivationTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode    
from ast import Slice
from cgitb import enable
import email
from multiprocessing import context
from operator import ge
from pickle import FALSE
from pickletools import int4
from re import template
from time import strftime
from dateutil.relativedelta import *
from codecs import namereplace_errors
import datetime
from itertools import count
from pyexpat import model
from tkinter import Y
from turtle import update
from django.conf import settings
from webbrowser import get
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from .forms import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin, SingleObjectMixin
from django.db.models import Q
from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from .models import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from .token import AccountActivationTokenGenerator
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_str as force_text
from django.contrib.auth import get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.urls import reverse,reverse_lazy
from urllib.request import  urlopen
import json
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'pdf']
urlpegawai = 'http://103.114.144.202/nip/?search='




class LoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('pegawai:pegawailist') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


def PegawaiList(request):
    user = request.user.username
    akun = TUser.objects.get(pengguna =request.user)
    if akun.jenis.id == 1:
        pegawai = TPegawaiSapk.objects.filter(nip_baru=user)
        data = urlopen(urlpegawai + user)
        json_pegawai = json.load(data)
        print(json_pegawai)
        for x in json_pegawai:
            opdupdate = TPegawaiSapk.objects.get(nip_baru = user)
            opdupdate.unor_skp_id =x['company_id']
            opdupdate.save(update_fields=['unor_skp'])

        filterku = PegawaiFilter(request.GET, queryset=pegawai)
        p = Paginator(filterku.qs, 25)
        page = request.GET.get('page')
        
        try:
            response = p.page(page)
        except PageNotAnInteger:
            response = p.page(1)
        except EmptyPage:from django.utils.http import urlsafe_base64_encode
        response = p.page(p.num_pages)
        context = {
            'filterku': filterku,
            'object_list': pegawai,
            'filter':response
            }
        return render (request, 'pegawai/tpegawaisapk_list.html',context)
    elif akun.jenis.id == 2:
        pegawai = TPegawaiSapk.objects.filter(unor_induk_bkd = akun.user_akses)
        filterku = PegawaiFilter(request.GET, queryset=pegawai)
        p = Paginator(filterku.qs, 25)
        page = request.GET.get('page')
        
        try:
            response = p.page(page)
        except PageNotAnInteger:
            response = p.page(1)
        except EmptyPage:
            response = p.page(p.num_pages)
        context = {
            'filterku': filterku,
            'object_list': pegawai,
            'filter':response
            }
        return render (request, 'pegawai/tpegawaisapk_list.html',context)
    else:
        pegawai = TPegawaiSapk.objects.all()
        for data in pegawai:
            tahun = data.nip_baru[0:4]
            bulan = data.nip_baru[4:6]
            tgl = data.nip_baru[6:8]
            lahir = datetime.strptime(tahun+'-'+bulan+'-'+tgl, "%Y-%m-%d").date()
            data.tgl_lhr= lahir
            data.save()
            umur = relativedelta(datetime.today(), lahir)
            if umur.years > 58:
                print(data.nip_baru, data.nama, umur.years)
        filterku = PegawaiFilter(request.GET, queryset=pegawai)
        p = Paginator(filterku.qs, 25)
        page = request.GET.get('page')
        
        try:
            response = p.page(page)
        except PageNotAnInteger:
            response = p.page(1)
        except EmptyPage:
            response = p.page(p.num_pages)
        context = {
            'filterku': filterku,
            'object_list': pegawai,
            'filter':response
            }
        return render (request, 'pegawai/tpegawaisapk_list.html', context)


class HomeView(View):
    template_name = 'register/home.html'
    def get(self, request):
        return render(request, self.template_name)


class Logout(LogoutView):
    template_name = 'register/login.html'
    next_page = 'pegawai:login'

class RegisterView(View):
    form_class = SignupForm
    template_name = 'register/register.html'

    def get(self, request):
        form = self.form_class()
        # form1 = OpdForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # form1 = OpdForm(request.POST)
        if form.is_valid():
            cekpegawai = TPegawaiSapk.objects.filter(nip_baru = request.POST.get('username')).exists()
            print(cekpegawai)
            if cekpegawai:
                x = TPegawaiSapk.objects.get(nip_baru = request.POST.get('username'))
                user = form.save(commit=False)
                user.is_active = False # Deactivate account till it is confirmed
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('register/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    })
                user.email_user(subject, message)
                return HttpResponse('Silahkan komfirmasi email Anda untuk menyelesaikan proses pendaftaran!')
            else:
                return HttpResponse('Data Anda tidak terhubung dengan data kepegawaian Pemerintah Provinsi Jambi!')
        else:
            return render(request, self.template_name)

           


        # return redirect('pegawai:login')

        # return render(request, self.template_name, {'form': form, 'form1':form1})


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            TUser.objects.update_or_create(
                pengguna = user,
            )
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('pegawai:login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('pegawai:login')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'register/password_change.html'
    success_url = reverse_lazy('pegawai:home')

    def form_valid(self, form):
        messages.success(self.request, 'Password kamu berhasil diubah')
        return super().form_valid(form)


def GolonganListView(request, id):
    pegawai = get_object_or_404(TPegawaiSapk, id =id)
    gol = get_list_or_404(TRiwayatGolongan, orang_id = id)
    if gol:     
        context = {
            'object_list':gol,
            'pegawai':pegawai
            }
        return render(request,'pegawai/rwgolongan_list.html',context)
    else:
        context={
            'objec_list': "Data Tidak Ada"
        }
        return render(request,'pegawai/rwgolongan_list.html',context)


def JabatanListView(request, id):
    pegawai = get_object_or_404(TPegawaiSapk, id =id)
    jabatan = get_list_or_404(TRiwayatJabatan, orang = id)
    context = {
        'object_list':jabatan,
        'pegawai':pegawai
    }
    return render(request,'pegawai/rwjabatan_list.html',context)


def RiwayatSkpList(request, id):
    pegawai = get_object_or_404(TPegawaiSapk, id =id)
    skp = TRiwayatDp3.objects.filter( id_pns = id)
    context = {
        'object_list':skp,
        'pegawai':pegawai
        }
    if skp:
        try:
            context = {
                'object_list':skp,
                'pegawai':pegawai
                }
            return render(request,'pegawai/rwskp_list.html',context)
        except:       
            context={
                'objec_list': "Data Tidak Ada"
                }
            return render(request,'pegawai/rwskp_list.html',context)
    return render(request,'pegawai/rwskp_list.html',context)

def RiwayatPendidikanList(request, id):
    pegawai = get_object_or_404(TPegawaiSapk, id = id)
    pendidikan = TRiwayatPendidikan.objects.filter( pengguna = id)
    if pendidikan:
        try:
            context = {
                'object_list':pendidikan,
                'pegawai':pegawai
                }
            return render(request,'pegawai/rwpendidikan_list.html',context)
        except:       
            context={
                'objec_list': "Data Tidak Ada",
                'pegawai':pegawai
                }
            return render(request,'pegawai/rwpendidikan_list.html',context)
    return render(request,'pegawai/rwpendidikan_list.html')




def RiwayatHukdisList(request, id):
    pegawai = get_object_or_404(TPegawaiSapk, id =id)
    hukdis = TRiwayatHukdis.objects.filter( orang = id)
    context = {
        'object_list':hukdis,
        'pegawai':pegawai
        }
    if hukdis:
        try:
            context = {
                'object_list':hukdis,
                'pegawai':pegawai
                }
            return render(request,'pegawai/rwhukdis_list.html',context)
        except:       
            context={
                'objec_list': "Data Tidak Ada"
                }
            return render(request,'pegawai/rwhukdis_list.html',context)
    return render(request,'pegawai/rwhukdis_list.html',context)


def RiwayatKursusList(request, id):
    pegawai = get_object_or_404(TPegawaiSapk, id =id)
    kursus = TRiwayatKursus.objects.filter( orang = id)
    context = {
        'object_list':kursus,
        'pegawai':pegawai
        }
    if kursus:
        try:
            context = {
                'object_list':kursus,
                'pegawai':pegawai
                }
            return render(request,'pegawai/rwkursus_list.html',context)
        except:       
            context={
                'objec_list': "Data Tidak Ada"
                }
            return render(request,'pegawai/rwkursus_list.html',context)
    return render(request,'pegawai/rwkursus_list.html',context)


def JabatanEditView(request, id):                                         
    data = get_object_or_404(TRiwayatJabatan, id=id)
    form = FormTriwayatJabatan(instance=data)
    if request.method == "POST":
        form = FormTriwayatJabatan(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect ('pegawai:rwjabatan')
    context = {
        "form":form
        }
    return render(request, 'pegawai/triwayatjabatan_update_form.html', context)


class JabatanInputView(CreateView):
    model = TRiwayatJabatan
    form_class = FormTriwayatJabatan
    template_name_suffix = '_update_form'

    def get_initial(self):
        super(JabatanInputView, self).get_initial()
        print(self.kwargs)
        pegawai = get_object_or_404(TPegawaiSapk, id = self.kwargs.get('id'))
        self.initial = {
            "orang":pegawai.id, 
            "unor":pegawai.unor_induk_bkd, 
            "jenis_jabatan":pegawai.jenis_jabatan
            }
        return self.initial

def PegawaiDetailView(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    pegawai = TPegawaiSapk.objects.get(id =id)
    print(pegawai.unor_skp)
    # add the dictionary during initialization
    context= {
        'pegawai' : pegawai
    }
    return render(request, "pegawai/profile.html", context)

class PangkatEditView(UpdateView):
    model = TRiwayatGolongan
    template_name = 'pegawai/triwayatgolongan_update_form.html'
    form_class = FormTRiwayatGolongan
    success_url = reverse_lazy("pegawai:rwgolongan")

    def get_object(self):
        return get_object_or_404(TRiwayatGolongan, pk=self.kwargs['pk'])
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.pk, self.object.orang_id.nip_baru)
        return super(PangkatEditView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = 1
        self.object.save(update_fields=['status'])
        return super(PangkatEditView, self).post(request, *args, **kwargs)
    


class SkpEditView(UpdateView):
    model = TRiwayatDp3
    form_class = FormRiwayatSkp
    template_name_suffix = '_update_form'

class SkpInputView(CreateView):
    model = TRiwayatDp3
    form_class = FormRiwayatSkp
    template_name_suffix = '_update_form'
    
    def get_initial(self):
        super(SkpInputView, self).get_initial()
        pegawai = get_object_or_404(TPegawaiSapk, id = self.kwargs.get('id'))
        self.initial = {
            "id_pns":pegawai,
            }
        return self.initial

    
# class PendidikanEditView(UpdateView):
#     model = TRiwayatPendidikan
#     form_class = FormTRiwayatPendidikan
#     template_name_suffix = '_update_form'


def PendidikanEditView(request, id):                                         
    data = get_object_or_404(TRiwayatPendidikan, id=id)
    form = FormTRiwayatPendidikan(instance=data)                                                               

    if request.method == "POST":
        form = FormTRiwayatPendidikan(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect ('pegawai:rwpendidikan')
    context = {
        "form":form,
        "object_list":data
    }
    return render(request, 'pegawai/triwayatpendidikan_update_form.html', context)


# def PensiunList(request):
#     user = request.user.username
#     akun = TUser.objects.get(pengguna =request.user)
#     if akun.jenis.id == 1:
#         pegawai = TPegawaiSapk.objects.filter(nip_baru=user)
#         data = urlopen(urlpegawai + user)
#         json_pegawai = json.load(data)
#         print(json_pegawai)
#         for x in json_pegawai:
#             opdupdate = TPegawaiSapk.objects.get(nip_baru = user)
#             opdupdate.unor_skp_id =x['company_id']
#             opdupdate.save(update_fields=['unor_skp'])

#         filterku = PegawaiFilter(request.GET, queryset=pegawai)
#         p = Paginator(filterku.qs, 25)
#         page = request.GET.get('page')
        
#         try:
#             response = p.page(page)
#         except PageNotAnInteger:
#             response = p.page(1)
#         except EmptyPage:from django.utils.http import urlsafe_base64_encode
#         response = p.page(p.num_pages)
#         context = {
#             'filterku': filterku,
#             'object_list': pegawai,
#             'filter':response
#             }
#         return render (request, 'pegawai/tpegawaisapk_list.html',context)
#     elif akun.jenis.id == 2:
#         pegawai = TPegawaiSapk.objects.filter(unor_induk_bkd = akun.user_akses)
#         filterku = PegawaiFilter(request.GET, queryset=pegawai)
#         p = Paginator(filterku.qs, 25)
#         page = request.GET.get('page')
        
#         try:
#             response = p.page(page)
#         except PageNotAnInteger:
#             response = p.page(1)
#         except EmptyPage:
#             response = p.page(p.num_pages)
#         context = {
#             'filterku': filterku,
#             'object_list': pegawai,
#             'filter':response
#             }
#         return render (request, 'pegawai/tpegawaisapk_list.html',context)
#     else:
#         pegawai = TPegawaiSapk.objects.all()
#         for data in pegawai:
#             tahun = data.nip_baru[0:4]
#             bulan = data.nip_baru[4:6]
#             tgl = data.nip_baru[6:8]
#             lahir = datetime.strptime(tahun+'-'+bulan+'-'+tgl, "%Y-%m-%d").date()
#             data.tgl_lhr= lahir
#             data.save()
#         filterku = PegawaiFilter(request.GET, queryset=pegawai)
#         p = Paginator(filterku.qs, 25)
#         page = request.GET.get('page')
        
#         try:
#             response = p.page(page)
#         except PageNotAnInteger:
#             response = p.page(1)
#         except EmptyPage:
#             response = p.page(p.num_pages)
#         context = {
#             'filterku': filterku,
#             'object_list': pegawai,
#             'filter':response
#             }
#         return render (request, 'pegawai/tpegawaisapk_list.html', context)