# Generated by Django 4.2 on 2023-05-29 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EscaneoQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket')),
            ],
        ),
    ]
