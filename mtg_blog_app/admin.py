from django.contrib import admin
from . import models

class CommentInLine(admin.TabularInline):
    model = models.Comment
    fields = ('name', 'email', 'text', 'approved')
    readonly_fields = ('name', 'email', 'text')    
    extra = 0
    
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated'
    )
    
    list_filter = (
        'status',
        'topics',
    )
    
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
        
    )
    
    prepopulated_fields = {
        'slug': ('title',)
    }
    
    inlines = [CommentInLine]

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {
        'slug': ('name',)
        }

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'post',
        'approved',
        'created',      
    )
    list_filter = ('approved', 'created', 'updated')
    search_fields = ('name', 'email', 'text')