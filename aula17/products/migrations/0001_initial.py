# Generated by Django 5.0.4 on 2024-04-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=20)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ptucdo',
                'verbose_name_plural': 'cenas',
            },
        ),
    ]