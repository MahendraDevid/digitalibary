# Generated by Django 4.2 on 2024-02-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.AutoField(db_column='UserID', primary_key=True, serialize=False),
        ),
    ]
