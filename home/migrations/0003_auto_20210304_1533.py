# Generated by Django 3.1.7 on 2021-03-04 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('title', models.CharField(max_length=100, null=True)),
                ('prodID', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('price', models.FloatField(null=True)),
                ('prodName', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('H', 'Household'), ('S', 'Snacks'), ('GR', 'Groceries'), ('GA', 'Games'), ('T', 'Toys'), ('OD', 'Outdoors')], max_length=2)),
                ('quantity', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('date_created', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Welcome!', max_length=100),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_id', models.CharField(max_length=12)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_click_purchasing', models.BooleanField(default=False, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('street_address', models.CharField(max_length=100, null=True)),
                ('apartment_address', models.CharField(max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100, null=True)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1, null=True)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='ProductOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('ordered_date', models.DateTimeField(null=True)),
                ('ordered', models.BooleanField(default=False, null=True)),
                ('products', models.ManyToManyField(to='home.ProductList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='productlist',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.products'),
        ),
    ]
