from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Inscricao, Alternativa, Participante

class AlternativaAdmin(admin.TabularInline):
    model = Alternativa
    pass

@admin.register(Alternativa)
class AlternativaAdminImportExport(ImportExportModelAdmin):
    model = Alternativa
    list_display = ['titulo', 'inscricao', 'quantidade_maxima']
    pass


# Documentação: https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
@admin.register(Participante)
class ParticipanteAdmin(ImportExportModelAdmin):
    list_display = ['nome', 'turma', 'inscricao', 'alternativa', 'resposta']
    list_filter = ['turma', 'alternativa','inscricao']
    pass


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    list_display = ['titulo', 'id', 'inicio']

    fieldsets = [
        (None,               {'fields': ['id', 'titulo']}),
        ('Data das inscrições', {'fields': ['inicio']}),
        ('Extra', {'fields': ['resposta_textual']})
    ]
    inlines = [
        AlternativaAdmin,
    ]
