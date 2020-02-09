from django.contrib import admin

# Register your models here.
from .models import Grades,Students
class GradesAdmin(admin.ModelAdmin):
#列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

# 添加，修改页属性
    fields = ['ggirlnum','gboynum','gname','gdate','isDelete'] # 这俩不能同时用要注释掉一个
    # fieldsets = [
    #     ("num",{"fields":['ggirlnum','gboynum']})
    #     ("base",{"fields":['gname','gdate','idDelete']})
    # ]
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # 设置页面列的名称
    gender.short_description = "性别"
    list_display = ['pk','sname','sage',gender,'scontent','sgrade','isDelete']
    list_per_page = 2
    # 执行动作的位置
    # actions_on_top = True
    # actions_on_bottom = False
admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)
# 注册
