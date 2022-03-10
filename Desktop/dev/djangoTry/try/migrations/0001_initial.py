# Generated by Django 4.0.3 on 2022-03-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, max_length=300, null=True, verbose_name='本文')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'タスク',
            },
        ),
    ]