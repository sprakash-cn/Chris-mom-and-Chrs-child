# Generated by Django 2.2.4 on 2020-12-01 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_userprofile_mentions'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mentions',
            field=models.CharField(max_length=100, null=True),
        ),
    ]