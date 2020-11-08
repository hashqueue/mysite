from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    # 指定显示在修改页面上的字段
    list_display = ['title', 'status']
    # 设置排序的字段。
    ordering = ['title']
    # admin提供了自定义功能函数actions
    actions = ['make_published']

    # 第一个参数变为self
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request,
                          ngettext('{}个故事已被成功标记为published.',
                                   '{}个故事已被成功标记为published.',
                                   updated).format(updated),
                          messages.SUCCESS)

    # admin页面上action的描述展示
    make_published.short_description = "将所选故事标记为已发布"


admin.site.register(Article, ArticleAdmin)
