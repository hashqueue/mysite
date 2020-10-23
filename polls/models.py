import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题描述', help_text='问题描述')
    pub_date = models.DateTimeField(verbose_name='发布时间', help_text='发布时间')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='所属问题', help_text='所属问题')
    # 每个 Choice 对象都关联到一个 Question 对象，属于多对一关系
    choice_text = models.CharField(max_length=200, verbose_name='选项描述', help_text='选项描述')
    votes = models.IntegerField(default=0, verbose_name='当前得票数', help_text='当前得票数')

    def __str__(self):
        return self.choice_text
