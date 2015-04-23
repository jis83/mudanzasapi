# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campos_user',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('telefonos', models.CharField(max_length=200)),
                ('fotos', models.CharField(max_length=200)),
                ('horario_de_contacto', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200)),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('valor', models.FloatField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitud_Envio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('origen', models.CharField(max_length=200)),
                ('destino', models.CharField(max_length=200)),
                ('fecha_limite', models.DateTimeField(verbose_name='date published')),
                ('desc_objetos', models.CharField(max_length=200)),
                ('desc_lugar', models.CharField(max_length=200)),
                ('escalera', models.CharField(max_length=200)),
                ('ascensor', models.CharField(max_length=200)),
                ('tipo_aviso', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='solicitud_envio',
            field=models.ForeignKey(to='mudanzaapiapp.Solicitud_Envio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
