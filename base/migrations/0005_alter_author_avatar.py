# Generated by Django 4.1.7 on 2023-03-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='author_avatar.png', null=True, upload_to=''),
        ),
    ]
