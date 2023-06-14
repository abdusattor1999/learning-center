# Generated by Django 4.1 on 2023-06-14 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Kategoriya nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Ism')),
                ('surname', models.CharField(max_length=20, verbose_name='Familiya')),
                ('image', models.ImageField(upload_to='teachers/', verbose_name='Rasm')),
                ('about', models.TextField(verbose_name='Malumot')),
                ('degree', models.CharField(max_length=50, verbose_name='Darajasi')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Kurs nomi')),
                ('image', models.ImageField(upload_to='courses/', verbose_name='Rasm')),
                ('branch', models.CharField(choices=[('Chorsu filiali', 'Chosru filiali'), ("Do'stlik filiali", "Do'stlik filiali"), ('Lola filiali', 'Lola filiali'), ('Mikrorayon filiali', 'Mikrorayon filiali'), ('Toshbuloq filiali', 'Mikrorayon filiali'), ("To'raqo'rg'on filiali", "To'raqo'rg'on filiali")], max_length=50, verbose_name='Filial')),
                ('description', models.TextField(verbose_name='Kurs haqida')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Narx')),
                ('active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category', verbose_name='Kategoriyasi')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.teacher')),
            ],
        ),
    ]
