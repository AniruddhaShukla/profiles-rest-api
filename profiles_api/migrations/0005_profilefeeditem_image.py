# Generated by Django 2.2 on 2022-02-20 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_taskitem_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefeeditem',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
