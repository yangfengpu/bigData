# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducocoNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('showName', models.CharField(max_length=100)),
                ('nodeType', models.CharField(max_length=100)),
                ('uriDomain', models.CharField(max_length=300)),
                ('uriIdentifier', models.CharField(unique=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EducocoTriplePattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=240, db_index=True)),
                ('valueDescr', models.CharField(max_length=240, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='LiteralType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lType', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TripleContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='keyval',
            name='container',
            field=models.ForeignKey(to='cococloud.TripleContext'),
        ),
        migrations.AddField(
            model_name='educocotriplepattern',
            name='context',
            field=models.ForeignKey(related_name='triple_context', to='cococloud.TripleContext'),
        ),
        migrations.AddField(
            model_name='educocotriplepattern',
            name='predicate',
            field=models.ForeignKey(related_name='triple_predicate', to='cococloud.EducocoNode'),
        ),
        migrations.AddField(
            model_name='educocotriplepattern',
            name='subject',
            field=models.ForeignKey(related_name='triple_object', to='cococloud.EducocoNode'),
        ),
        migrations.AddField(
            model_name='educoconode',
            name='literalType',
            field=models.ForeignKey(to='cococloud.LiteralType'),
        ),
        migrations.AddField(
            model_name='educoconode',
            name='tag',
            field=models.ManyToManyField(related_name='vocabulary_tag', to='cococloud.Tag', db_index=True),
        ),
    ]
