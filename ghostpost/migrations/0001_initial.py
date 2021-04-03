# Generated by Django 3.1.7 on 2021-04-03 06:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('BO', 'Boast'), ('RO', 'Roast')], default='BO', max_length=2)),
                ('body', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
