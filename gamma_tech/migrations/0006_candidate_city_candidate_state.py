# Generated by Django 4.0.2 on 2022-04-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamma_tech', '0005_alter_candidate_cur_sal_alter_candidate_exp_sal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='city',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='state',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
