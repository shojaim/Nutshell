# Generated by Django 4.2.2 on 2023-06-15 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutshell.city', verbose_name='شهر')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='تعداد')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutshell.inventory', verbose_name='انبار')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('quantity', models.PositiveIntegerField(verbose_name='مقدار هر بسته به گرم')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutshell.category', verbose_name='دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='تعداد')),
                ('status', models.CharField(choices=[('ثبت شد', 'ثبت شد'), ('آماده ارسال', 'آماده ارسال')], default='ثبت شد', max_length=20, verbose_name='وضعیت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutshell.inventoryproduct', verbose_name='محصول')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='سفارش دهنده')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryproduct',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutshell.product', verbose_name='نام'),
        ),
    ]
