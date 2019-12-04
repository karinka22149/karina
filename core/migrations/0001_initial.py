# Generated by Django 2.2.7 on 2019-11-27 07:47

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
            name='CategoryName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Название категории',
                'verbose_name_plural': 'Названия категорий',
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Наименование')),
                ('l_address', models.TextField(verbose_name='Юридический адрес')),
                ('p_address', models.TextField(verbose_name='Физический адрес')),
                ('telephone_number', models.CharField(max_length=12, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('salary', models.FloatField(verbose_name='Ставка в час')),
                ('technical_duties', models.TextField(verbose_name='Технические обязанности')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Наименование')),
                ('expiration_date', models.CharField(max_length=11, verbose_name='Срок годности')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('count', models.FloatField(verbose_name='Количество')),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Dealer', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='Количество')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Количество продукта',
                'verbose_name_plural': 'Количество продуктов',
            },
        ),
        migrations.CreateModel(
            name='RecipeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(verbose_name='Объем')),
            ],
            options={
                'verbose_name': 'Объем рецептуры',
                'verbose_name_plural': 'Объем рецептур',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=20, verbose_name='Отчество')),
                ('table_number', models.PositiveIntegerField(verbose_name='Табельный номер')),
                ('telephone_number', models.CharField(max_length=12, verbose_name='Телефонный номер')),
                ('pasport_data', models.TextField(verbose_name='Паспортные данные')),
                ('height', models.PositiveIntegerField(verbose_name='Рост')),
                ('clothing_size', models.CharField(max_length=2, verbose_name='Размер одежды')),
                ('active', models.BooleanField(default=True)),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Position', verbose_name='Должность')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название рецептуры')),
                ('description', models.TextField(verbose_name='Описание')),
                ('product_count', models.ManyToManyField(to='core.ProductCount', verbose_name='Продукт')),
                ('volume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.RecipeCount', verbose_name='Объем')),
            ],
            options={
                'verbose_name': 'Рецептура',
                'verbose_name_plural': 'Рецептуры',
            },
        ),
        migrations.CreateModel(
            name='Realization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_number', models.PositiveIntegerField(unique=True, verbose_name='Номер чека')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата')),
                ('comment', models.TextField(verbose_name='Замечания')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Service', verbose_name='Услуга')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Staff', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Реализация',
                'verbose_name_plural': 'Реализации',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.CategoryName', verbose_name='Название категории')),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Recipe', verbose_name='Рецептура')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
