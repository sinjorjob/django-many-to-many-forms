from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):

    class Meta:
        verbose_name = "メンバー情報"
        verbose_name_plural = "メンバー情報"

    user = models.ForeignKey(User, verbose_name="管理者名", on_delete=models.CASCADE)
    member_name = models.CharField(verbose_name="メンバの氏名",max_length=100)
    email = models.EmailField(verbose_name="メンバーのアドレス")
 
    def __str__(self):
        return '%s' % (self.member_name)


class Agenda(models.Model):

    class Meta:
        verbose_name = "会議情報"
        verbose_name_plural = "会議情報"
        
    title = models.CharField(verbose_name="タイトル",max_length=255)
    contents = models.TextField(verbose_name="内容")
    date = models.DateField(verbose_name="開催日時")
    members = models.ManyToManyField(Member,verbose_name="参加メンバー")

