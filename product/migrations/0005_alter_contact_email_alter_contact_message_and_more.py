# Generated by Django 5.1.6 on 2025-02-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
