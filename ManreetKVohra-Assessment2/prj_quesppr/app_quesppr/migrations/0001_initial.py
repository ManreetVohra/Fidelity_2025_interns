# Generated by Django 5.1.6 on 2025-02-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('subcode', models.IntegerField(primary_key=True, serialize=False)),
                ('qno', models.IntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('question', models.IntegerField()),
            ],
        ),
    ]
