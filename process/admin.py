from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *

admin.site.register(Candidate)
admin.site.register(Technology)
admin.site.register(Attempts)
admin.site.register(Result)

class QuestionsResource(resources.ModelResource):

    class Meta:
        model = Questions
        fields = ('question',
                'answer',
                'difficulty',
                'technology',
                'id',
                )
        
        import_id_fields = (
                'question',
                'answer',
                'difficulty',
                'technology')

class QuestionsAdmin(ImportExportModelAdmin):
    resource_class = QuestionsResource



admin.site.register(Questions, QuestionsAdmin)