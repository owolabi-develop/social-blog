# Generated by Django 4.1 on 2022-08-08 01:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_article_author_delete_article_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=255)),
                ('Article_pic', models.FileField(upload_to='Articles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'], message='Please Upload The Fellowing Image Format jpg ord png')], verbose_name='Article Pic')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'get_latest_by': ['pub_date', 'headlines'],
            },
        ),
        migrations.CreateModel(
            name='Article_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=255)),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='blog.article')),
            ],
            options={
                'get_latest_by': ['comment_date'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article_category'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]