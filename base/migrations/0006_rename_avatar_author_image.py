# Generated by Django 4.1.7 on 2023-03-23 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_author_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='avatar',
            new_name='image',
        ),
    ]