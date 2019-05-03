from django import forms
# 引入模型
from .models import Tag,Student

# 写表单类
class TagForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Tag
        # 定义表单包含的字段
        fields = ('tname', 'tcolor')

# class SelectForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('sgrade', 'smajor', 'sbanji')