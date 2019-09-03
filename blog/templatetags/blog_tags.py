from ..models import Post, Category
from django import template

# 最新模板标签代码
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-created_time")[:num]


# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates("created_time", "month", order="DESC")


# dates返回文章创建时间

# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()
