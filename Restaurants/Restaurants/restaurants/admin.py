from django.contrib import admin
from .models import Restaurant, Category

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pub_date', 'update_date', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'pub_date', 'id', 'update_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'describtion')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Category, CategoryAdmin)
