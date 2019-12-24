from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    salary = models.FloatField(verbose_name='Ставка в час')
    technical_duties = models.TextField(verbose_name='Технические обязанности')
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name

class Staff(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, verbose_name='Отчество')
    table_number = models.PositiveIntegerField(verbose_name='Табельный номер')
    telephone_number = models.CharField(max_length=12, verbose_name='Телефонный номер')
    pasport_data = models.TextField(verbose_name='Паспортные данные')
    height = models.PositiveIntegerField(verbose_name='Рост')
    clothing_size = models.CharField(max_length=2, verbose_name='Размер одежды')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Должность')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    active = models.BooleanField(default=True)

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.get_full_name()

class Realization(models.Model):
    check_number = models.PositiveIntegerField(unique=True, verbose_name='Номер чека')
    service = models.ForeignKey('Service', on_delete=models.CASCADE, blank=True, null=True, verbose_name='')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Сотрудник')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата')
    comment = models.CharField(max_length=50,verbose_name='Замечания')

    class Meta:
        verbose_name = 'Реализация'
        verbose_name_plural = 'Реализации'

    def __str__(self):
        return f"{self.check_number}"
    
class Service(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class CategoryName(models.Model):
    name = models.CharField(max_length=11, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Названия категорий'

    def __str__(self):
        return self.name

class Category(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Рецептура')
    description = models.TextField(verbose_name='Описание')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Услуга')
    count = models.PositiveIntegerField(verbose_name='Количество')
    name = models.ForeignKey(CategoryName, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name.name
    
class Recipe(models.Model):
    #product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Продукт')
    #product = models.ManyToManyField('Product', blank=True, null=True, verbose_name='Продукт')
    name = models.CharField(max_length=25, verbose_name='Название рецептуры')
    description = models.TextField(verbose_name='Описание')
    volume = models.ForeignKey("RecipeCount", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Объем')
    product_count = models.ManyToManyField('ProductCount', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Рецептура'
        verbose_name_plural = 'Рецептуры'

    def __str__(self):
        return self.name

class RecipeCount(models.Model):
    volume = models.FloatField(verbose_name='Объем')

    class Meta:
        verbose_name = 'Объем рецептуры'
        verbose_name_plural = 'Объем рецептур'

    def __str__(self):
        return str(self.volume)

class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')
    expiration_date = models.CharField(max_length=11, verbose_name='Срок годности')
    price = models.FloatField(verbose_name='Цена')
    count = models.FloatField(verbose_name='Количество')
    dealer = models.ForeignKey("Dealer",on_delete=models.CASCADE, blank=True, null=True, verbose_name='Поставщик')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class ProductCount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Продукт')
    count = models.FloatField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Количество продукта'
        verbose_name_plural = 'Количество продуктов'

    def __str__(self):
        return str(self.count)

class Dealer(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')
    l_address = models.TextField(verbose_name='Юридический адрес')
    p_address = models.TextField(verbose_name='Физический адрес')
    telephone_number = models.CharField(max_length=12, verbose_name='Телефонный номер')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name