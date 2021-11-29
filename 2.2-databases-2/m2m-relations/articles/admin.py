from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main_tag = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main', False) and not form.cleaned_data['DELETE']:
                count_main_tag += 1
        if count_main_tag > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif count_main_tag == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class TagInLine(admin.TabularInline):
    model = Tag
    formset = TagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInLine]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
