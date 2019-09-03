from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        #对应数据库模型指定为Comment类
        model = Comment
        #指定需要显示的字段
        fields = ["name", "email", "url", "text"]
