# Generated by Django 5.0.2 on 2024-03-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.AutoField(db_column='UserID', primary_key=True, serialize=False),
        ),
    ]