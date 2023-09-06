from django.contrib import admin

from firstapp.models import Person, Company, OrderPosition, Order, Product


#                             7.6.2. Организация связей между таблицами "многие-ко-многим". Стр. 262 - 266.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_display_links = ['id', 'name', 'age']
    search_fields = ['name', 'age']
    list_filter = ['age', 'name', ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'company']
    list_display_links = ['id', 'name', 'price']
    search_fields = ['name', ]


class OrderPositionInLine(admin.TabularInline):
    """ Таблица, встраиваемая в отображение другой таблицы. """
    model = OrderPosition
    extra = 2


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'person', 'created_at', 'executed']
    list_display_links = ['id', 'number']  # Не могут быть, одновременно, редактируемыми.
    search_fields = ['number', 'created_at']
    list_filter = ('created_at', 'executed')
    list_editable = ('executed', )       # Поля, которые можно редактировать прямо в общем списке.
    inlines = [OrderPositionInLine, ]    # Добавляем встраиваемые данные (таблицу OrderPosition)

# admin.site.register(Order, OrderAdmin)    # Можно и так, вместо декоратора.
