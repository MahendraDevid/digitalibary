# Generated by Django 5.0.2 on 2024-03-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(db_column='UserID', max_length=10, primary_key=True, serialize=False),
        ),
    ]
