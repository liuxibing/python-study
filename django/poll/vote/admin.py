from django.contrib import admin

# 注册Vote应用的模型，并添加到后台管理中，by ainoob.cn
from vote.models import Subject, Teacher

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'create_date', 'is_hot')
    ordering = ('no', )

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'good_count', 'bad_count', 'subject')
    ordering = ('subject', 'no')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)