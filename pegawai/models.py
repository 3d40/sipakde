from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from datetime import datetime


class TJenisUser(models.Model):
    # user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, db_column="user_id")
    # pegawai = models.ForeignKey('TPegawaiSapk', on_delete=models.DO_NOTHING, blank=True, null=True, related_name="pegawai")
    jenis_choice = [
        ('ver', 'Verifikator'),
        ('op', 'Operator'),
        ('peg', 'Pegawai'),
        {'admin', 'Admin'}
        ]
    jenis =models.CharField(max_length=20, default='peg', choices=jenis_choice)
    class Meta:
        managed = False
        db_table = 't_jenis_user'

    def __str__(self):
        return str(self.jenis)

class TPegawaiSapk(models.Model):
    id = models.CharField(db_column='PNS_ID', primary_key=True, max_length = 32, editable=False)  # Field name made lowercase.
    nip_baru = models.CharField(db_column='NIP_BARU', max_length=18)  # Field name made lowercase.
    nip_lama = models.CharField(db_column='NIP_LAMA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gelar_depan = models.CharField(db_column='GELAR_DEPAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gelar_blk = models.CharField(db_column='GELAR_BLK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tempat_lahir= models.ForeignKey('TLokasi', max_length=32, on_delete=models.CASCADE, related_name='TEMPAT_LAHIR', null = True, blank = True)  # Field name made lowercase.
    tgl_lhr = models.DateField(db_column='TGL_LAHIR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_kelamin = models.CharField(db_column='JENIS_KELAMIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agama= models.ForeignKey('TKodeAgama', max_length=1, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    jenis_kawin = models.ForeignKey('TStatusKawin', max_length=1, blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    nik = models.CharField(db_column='NIK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_hp = models.CharField(db_column='NOMOR_HP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)
    alamat = models.CharField(db_column='ALAMAT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    npwp_nomor = models.CharField(db_column='NPWP_NOMOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bpjs = models.CharField(db_column='BPJS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jenis_pegawai = models.ForeignKey('TJenisPegawai', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    kedudukan_hukum = models.ForeignKey('TStatusKedudukan', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    status_cpns_pns = models.CharField(db_column='STATUS_CPNS_PNS', max_length=1)  # Field name made lowercase.
    kartu_pegawai = models.CharField(db_column='KARTU_PEGAWAI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_cpns = models.CharField(db_column='NOMOR_SK_CPNS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_cpns = models.DateField(db_column='TGL_SK_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_cpns = models.DateField(db_column='TMT_CPNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomor_sk_pns = models.CharField(db_column='NOMOR_SK_PNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tgl_sk_pns = models.DateField(db_column='TGL_SK_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tmt_pns = models.DateField(db_column='TMT_PNS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gol_awal = models.ForeignKey('TKodeGolongan', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    gol= models.ForeignKey('TKodeGolongan',related_name='GOL_ID', max_length=2, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    tmt_golongan = models.CharField(db_column='TMT_GOLONGAN', max_length=10)  # Field name made lowercase.
    mk_tahun = models.IntegerField(db_column='MK_TAHUN', blank=True, null=True)  # Field name made lowercase.
    mk_bulan = models.IntegerField(db_column='MK_BULAN', blank=True, null=True)  # Field name made lowercase.
    jenis_jabatan= models.ForeignKey('TJenisJabatan',on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    jabatan = models.ForeignKey('TJabatan', on_delete=models.DO_NOTHING, null=True, db_column='JABATAN_ID')  # Field name made lowercase.
    tingkat_pendidikan= models.ForeignKey('TTingkatPendidikan', on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    pendidikan= models.ForeignKey('TPendidikan', max_length=32, on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    kpkn= models.CharField(db_column='KPKN_ID', max_length=32)  # Field name made lowercase.
    lokasi_kerja = models.ForeignKey('TLokasi',related_name='LOKASI_KERJA_ID', on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    unor= models.ForeignKey('TUnor', max_length=32, on_delete=models.CASCADE, related_name='UNOR_ID', null=True)  # Field name made lowercase.
    unor_induk = models.ForeignKey('TOpd', on_delete=models.DO_NOTHING, related_name='UNOR_INDUK_ID', null=True, blank=True)  # Field name made lowercase.
    unor_induk_bkd = models.ForeignKey('TOpd', on_delete=models.DO_NOTHING, db_column='UNOR_INDUK_BKD', verbose_name='Instansi', null=True, blank=True)  # Field name made lowercase.
    instansi_induk_nama = models.CharField(db_column='INSTANSI_INDUK_NAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    instansi_kerja_nama= models.CharField(db_column='INSTANSI_KERJA_NAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    satuan_kerja_induk_nama = models.CharField(db_column='SATUAN_KERJA_INDUK_NAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    satuan_kerja_kerja_nama= models.CharField(db_column='SATUAN_KERJA_KERJA_NAMA', max_length=150, blank=True, null=True)  
    tmt_pensiun = models.DateField(db_column='TMT_PENSIUN', blank=True, null=True)# Field name made lowercase.
    fhoto=models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)

    class Meta:
        managed = False
        db_table = 't_pegawai_sapk'
        

    def __str__(self):
        return self.nama

class TKodeAgama(models.Model):
    agama_id = models.CharField(db_column='AGAMA_ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    agama_nama = models.CharField(db_column='AGAMA_NAMA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TKodeAgama'

    def __str__(self):
        return self.agama_nama

class TKodeGolongan(models.Model):
    id = models.CharField(primary_key=True, max_length=32, editable=False)
    nama_golongan = models.CharField(max_length=5)
    nama_pangkat = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 't_kode_golongan'

    def __str__(self):
        return self.nama_golongan

class TJabatan(models.Model):
    id = models.CharField(primary_key=True,max_length=32, editable=False)
    nama_jabatan = models.CharField(db_column='nama_Jabatan', max_length=139)  # Field name made lowercase.
    id_jenis_jabatan = models.ForeignKey('TJenisJabatan', db_column='id_jenis_jabatan', on_delete=models.DO_NOTHING, null=True)  # Field name made lowercase.
    jenis_jabatan = models.CharField(max_length=27)
    id_eselon = models.ForeignKey('Teselon', db_column='id_eselon', on_delete=models.DO_NOTHING, null=True)
    bup = models.IntegerField()
    stastus = models.CharField(max_length=5)

    class Meta:
        managed = True
        db_table = 't_jabatan'
    
    def __str__(self):
        return str(self.nama_jabatan)


class TEselon(models.Model):
    id = models.CharField(primary_key=True, max_length=32, editable=False)
    nama = models.CharField(max_length=10)
    maxgol = models.ForeignKey('TKodeGolongan', on_delete=models.DO_NOTHING,db_column='max_pangkat', related_name='maxgol', null=True)
    mingol = models.ForeignKey('TKodeGolongan', on_delete=models.DO_NOTHING, db_column='min_pangkat', related_name='mingol', null=True)
    keterangan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_eselon'
    
    def __str__(self):
        return str(self.nama)

class TJenisJabatan(models.Model):
    id = models.CharField(db_column='JENIS_JABATAN_ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    jenis_jabatan_nama = models.CharField(db_column='JENIS_JABATAN_NAMA', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_jenis_jabatan'

    def __str__(self):
        return self.jenis_jabatan_nama

class TStatusKawin(models.Model):
    id = models.CharField(db_column='JENIS_KAWIN_ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    jenis_kawin_nama = models.CharField(db_column='JENIS_KAWIN_NAMA', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TStatusKawin'

    def __str__(self):
        return self.jenis_kawin_nama


class TJenisPegawai(models.Model):
    id = models.CharField(db_column='JENIS_PEGAWAI_ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    jenis_pegawai_nama = models.CharField(db_column='JENIS_PEGAWAI_NAMA', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TJenisPegawai'

    def __str__(self):
        return self.jenis_pegawai_nama


class TStatusKedudukan(models.Model):
    id = models.CharField(db_column='ID_STATUS_KEDUDUKAN', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    nama_status_kedudukan = models.CharField(db_column='NAMA_STATUS_KEDUDUKAN', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TStatusKedudukan'

    def __str__(self):
        return self.nama_status_kedudukan

class TLokasi(models.Model):
    id = models.CharField(db_column='LOKASI_ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    kanreg_id = models.CharField(db_column='KANREG_ID', max_length=2)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=50)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=10)  # Field name made lowercase.
    jenis = models.CharField(db_column='JENIS', max_length=3)  # Field name made lowercase.
    jenis_kabupaten = models.CharField(db_column='JENIS_KABUPATEN', max_length=25)  # Field name made lowercase.
    jenis_desa = models.CharField(db_column='JENIS_DESA', max_length=15)  # Field name made lowercase.
    ibukota = models.CharField(db_column='IBUKOTA', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TLokasi'

    def __str__(self):
        return self.nama

class TPendidikan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    tingkat_pendidikan = models.ForeignKey('TPendidikan', max_length=3, on_delete=models.DO_NOTHING, null=True)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=150)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TPendidikan'

    def __str__(self):
        return self.nama

class TTingkatPendidikan(models.Model):
    id = models.CharField(db_column='KODE', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=25)  # Field name made lowercase.
    golongan_awal = models.CharField(db_column='GOLONGAN_AWAL', max_length=3)  # Field name made lowercase.
    golongan_akhir = models.CharField(db_column='GOLONGAN_AKHIR', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_tingkat_pendidikan'

    def __str__(self):
        return self.nama


class TUnor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    instansi_id = models.CharField(db_column='INSTANSI_ID', max_length=32)  # Field name made lowercase.
    diatasan_id = models.CharField(db_column='DIATASAN_ID', max_length=32)  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=250)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    # unor_order = models.IntegerField(db_column='UNOR_ORDER', blank=True, null=True)  # Field name made lowercase.
    # status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pemimpin_pns= models.ForeignKey('TPegawaiSapk', max_length=32, blank=True, null=True, on_delete=models.DO_NOTHING)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jenis_unor_id = models.CharField(db_column='JENIS_UNOR_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nama_pejabat = models.CharField(db_column='NAMA_PEJABAT', max_length=70, blank=True, null=True)  # Field name made lowercase.
    unor_induk = models.CharField(db_column='UNOR_INDUK_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TUnor'

    def __str__(self):
        return self.nama_unor


class TOpd(models.Model):
    id = models.CharField(db_column='ID',primary_key=True, max_length=32, editable=False)  # Field name made lowercase.
    nama_unor = models.CharField(db_column='NAMA_UNOR', max_length=255, verbose_name = 'Instansi')  # Field name made lowercase.
    eselon_id = models.CharField(db_column='ESELON_ID', max_length=3)  # Field name made lowercase.
    cepat_kode = models.CharField(db_column='CEPAT_KODE', max_length=15)  # Field name made lowercase.
    nama_jabatan = models.CharField(db_column='NAMA_JABATAN', max_length=255)  # Field name made lowercase.
    nama_pejabat = models.ForeignKey('TPegawaiSapk' ,db_column='NAMA_PEJABAT', on_delete=models.DO_NOTHING, null=True)  # Field name made lowercase.
    diatasan_id = models.CharField(db_column='DIATASAN_ID', max_length=32)  # Field name made lowercase.
    instansi_id = models.CharField(db_column='INSTANSI_ID', max_length=32)  # Field name made lowercase.
    pemimpin_non_pns_id = models.CharField(db_column='PEMIMPIN_NON_PNS_ID', max_length=55)  # Field name made lowercase.
    pemimpin_pns_id = models.CharField(db_column='PEMIMPIN_PNS_ID', max_length=32)  # Field name made lowercase.
    jenis_unor_id = models.CharField(db_column='JENIS_UNOR_ID', max_length=32)  # Field name made lowercase.
    unor_induk = models.CharField(db_column='UNOR_INDUK', max_length=32)  # Field name made lowercase.
    jumlah_ideal_staff = models.CharField(db_column='JUMLAH_IDEAL_STAFF', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_opd'
    
    def __str__(self):
        return str(self.nama_unor)

def _upload_path_kp(instance,filename):
    return instance.get_upload_path(filename)

class TRiwayatGolongan(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)
    orang_id = models.ForeignKey('TPegawaiSapk', blank = True, null=True, on_delete = models.CASCADE, db_column='orang_id')
    nip_baru = models.CharField(db_column='NIP', max_length=18, blank=True, null=True)  # Field name made lowercase.
    kode_jenis_kp = models.IntegerField(db_column='Kode_Jenis_KP', blank=True, null=True)  # Field name made lowercase.
    jenis_kp = models.CharField(db_column='Jenis_KP', max_length=52, blank=True, null=True, verbose_name="Jenis Kenaikan Pangkat")  # Field name made lowercase.
    id_golongan = models.ForeignKey('TKodeGolongan', verbose_name ="Golongan" ,max_length=32, on_delete=models.CASCADE, db_column='id_golongan')  # Field name made lowercase.
    sk_nomor = models.CharField(db_column='SK_Nomor', verbose_name ="Nomor SK",max_length=45, blank=True, null=True)  # Field name made lowercase.
    sk_tanggal = models.DateField(db_column='Sk_Tanggal', verbose_name="Tanggal SK",max_length=14,  null=True, default='1900-01-01', blank=True)  # Field name made lowercase.
    nomor_bkn = models.CharField(db_column='Nomor_BKN', verbose_name="Nomor BKN",max_length=30,  null=True, blank=True )  # Field name made lowercase.
    tanggal_bkn = models.DateField(db_column='Tanggal_BKN', verbose_name="Tanggal BKN",max_length=14, null=True, default='1900-01-01')  # Field name made lowercase.
    tmt_golongan = models.DateField(db_column='TMT_Golongan', verbose_name = "TMT Golongan",max_length=14, blank=True, null=True)  # Field name made lowercase.
    jumlah_angka_kredit_utama = models.DecimalField(db_column='Jumlah_Angka_Kredit_Utama', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    jumlah_angka_kredit_tambahan = models.DecimalField(db_column='Jumlah_Angka_Kredit_Tambahan', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    mk_golongan_tahun = models.IntegerField(db_column='MK_Golongan_Tahun', verbose_name= "Masa Kerja Golongan (Tahun)", blank=True, null=True)  # Field name made lowercase.
    mk_golongan_bulan = models.IntegerField(db_column='MK_Golongan_Bulan', verbose_name= "Masa Kerja Golongan (Bulan)", blank=True, null=True)  # Field name made lowercase.
    dokumen = models.FileField(upload_to= _upload_path_kp, null=True, validators=[FileExtensionValidator( ['pdf'] )])
    berkas = models.ForeignKey('TBerkas', on_delete=models.DO_NOTHING, blank=True, null=True)
    nama = models.CharField(db_column='Nama', max_length=255, blank=True, null=True)
    
    class Meta:             
        managed = False
        db_table = 't_riwayat_golongan'
    
    def __str__(self):
        return self.orang_id.nip_baru+":"+str(self.dokumen.name)
    
    def get_upload_path(self,filename):
        filelama = self.orang_id.nip_baru, self.id_golongan.nama_pangkat
        filename = {"SKKP_"},filelama
        return "{}/{}".format(self.nip_baru, filename)

class TBerkas(models.Model):
    status_choice =(
        ("1", "User"),
        ("2", "Verifikasi"),
        ("3", "Valid"),
        ("4", "Rejected"),
        )
    id = models.IntegerField(primary_key=True, editable=False)
    pns_id = models.ForeignKey('TPegawaiSapk',  on_delete=models.DO_NOTHING, db_column='pns')
    status = models.IntegerField(choices=status_choice, default=1, verbose_name=status_choice)
    
    class Meta:
        managed = False
        db_table = 't_berkas'

    def __str__(self):
        return str(self.pns_id)

class TUser(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    pengguna=models.ForeignKey(User, db_column='pengguna',on_delete=models.CASCADE, related_name="usernames")
    jenis = models.ForeignKey('TJenisUser', db_column='jenis', on_delete=models.CASCADE, verbose_name='Jenis Pengguna', default=1)
    user_akses = models.ForeignKey('TOpd', db_column='user_akses', on_delete=models.CASCADE, verbose_name='Nama OPD', null=True),
    waktu_login = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        managed = False
        db_table = 't_user'

    def __str__(self):
        return self.pengguna.username
