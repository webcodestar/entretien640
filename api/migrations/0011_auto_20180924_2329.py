# Generated by Django 2.1.1 on 2018-09-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180924_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='customer_type',
            field=models.CharField(blank=True, choices=[('Résidentiel', 'Residential'), ('Commercial', 'Commercial'), ('Occasionnel', 'Occasionnel')], max_length=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='frequency',
            field=models.CharField(blank=True, choices=[('1x semaine', '1x semaine'), ('2x semaine', '2x semaine'), ('1x 2 semaines', '1x 2 semaines'), ('1x 3 semaines', '1x 3 semaines'), ('1x 4 semaines', '1x 4 semaines')], max_length=15),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='stage',
            field=models.CharField(choices=[('Nouveau', 'Nouveau'), ('Appel manqué #1', 'Appel manqué #1'), ('Appel manqué #2', 'Appel manqué #2'), ('Soumission RDV', 'Soumission RDV'), ('Soumission envoyée', 'Soumission envoyée'), ('Non intéressé', 'Non intéressé'), ('En attente', 'En attente'), ('Nouveau client', 'Nouveau client')], max_length=15),
        ),
    ]