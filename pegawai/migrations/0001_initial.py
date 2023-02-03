# Generated by Django 4.1 on 2023-01-30 01:47

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pegawai.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TBerkas',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[('1', 'User'), ('2', 'Verifikasi'), ('3', 'Valid'), ('4', 'Rejected')], default=1, verbose_name=(('1', 'User'), ('2', 'Verifikasi'), ('3', 'Valid'), ('4', 'Rejected')))),
            ],
            options={
                'db_table': 't_berkas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TJenisUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('jenis', models.CharField(choices=[('ver', 'Verifikator'), ('op', 'Operator'), ('peg', 'Pegawai')], default='peg', max_length=20)),
            ],
            options={
                'db_table': 't_jenis_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TKodeAgama',
            fields=[
                ('agama_id', models.CharField(db_column='AGAMA_ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('agama_nama', models.CharField(blank=True, db_column='AGAMA_NAMA', max_length=10, null=True)),
            ],
            options={
                'db_table': 'TKodeAgama',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRiwayatGolongan',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=32, primary_key=True, serialize=False)),
                ('nip_baru', models.CharField(blank=True, db_column='NIP', max_length=18, null=True)),
                ('kode_jenis_kp', models.IntegerField(blank=True, db_column='Kode_Jenis_KP', null=True)),
                ('jenis_kp', models.CharField(blank=True, db_column='Jenis_KP', max_length=52, null=True)),
                ('sk_nomor', models.CharField(blank=True, db_column='SK_Nomor', max_length=45, null=True)),
                ('sk_tanggal', models.DateField(blank=True, db_column='Sk_Tanggal', default='1900-01-01', max_length=14, null=True)),
                ('nomor_bkn', models.CharField(blank=True, db_column='Nomor_BKN', max_length=30, null=True)),
                ('tanggal_bkn', models.DateField(db_column='Tanggal_BKN', default='1900-01-01', max_length=14, null=True)),
                ('tmt_golongan', models.DateField(blank=True, db_column='TMT_Golongan', max_length=14, null=True)),
                ('jumlah_angka_kredit_utama', models.DecimalField(blank=True, db_column='Jumlah_Angka_Kredit_Utama', decimal_places=3, max_digits=8, null=True)),
                ('jumlah_angka_kredit_tambahan', models.DecimalField(blank=True, db_column='Jumlah_Angka_Kredit_Tambahan', decimal_places=3, max_digits=7, null=True)),
                ('mk_golongan_tahun', models.IntegerField(blank=True, db_column='MK_Golongan_Tahun', null=True)),
                ('mk_golongan_bulan', models.IntegerField(blank=True, db_column='MK_Golongan_Bulan', null=True)),
                ('dokumen', models.FileField(null=True, upload_to=pegawai.models._upload_path_kp, validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('nama', models.CharField(blank=True, db_column='Nama', max_length=255, null=True)),
            ],
            options={
                'db_table': 't_riwayat_golongan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_login', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TEselon',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=10)),
                ('keterangan', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 't_eselon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TJabatan',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama_jabatan', models.CharField(db_column='nama_Jabatan', max_length=139)),
                ('jenis_jabatan', models.CharField(max_length=27)),
                ('bup', models.IntegerField()),
                ('stastus', models.CharField(max_length=5)),
                ('id_eselon', models.ForeignKey(db_column='id_eselon', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.teselon')),
            ],
            options={
                'db_table': 't_jabatan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TJenisJabatan',
            fields=[
                ('id', models.CharField(db_column='JENIS_JABATAN_ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('jenis_jabatan_nama', models.CharField(db_column='JENIS_JABATAN_NAMA', max_length=30)),
            ],
            options={
                'db_table': 't_jenis_jabatan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TJenisPegawai',
            fields=[
                ('id', models.CharField(db_column='JENIS_PEGAWAI_ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('jenis_pegawai_nama', models.CharField(db_column='JENIS_PEGAWAI_NAMA', max_length=60)),
            ],
            options={
                'db_table': 'TJenisPegawai',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TKodeGolongan',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama_golongan', models.CharField(max_length=5)),
                ('nama_pangkat', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 't_kode_golongan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TLokasi',
            fields=[
                ('id', models.CharField(db_column='LOKASI_ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('kanreg_id', models.CharField(db_column='KANREG_ID', max_length=2)),
                ('nama', models.CharField(db_column='NAMA', max_length=50)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=10)),
                ('jenis', models.CharField(db_column='JENIS', max_length=3)),
                ('jenis_kabupaten', models.CharField(db_column='JENIS_KABUPATEN', max_length=25)),
                ('jenis_desa', models.CharField(db_column='JENIS_DESA', max_length=15)),
                ('ibukota', models.CharField(db_column='IBUKOTA', max_length=25)),
            ],
            options={
                'db_table': 'TLokasi',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TOpd',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama_unor', models.CharField(db_column='NAMA_UNOR', max_length=255, verbose_name='Instansi')),
                ('eselon_id', models.CharField(db_column='ESELON_ID', max_length=3)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=15)),
                ('nama_jabatan', models.CharField(db_column='NAMA_JABATAN', max_length=255)),
                ('diatasan_id', models.CharField(db_column='DIATASAN_ID', max_length=32)),
                ('instansi_id', models.CharField(db_column='INSTANSI_ID', max_length=32)),
                ('pemimpin_non_pns_id', models.CharField(db_column='PEMIMPIN_NON_PNS_ID', max_length=55)),
                ('pemimpin_pns_id', models.CharField(db_column='PEMIMPIN_PNS_ID', max_length=32)),
                ('jenis_unor_id', models.CharField(db_column='JENIS_UNOR_ID', max_length=32)),
                ('unor_induk', models.CharField(db_column='UNOR_INDUK', max_length=32)),
                ('jumlah_ideal_staff', models.CharField(db_column='JUMLAH_IDEAL_STAFF', max_length=3)),
            ],
            options={
                'db_table': 't_opd',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TPegawaiSapk',
            fields=[
                ('id', models.CharField(db_column='PNS_ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nip_baru', models.CharField(db_column='NIP_BARU', max_length=18)),
                ('nip_lama', models.CharField(blank=True, db_column='NIP_LAMA', max_length=9, null=True)),
                ('nama', models.CharField(blank=True, db_column='NAMA', max_length=50, null=True)),
                ('gelar_depan', models.CharField(blank=True, db_column='GELAR_DEPAN', max_length=5, null=True)),
                ('gelar_blk', models.CharField(blank=True, db_column='GELAR_BLK', max_length=20, null=True)),
                ('tgl_lhr', models.DateField(blank=True, db_column='TGL_LAHIR', max_length=10, null=True)),
                ('jenis_kelamin', models.CharField(blank=True, db_column='JENIS_KELAMIN', max_length=1, null=True)),
                ('nik', models.CharField(blank=True, db_column='NIK', max_length=30, null=True)),
                ('nomor_hp', models.CharField(blank=True, db_column='NOMOR_HP', max_length=40, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=50, null=True)),
                ('alamat', models.CharField(blank=True, db_column='ALAMAT', max_length=150, null=True)),
                ('npwp_nomor', models.CharField(blank=True, db_column='NPWP_NOMOR', max_length=30, null=True)),
                ('bpjs', models.CharField(blank=True, db_column='BPJS', max_length=50, null=True)),
                ('status_cpns_pns', models.CharField(db_column='STATUS_CPNS_PNS', max_length=1)),
                ('kartu_pegawai', models.CharField(blank=True, db_column='KARTU_PEGAWAI', max_length=30, null=True)),
                ('nomor_sk_cpns', models.CharField(blank=True, db_column='NOMOR_SK_CPNS', max_length=40, null=True)),
                ('tgl_sk_cpns', models.DateField(blank=True, db_column='TGL_SK_CPNS', max_length=10, null=True)),
                ('tmt_cpns', models.DateField(blank=True, db_column='TMT_CPNS', max_length=10, null=True)),
                ('nomor_sk_pns', models.CharField(blank=True, db_column='NOMOR_SK_PNS', max_length=50, null=True)),
                ('tgl_sk_pns', models.DateField(blank=True, db_column='TGL_SK_PNS', max_length=10, null=True)),
                ('tmt_pns', models.DateField(blank=True, db_column='TMT_PNS', max_length=10, null=True)),
                ('tmt_golongan', models.CharField(db_column='TMT_GOLONGAN', max_length=10)),
                ('mk_tahun', models.IntegerField(blank=True, db_column='MK_TAHUN', null=True)),
                ('mk_bulan', models.IntegerField(blank=True, db_column='MK_BULAN', null=True)),
                ('kpkn', models.CharField(db_column='KPKN_ID', max_length=32)),
                ('instansi_induk_nama', models.CharField(blank=True, db_column='INSTANSI_INDUK_NAMA', max_length=150, null=True)),
                ('instansi_kerja_nama', models.CharField(blank=True, db_column='INSTANSI_KERJA_NAMA', max_length=150, null=True)),
                ('satuan_kerja_induk_nama', models.CharField(blank=True, db_column='SATUAN_KERJA_INDUK_NAMA', max_length=150, null=True)),
                ('satuan_kerja_kerja_nama', models.CharField(blank=True, db_column='SATUAN_KERJA_KERJA_NAMA', max_length=150, null=True)),
                ('tmt_pensiun', models.DateField(blank=True, db_column='TMT_PENSIUN', null=True)),
                ('fhoto', models.ImageField(upload_to='media')),
                ('agama', models.ForeignKey(blank=True, max_length=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tkodeagama')),
                ('gol', models.ForeignKey(blank=True, max_length=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='GOL_ID', to='pegawai.tkodegolongan')),
                ('gol_awal', models.ForeignKey(blank=True, max_length=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tkodegolongan')),
                ('jabatan', models.ForeignKey(db_column='JABATAN_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tjabatan')),
                ('jenis_jabatan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tjenisjabatan')),
            ],
            options={
                'db_table': 't_pegawai_sapk',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TStatusKawin',
            fields=[
                ('id', models.CharField(db_column='JENIS_KAWIN_ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('jenis_kawin_nama', models.CharField(db_column='JENIS_KAWIN_NAMA', max_length=15)),
            ],
            options={
                'db_table': 'TStatusKawin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TStatusKedudukan',
            fields=[
                ('id', models.CharField(db_column='ID_STATUS_KEDUDUKAN', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama_status_kedudukan', models.CharField(db_column='NAMA_STATUS_KEDUDUKAN', max_length=100)),
            ],
            options={
                'db_table': 'TStatusKedudukan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TTingkatPendidikan',
            fields=[
                ('id', models.CharField(db_column='KODE', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='NAMA', max_length=25)),
                ('golongan_awal', models.CharField(db_column='GOLONGAN_AWAL', max_length=3)),
                ('golongan_akhir', models.CharField(db_column='GOLONGAN_AKHIR', max_length=3)),
            ],
            options={
                'db_table': 't_tingkat_pendidikan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TUnor',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('instansi_id', models.CharField(db_column='INSTANSI_ID', max_length=32)),
                ('diatasan_id', models.CharField(db_column='DIATASAN_ID', max_length=32)),
                ('eselon_id', models.CharField(db_column='ESELON_ID', max_length=3)),
                ('nama_unor', models.CharField(db_column='NAMA_UNOR', max_length=250)),
                ('nama_jabatan', models.CharField(blank=True, db_column='NAMA_JABATAN', max_length=250, null=True)),
                ('cepat_kode', models.CharField(blank=True, db_column='CEPAT_KODE', max_length=10, null=True)),
                ('jenis_unor_id', models.CharField(blank=True, db_column='JENIS_UNOR_ID', max_length=32, null=True)),
                ('nama_pejabat', models.CharField(blank=True, db_column='NAMA_PEJABAT', max_length=70, null=True)),
                ('unor_induk', models.CharField(blank=True, db_column='UNOR_INDUK_ID', max_length=32, null=True)),
                ('pemimpin_pns', models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tpegawaisapk')),
            ],
            options={
                'db_table': 'TUnor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TPendidikan',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=32, primary_key=True, serialize=False)),
                ('nama', models.CharField(db_column='NAMA', max_length=150)),
                ('cepat_kode', models.CharField(db_column='CEPAT_KODE', max_length=6)),
                ('tingkat_pendidikan', models.ForeignKey(max_length=3, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tpendidikan')),
            ],
            options={
                'db_table': 'TPendidikan',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='jenis_kawin',
            field=models.ForeignKey(blank=True, max_length=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tstatuskawin'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='jenis_pegawai',
            field=models.ForeignKey(blank=True, max_length=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tjenispegawai'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='kedudukan_hukum',
            field=models.ForeignKey(blank=True, max_length=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tstatuskedudukan'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='lokasi_kerja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='LOKASI_KERJA_ID', to='pegawai.tlokasi'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='pendidikan',
            field=models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tpendidikan'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='tempat_lahir',
            field=models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TEMPAT_LAHIR', to='pegawai.tlokasi'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='tingkat_pendidikan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.ttingkatpendidikan'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='unor',
            field=models.ForeignKey(max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UNOR_ID', to='pegawai.tunor'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='unor_induk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='UNOR_INDUK_ID', to='pegawai.topd'),
        ),
        migrations.AddField(
            model_name='tpegawaisapk',
            name='unor_induk_bkd',
            field=models.ForeignKey(blank=True, db_column='UNOR_INDUK_BKD', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.topd', verbose_name='Instansi'),
        ),
        migrations.AddField(
            model_name='topd',
            name='nama_pejabat',
            field=models.ForeignKey(db_column='NAMA_PEJABAT', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tpegawaisapk'),
        ),
        migrations.AddField(
            model_name='tjabatan',
            name='id_jenis_jabatan',
            field=models.ForeignKey(db_column='id_jenis_jabatan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pegawai.tjenisjabatan'),
        ),
        migrations.AddField(
            model_name='teselon',
            name='maxgol',
            field=models.ForeignKey(db_column='max_pangkat', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='maxgol', to='pegawai.tkodegolongan'),
        ),
        migrations.AddField(
            model_name='teselon',
            name='mingol',
            field=models.ForeignKey(db_column='min_pangkat', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mingol', to='pegawai.tkodegolongan'),
        ),
    ]