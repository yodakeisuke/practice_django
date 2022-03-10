from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=30)
    content = models.TextField(verbose_name="本文",max_length=300, blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = ("タスク")

    def __str__(self):
        return self.title
