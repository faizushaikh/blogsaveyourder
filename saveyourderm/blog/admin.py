from django.contrib import admin
from .models import Blogs_Category,Blogs_Post


class Blogs_CategoryAdmin(admin.ModelAdmin):
    list_display=('title','description','url','image_show','add_dates')
    search_fields=('title',)
    
        


class Blogs_PostAdmin(admin.ModelAdmin):
    list_display=('post_id','title','content','url','category','image_show','videos','add_dates')
    search_fields=('title',)
    list_filter=('category',)   
    list_per_page=50




admin.site.register(Blogs_Category,Blogs_CategoryAdmin)  
admin.site.register(Blogs_Post,Blogs_PostAdmin)