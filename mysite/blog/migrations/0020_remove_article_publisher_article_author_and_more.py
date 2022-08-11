# Generated by Django 4.1 on 2022-08-10 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_article_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publisher',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article_category'),
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
