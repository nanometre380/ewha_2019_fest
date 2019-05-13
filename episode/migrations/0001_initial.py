# Generated by Django 2.2.1 on 2019-05-13 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_contents', models.CharField(max_length=400)),
                ('dropdown', models.CharField(max_length=10)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='episode.Board')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]