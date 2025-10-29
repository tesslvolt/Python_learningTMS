from django.contrib import admin
import openpyxl
import datetime
from io import BytesIO
from django.http import HttpResponse
from .models import Product, Category


# Register your models here.

@admin.action(description="Загрузить в Excel")
def download_to_excel(modeladmin, request, queryset):
    """
    создание файла excel.
    """
    wb = openpyxl.Workbook() # создаёт новый Excel-файл
    ws = wb.active # активный лист
    ws.title = f"Products {datetime.date.today().strftime('%Y-%m-%d')}" # название

    ws.append(['ID', 'Название', 'Описание', 'Цена', 'В наличии', 'Категория'])

    for product in queryset:
        ws.append([
            product.id,
            product.name,
            product.description,
            product.price,
            "Да" if product.in_stock else "Нет",
            product.category.name if product.category else "Без категории"
        ])

    output = BytesIO()
    wb.save(output)
    output.seek(0)

    # Формируем HTTP-ответ
    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=products_{datetime.date.today().strftime('%Y-%m-%d')}.xlsx'
    return response


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [download_to_excel]
    list_display = ('name', 'price', 'category', 'in_stock')
    list_filter = ('in_stock', 'category')
    search_fields = ('name','category__name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)