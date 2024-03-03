from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Category


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_active'):
                count += 1
        if count == 0:
            raise ValidationError('Необходимо выбрать публикацию')
        if count > 1:
            raise ValidationError('Необходимо выбрать только одну публикацию')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

