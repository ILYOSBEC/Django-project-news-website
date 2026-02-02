from django.contrib import admin
from .models import News , Category , Contact
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug' , 'status','published_time')
    list_filter = ('status','created_time' , 'published_time')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'published_time'
    search_fields = ('title','content')
    ordering = ( 'status' ,'published_time',)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Category, CategoryAdmin)


admin.site.register(Contact)

