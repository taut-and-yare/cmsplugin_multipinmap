# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-19 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_multipinmap_map', serialize=False, to='cms.CMSPlugin')),
                ('style', models.CharField(choices=[('google', 'Google Maps'), ('leaflet', 'Leaflet')], default='leaflet', max_length=25, verbose_name='style')),
                ('leaflet_tile_url', models.CharField(default='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', max_length=255, verbose_name='tile url')),
                ('height', models.IntegerField(default=400, help_text='height of the map in px.', verbose_name='height')),
                ('zoom', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21')], default=8, verbose_name='zoom')),
                ('street', models.CharField(blank=True, help_text='address for center of map', max_length=100, null=True, verbose_name='street')),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True, verbose_name='lat')),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True, verbose_name='lng')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='street')),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('link', models.URLField(blank=True, null=True, verbose_name='link')),
                ('link_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='link title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('pin_color', models.CharField(choices=[('redIcon', 'red'), ('blueIcon', 'blue'), ('greenIcon', 'green'), ('yellowIcon', 'yellow')], max_length=20)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True, verbose_name='lat')),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True, verbose_name='lng')),
                ('map_plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to='cmsplugin_multipinmap.Map')),
            ],
        ),
    ]