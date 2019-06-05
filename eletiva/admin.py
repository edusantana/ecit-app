from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin

# Register your models here.
from .models import EletivaConfiguracao, Eletiva, Aluno


class EletivaAdmin(admin.TabularInline):
    model = Eletiva
    pass


# Documentação: https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    list_display = ['nome', 'turma', 'configuracao', 'eletiva']
    list_filter = ['turma', 'eletiva','configuracao']
    pass


@admin.register(EletivaConfiguracao)
class EletivaConfiguracaoAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    list_display = ['id', 'periodo', 'inicio_selecao']

    fieldsets = [
        (None,               {'fields': ['id', 'periodo']}),
        ('Data das inscrições', {'fields': ['inicio_selecao']}),
        ('Configuração', {
            'classes': 'wide',
            'fields': ['quantidade_maxima']}
        ),
    ]
    inlines = [
        EletivaAdmin,
    ]
