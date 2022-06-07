# Generated by Django 4.0.4 on 2022-05-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_contactformsubmission_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Blog Title', max_length=100)),
                ('content', models.TextField()),
                ('slug', models.CharField(default=1, max_length=200)),
                ('image', models.ImageField(upload_to='media/projectImages/')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='projectSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(help_text='Skill Name', max_length=100)),
                ('projectName', models.CharField(help_text='Project Name', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Label',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='projectLabel',
        ),
        migrations.AlterField(
            model_name='contactformsubmission',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
