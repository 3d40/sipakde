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


class MyLoginView(LoginView):
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
        filterku = PegawaiFilter(request.GET, queryset=pegawai)
        context = {
            'filterku': filterku,
            'object_list': pegawai,
            }
        return render (request, 'pegawai/tpegawaisapk_list.html',context)
    elif akun.jenis.id == 2:
        pegawai = TPegawaiSapk.objects.filter(unor_induk_bkd = akun.user_akses)
        filterku = PegawaiFilter(request.GET, queryset=pegawai)
        context = {
            'filterku': filterku,
            'object_list': pegawai,
            }
        return render (request, 'pegawai/tpegawaisapk_list.html',context)
    else:
        pegawai = TPegawaiSapk.objects.all()
        filterku = PegawaiFilter(request.GET, queryset=pegawai)
        context = {
            'filterku': filterku,
            'object_list': pegawai,
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
    template_name = 'register/register.html'
    def get(self, request):
        form = SignupForm()
        form1 = OpdForm()
        return render(request, self.template_name, {'form': form, 'form1':form1})
    
    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        form1 = OpdForm(request.POST)
        if form.is_valid():
            pegawai = TPegawaiSapk.objects.filter(nip_baru=request.POST.get('username')).exists()
            if pegawai == True:
                y = get_object_or_404(TOpd, id = request.POST.get('unor_induk_bkd'))
                x = TPegawaiSapk.objects.get(nip_baru = request.POST.get('username'))
                x.unor_induk_bkd = y
                x.save()
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Aktifkan akun Anda!'
                message = render_to_string('regitster/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Silahkan komfirmasi email Anda untuk menyelesaikan proses pendaftaran!')
            else:
                return HttpResponse('Data Anda tidak terhubung dengan data kepegawaian Pemerintah Provinsi Jambi!')
        else:
            form = SignupForm()
            form1 = OpdForm()
        return render(request, 'register/register.html', {'form': form, 'form1':form1})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'register/password_change.html'
    success_url = reverse_lazy('pegawai:home')

    def form_valid(self, form):
        messages.success(self.request, 'Password kamu berhasil diubah')
        return super().form_valid(form)


# class GolonganListView(ListView):
#     model = TRiwayatGolongan
#     # form_class = FormTRiwayatGolongan
#     template_name = 'pegawai/rwgolongan_list.html'

#     def get_qeryset(self):
#         qs = super().get_queryset()
#         search_term = self.request.GET.get("search", None)
#         if search_term is not None:
#             qs = qs.filter(session_name__icontains=search_term)
#         return qs
    

    # def get_queryset(self, **kwargs):
    #     pegawai = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
    #     qs = super().get_queryset(**kwargs)
    #     return qs.filter(orang_id=pegawai.id)


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
    pegawai = get_object_or_404(TPegawaiSapk, id =id)
    pendidikan = get_list_or_404(TRiwayatPendidikan, pengguna = id)
    if pendidikan:
        try:
            context = {
                'object_list':pendidikan,
                'pegawai':pegawai,
                }
            return render(request,'pegawai/rwpendidikan_list.html',context)
        except:
            context={
                'objec_list': "Data Tidak Ada"
                }
    return render(request,'pegawai/rwpendidikan_list.html',context)

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





# class JabatanListView(ListView):
#     model = TRiwayatJabatan
#     # form_class = FormTRiwayatGolongan
#     template_name = 'pegawai/rwjabatan_list.html'
    

#     def get_queryset(self, **kwargs):
#         pegawai = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
#         qs = super().get_queryset(**kwargs)
#         return qs.filter(orang_id=pegawai.id)

class JabatanEditView(UpdateView):
    template_name = 'pegawai/triwayatjabatan_update_form.html'
    model = TRiwayatJabatan
    form_class = FormTriwayatJabatan
    
    def get_success_url(self):
        return reverse("pegawai:rwjabatan")

class JabatanInputView(CreateView):
    model = TRiwayatJabatan
    form_class = FormTriwayatJabatan
    template_name_suffix = '_update_form'

    def get_initial(self):
        super(JabatanInputView, self).get_initial()
        pegawai = TPegawaiSapk.objects.get(nip_baru=self.request.user)
        user = self.request.user
        self.initial = {
            "orang":pegawai.id, 
            "unor":pegawai.unor_induk_bkd, 
            "jenis_jabatan":pegawai.jenis_jabatan
            }
        return self.initial



# def InputPangkatView(request, id):
#     pengguna = request.session['user']
#     pns = get_object_or_404(TPegawaiSapk, nip_baru=pengguna)
#     gol = get_object_or_404(TRiwayatGolongan, id = id)
#     form=FormTRiwayatGolongan(instance=gol)
#     print(gol.orang_id.pns_id)
#     if request.method == 'POST':
#         gol.save() 
#         form = FormTRiwayatGolongan(request.POST, request.FILES, instance=gol)
#         if form.is_valid():
#             form.save()
#             return render(request, 'pegawai/pangkatinput.html', {'form': form})
#         else:
#             pass
#     return render(request, 'pegawai/pangkatinput.html', {'form':form})


class PegawaiDetailView(DetailView):
    model = TPegawaiSapk
    template_name = 'pegawai/profile.html'
    context_object_name = 'pegawai'

    def get_context_data(self, *args,**kwargs):
        context = super(PegawaiDetailView,self).get_context_data(*args, **kwargs)
        # add extra field       
        return context

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
        self.object.status = '1'
        self.object.save()
        return super(PangkatEditView, self).post(request, *args, **kwargs)
    


    # def get_queryset(self):
    #     queryset = super(PangkatEditView, self).get_queryset()
    #     return queryset.get(id=self.id)
    
    # def get_initial(self):
    #     initial = super().get_initial()
    #     return initial
        
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     form.save()
    #     return response

    

# class RiwayatSkpList(ListView):
#     model = TRiwayatDp3
#     template_name = 'pegawai/rwskp_list.html'

#     def get_queryset(self, **kwargs):
#         pegawai = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
#         qs = super().get_queryset(**kwargs)
#         return qs.filter(id_pns=pegawai.id)
    
#     def get_context_data(self, **kwargs):
#         context = super(RiwayatSkpList, self).get_context_data(**kwargs)
#         context['pegawai'] = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
#         context['judul'] = " Riwayat Sasaran Kinerja Pegawai"
#         return context


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
        pegawai = TPegawaiSapk.objects.get(nip_baru=self.request.user)
        user = self.request.user
        self.initial = {
            "id_pns":pegawai,
            }
        return self.initial
