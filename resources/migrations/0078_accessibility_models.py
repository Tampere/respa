# Generated by Django 2.1.7 on 2019-06-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0077_resource_slot_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessibilityValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=128, unique=True, verbose_name='Accessibility summary value')),
                ('order', models.IntegerField(default=0, verbose_name='Ordering priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Lisäysaika')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Muokkausaika')),
            ],
            options={
                'verbose_name': 'accessibility value',
                'verbose_name_plural': 'accessibility values',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='AccessibilityViewpoint',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nimi')),
                ('name_fi', models.CharField(max_length=200, null=True, verbose_name='Nimi')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Nimi')),
                ('name_sv', models.CharField(max_length=200, null=True, verbose_name='Nimi')),
                ('order_text', models.CharField(default='0', max_length=200, verbose_name='Tilaus')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Lisäysaika')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Muokkausaika')),
            ],
            options={
                'verbose_name': 'accessibility viewpoint',
                'verbose_name_plural': 'accessibility viewpoints',
                'ordering': ('order_text',),
            },
        ),
        migrations.CreateModel(
            name='ResourceAccessibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Resource ordering priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Lisäysaika')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Muokkausaika')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessibility_summaries', to='resources.Resource', verbose_name='Resurssi')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.AccessibilityValue', verbose_name='Accessibility summary value')),
                ('viewpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_accessibility_summaries', to='resources.AccessibilityViewpoint', verbose_name='Resource Accessibility')),
            ],
            options={
                'verbose_name': 'resource accessibility summary',
                'verbose_name_plural': 'resource accessibility summaries',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='UnitAccessibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Resource ordering priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Lisäysaika')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Muokkausaika')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessibility_summaries', to='resources.Unit', verbose_name='Resurssi')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.AccessibilityValue', verbose_name='Accessibility summary value')),
                ('viewpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_accessibility_summaries', to='resources.AccessibilityViewpoint', verbose_name='Resource Accessibility')),
            ],
            options={
                'verbose_name': 'unit accessibility summary',
                'verbose_name_plural': 'unit accessibility summaries',
                'ordering': ('id',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='unitaccessibility',
            unique_together={('viewpoint', 'unit')},
        ),
        migrations.AlterUniqueTogether(
            name='resourceaccessibility',
            unique_together={('viewpoint', 'resource')},
        ),
    ]