# Generated by Django 3.1.7 on 2021-04-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0003_auto_20210403_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
