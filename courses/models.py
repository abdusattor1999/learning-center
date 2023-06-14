from django.db import models


BRANCH_CHOICES = (
    ('Chorsu filiali', 'Chosru filiali'),
    ("Do'stlik filiali", "Do'stlik filiali"),
    ('Lola filiali', 'Lola filiali'),
    ('Mikrorayon filiali', 'Mikrorayon filiali'),
    ('Toshbuloq filiali', 'Mikrorayon filiali'),
    ("To'raqo'rg'on filiali", "To'raqo'rg'on filiali"),
)

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Kategoriya nomi')

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='Kurs nomi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriyasi')
    image = models.ImageField(upload_to='courses/', verbose_name='Rasm')
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, verbose_name='Filial')
    description = models.TextField(verbose_name='Kurs haqida')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Narx')
    active = models.BooleanField(default=True, verbose_name='Aktiv')

    def __str__(self) -> str:
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name='Ism')
    surname = models.CharField(max_length=20, verbose_name='Familiya')
    image = models.ImageField(upload_to='teachers/', verbose_name='Rasm')
    about = models.TextField(verbose_name='Malumot')
    degree = models.CharField(verbose_name='Darajasi', max_length=50)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}".title()