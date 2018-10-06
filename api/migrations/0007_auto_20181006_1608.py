# Generated by Django 2.1.1 on 2018-10-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181003_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='animals',
            field=models.CharField(blank=True, choices=[('Chat', 'Chat'), ('Oiseaux', 'Oiseaux')], max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='color',
            field=models.CharField(blank=True, default='#FFF', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_post',
            field=models.CharField(blank=True, choices=[('Préposé entretien ménager', 'Préposé entretien ménager'), ('Superviseur', 'Superviseur'), ('Administrateur', 'Administrateur')], max_length=45),
        ),
        migrations.AddField(
            model_name='employee',
            name='hourly_salary',
            field=models.IntegerField(blank=True, default=50, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='login_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='pre_payment_method',
            field=models.CharField(blank=True, choices=[('Argent comptant', 'Argent comptant'), ('Chèque', 'Chèque'), ('Dépôt direct', 'Dépôt direct')], max_length=45),
        ),
        migrations.AddField(
            model_name='employee',
            name='remarks',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]