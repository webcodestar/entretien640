# Generated by Django 2.1.1 on 2018-09-27 07:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_admin', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Admin User',
                'verbose_name_plural': 'Admin User',
            },
            bases=('users.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('customer_type', models.CharField(blank=True, choices=[('Résidentiel', 'Residential'), ('Commercial', 'Commercial'), ('Occasionnel', 'Occasionnel')], max_length=15)),
                ('is_admin', models.BooleanField(default=False)),
                ('frequency', models.CharField(blank=True, choices=[('1x semaine', '1x semaine'), ('2x semaine', '2x semaine'), ('1x 2 semaines', '1x 2 semaines'), ('1x 3 semaines', '1x 3 semaines'), ('1x 4 semaines', '1x 4 semaines')], max_length=15)),
                ('profit_month', models.IntegerField(blank=True, null=True)),
                ('login_email', models.EmailField(blank=True, max_length=100)),
                ('estimated_time', models.CharField(blank=True, choices=[('1 heure et demi', '1 heure et demi'), ('2 heures', '2 heures'), ('2 heures et demi', '2 heures et demi'), ('3 heures', '3 heures'), ('3 heures et demi', '3 heures et demi'), ('4 heures', '4 heures'), ('4 heures et demi', '4 heures et demi'), ('5 heures', '5 heures'), ('5 heures et demi', '5 heures et demi'), ('6 heures', '6 heures'), ('6 heures et demi', '6 heures et demi'), ('7 heures', '7 heures'), ('7 heures et demi', '7 heures et demi'), ('8 heures', '8 heures'), ('8 heures et demi', '8 heures et demi'), ('9 heures', '9 heures'), ('9 heures et demi', '9 heures et demi'), ('10 heures', '10 heures')], max_length=15)),
                ('replacement', models.CharField(blank=True, choices=[('Reporté le ménage', 'Reporté le ménage'), ('Envoyé un remplaçant', 'Envoyé un remplaçant')], max_length=30)),
                ('days', models.CharField(blank=True, choices=[('Lun', 'Lun'), ('Mar', 'Mar'), ('Mer', 'Mer'), ('Jeu', 'Jeu'), ('Ven', 'Ven'), ('Sam', 'Sam'), ('Dim', 'Dim')], max_length=5)),
                ('code_key', models.IntegerField(blank=True, null=True)),
                ('animals', models.CharField(blank=True, max_length=100)),
                ('payment', models.CharField(blank=True, choices=[('Virement Interac', 'Virement Interac'), ('Argent comptant', 'Argent comptant'), ('Dépôt direct', 'Dépôt direct'), ('Chèque', 'Chèque'), ('Carte de crédit', 'Carte de crédit')], max_length=30)),
                ('remarks', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Client',
            },
            bases=('users.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_admin', models.BooleanField(default=False)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('Supervisor', models.CharField(blank=True, max_length=100)),
                ('note', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
                'ordering': ('id',),
            },
            bases=('users.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('last_contact', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(max_length=20)),
                ('stage', models.CharField(choices=[('Nouveau', 'Nouveau'), ('Appel manqué #1', 'Appel manqué #1'), ('Appel manqué #2', 'Appel manqué #2'), ('Soumission RDV', 'Soumission RDV'), ('Soumission envoyée', 'Soumission envoyée'), ('Non intéressé', 'Non intéressé'), ('En attente', 'En attente'), ('Nouveau client', 'Nouveau client')], max_length=15)),
            ],
            options={
                'verbose_name': 'Prospects',
                'verbose_name_plural': 'Prospects',
            },
            bases=('users.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='assign_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Employee'),
        ),
    ]
