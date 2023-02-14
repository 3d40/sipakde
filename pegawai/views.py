from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, get_list_or_404,reverse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
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



# Create your views here.
# class Login(LoginView):
#     template_name = 'register/login.html';
# redirect_authenticated_user = True

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            request.session['user'] = username
            xxx = TUser.objects.get(pengguna = user)
            tipeuser = TJenisUser.objects.get(jenis=xxx.jenis)

            if user.is_active and tipeuser.jenis =='Pegawai':
                pegawai = get_object_or_404(TPegawaiSapk, nip_baru = user)
                print(pegawai.id) 
                login(request,user)
                return render(request, 'pegawai/profile.html',{'pegawai':pegawai})
            
            elif user.is_active and tipeuser.jenis =='Operator':
                data = get_list_or_404(TPegawaiSapk, unor_induk_bkd = xxx.user_akses)
                login(request,user)
                page_num = request.GET.get('page', 1)
                paginator = Paginator(data, 20)
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, 'pegawai/pegawai_list.html',{'page_obj':page_obj})
            
            elif user.is_active and tipeuser.jenis =='Verifikator':
                data = TPegawaiSapk.objects.all()
                login(request,user)
                page_num = request.GET.get('page', 1)
                paginator = Paginator(data, 20)
                try:
                    page_obj = paginator.page(page_num)
                except PageNotAnInteger:
                    page_obj = paginator.page(1)
                except EmptyPage:
                    page_obj = paginator.page(paginator.num_pages)
                return render(request, 'pegawai/pegawai_list.html',{'page_obj':page_obj})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Akun anda belum terdaftar")
    else:
        return render(request, 'register/login.html', {})

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

class HomePageView(ListView):
    model= TPegawaiSapk
    template_name = 'pegawai/pegawai_list.html'
    paginate_by = 25
    context_object_name ='object_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        jenis = get_object_or_404 (TUser, pengguna = self.request.user)
        self.filterset = PegawaiFilter(self.request.GET, queryset = queryset)
        return  self.filterset.qs
    

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        jenis = get_object_or_404 (TUser, pengguna = self.request.user)
        context['pengguna'] =jenis.jenis 
        context['form'] = self.filterset.form
        context['jumlah'] = self.filterset.qs.count()
        return context

def PegawaiDetail(request, nip_baru):
    pegawai = get_object_or_404(TPegawaiSapk, nip_baru=nip_baru)
    return render(request, 'pegawai/profile.html', {'pegawai': pegawai})


class GolonganListView(ListView):
    model = TRiwayatGolongan
    # form_class = FormTRiwayatGolongan
    template_name = 'pegawai/rwgolongan_list.html'
    

    def get_queryset(self, **kwargs):
        pegawai = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
        qs = super().get_queryset(**kwargs)
        return qs.filter(orang_id=pegawai.id)

class JabatanListView(ListView):
    model = TRiwayatJabatan
    # form_class = FormTRiwayatGolongan
    template_name = 'pegawai/rwjabatan_list.html'
    

    def get_queryset(self, **kwargs):
        pegawai = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
        qs = super().get_queryset(**kwargs)
        return qs.filter(orang_id=pegawai.id)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    

class RiwayatSkpList(ListView):
    model = TRiwayatDp3
    template_name = 'pegawai/rwskp_list.html'

    def get_queryset(self, **kwargs):
        pegawai = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
        qs = super().get_queryset(**kwargs)
        return qs.filter(id_pns=pegawai.id)
    
    def get_context_data(self, **kwargs):
        context = super(RiwayatSkpList, self).get_context_data(**kwargs)
        context['pegawai'] = get_object_or_404(TPegawaiSapk, nip_baru =self.request.user)
        context['judul'] = " Riwayat Sasaran Kinerja Pegawai"
        return context


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
