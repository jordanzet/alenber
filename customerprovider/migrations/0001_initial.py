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
            name='AddressCustomerProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'OFICINA_PRINCIPAL', help_text=b'Titulo de la Direccion', max_length=150, choices=[(b'OFICINA_PRINCIPAL', b'Oficina Principal'), (b'SUCURSAL', b'Sucursal'), (b'ALMACEN', b'Almacen'), (b'PLANTA', b'Planta')])),
                ('region', models.CharField(help_text=b'region', max_length=150)),
                ('provincia', models.CharField(help_text=b'provincia', max_length=150)),
                ('distrito', models.CharField(help_text=b'distrito', max_length=150)),
                ('direccion', models.CharField(help_text=b'Direccion de la Empresa', max_length=150)),
            ],
            options={
                'verbose_name': 'Direccion de la empresa proveedora',
                'verbose_name_plural': 'Direcciones de la empresa proveedora',
            },
        ),
        migrations.CreateModel(
            name='ContactCustomerProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Dato de Contacto de la empresa Provedora',
                'verbose_name_plural': 'Datos de Contacto de la empresa Provedora',
            },
        ),
        migrations.CreateModel(
            name='CustomerProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruc', models.BigIntegerField(help_text=b'Ingrese el numero de RUC', verbose_name=b'RUC de la empresa')),
                ('logo', models.ImageField(upload_to=b'customer_buy_logo/')),
                ('foto_institucional', models.ImageField(upload_to=b'customer_buy_foto_portada/')),
                ('razon_social', models.CharField(help_text=b'ingrese la razon social', max_length=150, verbose_name=b'Razon Social de la Empresa')),
                ('phone', models.IntegerField(help_text=b'Ingrese su Numero de Telefono', verbose_name=b'Telefono', blank=True)),
                ('cel', models.IntegerField(help_text=b'Ingrese su Numero de celular', verbose_name=b'Celular', blank=True)),
                ('inicio_de_actividades', models.DateField(help_text=b'Ingrese la fecha de inicio de actividades', verbose_name=b'Fecha de Inicio de Actividades')),
                ('numero_de_trabajadores', models.CharField(default=b'1 trabajador', max_length=250, choices=[(b'1t', b'1 trabajador'), (b'2a10t', b'2 a 10 trabajadores'), (b'11a100t', b'11 a 100 trabajadores'), (b'101a1000t', b'101 a 1000 trabajadores'), (b'1001a5000t', b'1001 a 5000 trabajadores'), (b'5000a+t', b'5000 a + trabajadores')])),
                ('website', models.URLField(help_text=b'Ingrese su sitio web', verbose_name=b'Sitio Web', blank=True)),
                ('email', models.EmailField(help_text=b'ingrese su email', max_length=254, blank=True)),
                ('sector', models.CharField(help_text=b'ingrese su sector', max_length=150, blank=True)),
                ('customer', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empresa Provedora',
                'verbose_name_plural': 'Empresas Provedoras',
            },
        ),
        migrations.CreateModel(
            name='ProductCustomerProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_product', models.CharField(max_length=250)),
                ('image_product', models.ImageField(upload_to=b'product_customer_buy/', blank=True)),
                ('customer_provider', models.ForeignKey(to='customerprovider.CustomerProvider')),
            ],
            options={
                'verbose_name': 'Producto de la empresa proveedora',
                'verbose_name_plural': 'Productos de la empresa proveedora',
            },
        ),
        migrations.CreateModel(
            name='TagProductCustomerProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('customer_provider', models.ForeignKey(to='customerprovider.CustomerProvider')),
            ],
            options={
                'verbose_name': 'Categoria de producto de la empresa proveedora',
                'verbose_name_plural': 'Categorias de los productos de la empresa proveedora',
            },
        ),
        migrations.AddField(
            model_name='productcustomerprovider',
            name='tag_product',
            field=models.ForeignKey(to='customerprovider.TagProductCustomerProvider'),
        ),
        migrations.AddField(
            model_name='contactcustomerprovider',
            name='customer_provider',
            field=models.ForeignKey(to='customerprovider.CustomerProvider'),
        ),
        migrations.AddField(
            model_name='addresscustomerprovider',
            name='customer_provider',
            field=models.ForeignKey(to='customerprovider.CustomerProvider'),
        ),
    ]
