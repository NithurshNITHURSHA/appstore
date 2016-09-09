# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-09 18:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.CharField(help_text='app id, identical to folder name', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('user_docs', models.URLField(blank=True, max_length=256, verbose_name='User documentation url')),
                ('admin_docs', models.URLField(blank=True, max_length=256, verbose_name='Admin documentation url')),
                ('developer_docs', models.URLField(blank=True, max_length=256, verbose_name='Developer documentation url')),
                ('issue_tracker', models.URLField(blank=True, max_length=256, verbose_name='Issue tracker url')),
                ('website', models.URLField(blank=True, max_length=256, verbose_name='Homepage')),
                ('discussion', models.URLField(blank=True, max_length=256, verbose_name='Discussion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
                ('rating_recent', models.FloatField(default=0.5, verbose_name='Recent rating')),
                ('rating_overall', models.FloatField(default=0.5, verbose_name='Overall rating')),
                ('last_release', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Last release at')),
                ('certificate', models.TextField(verbose_name='Certificate')),
            ],
            options={
                'verbose_name_plural': 'Apps',
                'verbose_name': 'App',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AppAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Full name')),
                ('homepage', models.URLField(blank=True, max_length=256, verbose_name='Homepage')),
                ('mail', models.EmailField(blank=True, max_length=256, verbose_name='E-Mail')),
            ],
            options={
                'verbose_name_plural': 'App authors',
                'verbose_name': 'App author',
            },
        ),
        migrations.CreateModel(
            name='AppRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.5, help_text='Rating from 0.0 (worst) to 1.0 (best)', verbose_name='Rating')),
                ('rated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.App', verbose_name='App')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_ratings', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'App ratings',
                'verbose_name': 'App rating',
                'ordering': ('-rated_at',),
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AppRatingTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('comment', models.TextField(blank=True, default='', help_text='Rating comment in Markdown', verbose_name='Rating comment')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.AppRating')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'db_table': 'core_apprating_translation',
                'verbose_name': 'App rating Translation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AppRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(help_text='Version follows Semantic Versioning', max_length=256, verbose_name='Version')),
                ('php_version_spec', models.CharField(max_length=256, verbose_name='PHP version requirement')),
                ('platform_version_spec', models.CharField(max_length=256, verbose_name='Platform version requirement')),
                ('raw_php_version_spec', models.CharField(max_length=256, verbose_name='PHP version requirement (raw)')),
                ('raw_platform_version_spec', models.CharField(max_length=256, verbose_name='Platform version requirement (raw)')),
                ('min_int_size', models.IntegerField(blank=True, default=32, help_text='e.g. 32 for 32bit Integers', verbose_name='Minimum integer bits')),
                ('download', models.URLField(blank=True, max_length=256, verbose_name='Archive download Url')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
                ('signature', models.TextField(help_text="A signature using SHA512 and the app's certificate", verbose_name='Signature')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='core.App', verbose_name='App')),
            ],
            options={
                'verbose_name_plural': 'App releases',
                'verbose_name': 'App release',
                'ordering': ['-version'],
            },
        ),
        migrations.CreateModel(
            name='AppTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='Rendered app name for users', max_length=256, verbose_name='Name')),
                ('summary', models.CharField(help_text="Short text describing the app's purpose", max_length=256, verbose_name='Summary')),
                ('description', models.TextField(help_text='Will be rendered as Markdown', verbose_name='Description')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.App')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'db_table': 'core_app_translation',
                'verbose_name': 'App Translation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(help_text='Category id which is used to identify a category. Used to identify categories when uploading an app', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
                'ordering': ['id'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='Category name which will be presented to the user', max_length=256, verbose_name='Name')),
                ('description', models.TextField(help_text='Will be rendered as Markdown', verbose_name='Description')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.Category')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'db_table': 'core_category_translation',
                'verbose_name': 'Category Translation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.CharField(help_text='Key which is used to identify a database', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='Database name which will be presented to the user', max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Databases',
                'verbose_name': 'Database',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DatabaseDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_spec', models.CharField(max_length=256, verbose_name='Database version requirement')),
                ('raw_version_spec', models.CharField(max_length=256, verbose_name='Database version requirement (raw)')),
                ('app_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='databasedependencies', to='core.AppRelease', verbose_name='App release')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releasedependencies', to='core.Database', verbose_name='Database')),
            ],
            options={
                'verbose_name_plural': 'Database dependencies',
                'verbose_name': 'Database dependency',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.CharField(help_text='Key which is used to identify a license', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='License name which will be presented to the user', max_length=256, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Licenses',
                'verbose_name': 'License',
            },
        ),
        migrations.CreateModel(
            name='PhpExtension',
            fields=[
                ('id', models.CharField(help_text='e.g. libxml', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='PHP extension')),
            ],
            options={
                'verbose_name_plural': 'PHP extensions',
                'verbose_name': 'PHP extension',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PhpExtensionDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_spec', models.CharField(max_length=256, verbose_name='Extension version requirement')),
                ('raw_version_spec', models.CharField(max_length=256, verbose_name='Extension version requirement (raw)')),
                ('app_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phpextensiondependencies', to='core.AppRelease', verbose_name='App release')),
                ('php_extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releasedependencies', to='core.PhpExtension', verbose_name='PHP extension')),
            ],
            options={
                'verbose_name_plural': 'PHP extension dependencies',
                'verbose_name': 'PHP extension dependency',
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=256, verbose_name='Image url')),
                ('ordering', models.IntegerField(verbose_name='Ordering')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='core.App', verbose_name='App')),
            ],
            options={
                'verbose_name_plural': 'Screenshots',
                'verbose_name': 'Screenshot',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='ShellCommand',
            fields=[
                ('name', models.CharField(help_text='Name of a required shell command, e.g. grep', max_length=256, primary_key=True, serialize=False, unique=True, verbose_name='Shell command')),
            ],
            options={
                'verbose_name_plural': 'Shell commands',
                'verbose_name': 'Shell command',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='apprelease',
            name='databases',
            field=models.ManyToManyField(blank=True, through='core.DatabaseDependency', to='core.Database', verbose_name='Database dependency'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='licenses',
            field=models.ManyToManyField(to='core.License', verbose_name='License'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='php_extensions',
            field=models.ManyToManyField(blank=True, through='core.PhpExtensionDependency', to='core.PhpExtension', verbose_name='PHP extension dependency'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='shell_commands',
            field=models.ManyToManyField(blank=True, to='core.ShellCommand', verbose_name='Shell command dependency'),
        ),
        migrations.AddField(
            model_name='app',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='apps', to='core.AppAuthor', verbose_name='App authors'),
        ),
        migrations.AddField(
            model_name='app',
            name='categories',
            field=models.ManyToManyField(to='core.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='app',
            name='co_maintainers',
            field=models.ManyToManyField(blank=True, related_name='co_maintained_apps', to=settings.AUTH_USER_MODEL, verbose_name='Co-Maintainers'),
        ),
        migrations.AddField(
            model_name='app',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_apps', to=settings.AUTH_USER_MODEL, verbose_name='App owner'),
        ),
        migrations.AlterUniqueTogether(
            name='phpextensiondependency',
            unique_together=set([('app_release', 'php_extension', 'version_spec')]),
        ),
        migrations.AlterUniqueTogether(
            name='databasedependency',
            unique_together=set([('app_release', 'database', 'version_spec')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='apptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='apprelease',
            unique_together=set([('app', 'version')]),
        ),
        migrations.AlterUniqueTogether(
            name='appratingtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='apprating',
            unique_together=set([('app', 'user')]),
        ),
    ]
