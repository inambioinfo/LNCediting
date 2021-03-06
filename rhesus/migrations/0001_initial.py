# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='edit_sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wild_sequence', models.TextField(null=True)),
                ('wild_energy', models.FloatField(null=True)),
                ('edit_squence', models.TextField(null=True)),
                ('edit_energy', models.FloatField(null=True)),
                ('delta_energy', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='edit_site_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chromosome', models.CharField(max_length=45, null=True)),
                ('chr_edit_pos', models.BigIntegerField(null=True)),
                ('trans_edit_pos', models.BigIntegerField(null=True)),
                ('lncrna_id', models.CharField(max_length=225, null=True)),
                ('resource', models.CharField(max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='function_gains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mirna_id', models.CharField(max_length=225, null=True)),
                ('chromosome', models.CharField(max_length=20, null=True)),
                ('chr_edit_pos', models.BigIntegerField(null=True)),
                ('lncrna_id', models.CharField(max_length=225, null=True)),
                ('resource', models.CharField(max_length=200, null=True)),
                ('score', models.FloatField(null=True)),
                ('energy', models.FloatField(null=True)),
                ('targetscan_start_r', models.BigIntegerField(null=True)),
                ('targetscan_end_r', models.BigIntegerField(null=True)),
                ('miranda_start_r', models.BigIntegerField(null=True)),
                ('miranda_end_r', models.BigIntegerField(null=True)),
                ('ref_edit_pos', models.IntegerField(null=True)),
                ('en', models.FloatField(null=True)),
                ('query_start', models.IntegerField(null=True)),
                ('query_end', models.IntegerField(null=True)),
                ('ref_start', models.IntegerField(null=True)),
                ('ref_end', models.IntegerField(null=True)),
                ('align_length', models.IntegerField(null=True)),
                ('query_percentage', models.FloatField(null=True)),
                ('ref_percentage', models.FloatField(null=True)),
                ('query_match_sequence', models.CharField(max_length=225, null=True)),
                ('match_string', models.CharField(max_length=225, null=True)),
                ('ref_match_sequence', models.CharField(max_length=225, null=True)),
                ('edit_site_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.edit_site_info')),
            ],
        ),
        migrations.CreateModel(
            name='function_losses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mirna_id', models.CharField(max_length=225, null=True)),
                ('chromosome', models.CharField(max_length=20, null=True)),
                ('chr_edit_pos', models.BigIntegerField(null=True)),
                ('lncrna_id', models.CharField(max_length=225, null=True)),
                ('resource', models.CharField(max_length=200, null=True)),
                ('score', models.FloatField(null=True)),
                ('energy', models.FloatField(null=True)),
                ('targetscan_start_r', models.BigIntegerField(null=True)),
                ('targetscan_end_r', models.BigIntegerField(null=True)),
                ('miranda_start_r', models.BigIntegerField(null=True)),
                ('miranda_end_r', models.BigIntegerField(null=True)),
                ('ref_edit_pos', models.IntegerField(null=True)),
                ('en', models.FloatField(null=True)),
                ('query_start', models.IntegerField(null=True)),
                ('query_end', models.IntegerField(null=True)),
                ('ref_start', models.IntegerField(null=True)),
                ('ref_end', models.IntegerField(null=True)),
                ('align_length', models.IntegerField(null=True)),
                ('query_percentage', models.FloatField(null=True)),
                ('ref_percentage', models.FloatField(null=True)),
                ('query_match_sequence', models.CharField(max_length=225, null=True)),
                ('match_string', models.CharField(max_length=225, null=True)),
                ('ref_match_sequence', models.CharField(max_length=225, null=True)),
                ('edit_site_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.edit_site_info')),
            ],
        ),
        migrations.CreateModel(
            name='lncrna_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lncrna_id', models.CharField(max_length=225, null=True)),
                ('combined_resource', models.CharField(max_length=225, null=True)),
                ('strand', models.CharField(max_length=4, null=True)),
                ('annotation_by_RADAR', models.CharField(max_length=225, null=True)),
                ('chromosome', models.CharField(max_length=45, null=True)),
                ('trans_start', models.BigIntegerField(null=True)),
                ('trans_end', models.BigIntegerField(null=True)),
                ('exons_count', models.IntegerField(null=True)),
                ('exons_start', models.TextField(null=True)),
                ('exons_end', models.TextField(null=True)),
                ('wild_sequence', models.TextField(null=True)),
                ('wild_energy', models.FloatField(null=True)),
                ('edit_sequence', models.TextField(null=True)),
                ('edit_energy', models.FloatField(null=True)),
                ('delta_energy', models.FloatField(null=True)),
                ('edit_num', models.IntegerField(null=True)),
                ('gain_num', models.IntegerField(null=True)),
                ('loss_num', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mirna_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mirna_id', models.CharField(max_length=225)),
                ('accession', models.CharField(max_length=225)),
                ('chromosome', models.CharField(max_length=45)),
                ('strand', models.CharField(max_length=4)),
                ('start', models.BigIntegerField()),
                ('end', models.BigIntegerField()),
                ('mature_sequence', models.CharField(max_length=500)),
                ('pre_mirna_id', models.CharField(max_length=45)),
                ('pre_start', models.BigIntegerField()),
                ('pre_end', models.BigIntegerField()),
                ('pre_sequence', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lncrna_name', models.CharField(max_length=45, null=True)),
                ('resource', models.CharField(max_length=45, null=True)),
                ('description', models.TextField(null=True)),
                ('link', models.TextField(null=True)),
                ('lncrna_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.lncrna_info')),
            ],
        ),
        migrations.AddField(
            model_name='function_losses',
            name='mirna_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.mirna_info'),
        ),
        migrations.AddField(
            model_name='function_gains',
            name='mirna_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.mirna_info'),
        ),
        migrations.AddField(
            model_name='edit_site_info',
            name='lncrna_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.lncrna_info'),
        ),
        migrations.AddField(
            model_name='edit_sequence',
            name='edit_site_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhesus.edit_site_info'),
        ),
    ]
