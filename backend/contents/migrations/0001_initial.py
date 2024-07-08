# Generated by Django 4.2.11 on 2024-05-02 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=191)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(null=True)),
                ('slug', models.CharField(db_index=True, max_length=255)),
                ('content', models.TextField()),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=191)),
                ('email', models.CharField(db_index=True, max_length=191, null=True)),
                ('subject', models.CharField(db_index=True, max_length=191, null=True)),
                ('message', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=255, null=True)),
                ('name', models.CharField(db_index=True, max_length=191)),
                ('email', models.CharField(db_index=True, max_length=191)),
                ('phone', models.CharField(db_index=True, max_length=191)),
                ('address', models.TextField()),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(db_index=True, max_length=191)),
                ('answer', models.TextField()),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'faqs',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=191)),
                ('description', models.TextField(null=True)),
                ('project_date', models.DateField(db_index=True, null=True)),
                ('project_url', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contents.customer')),
            ],
            options={
                'db_table': 'portfolios',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(db_index=True, max_length=191)),
                ('name', models.CharField(db_index=True, max_length=191)),
                ('description', models.TextField(null=True)),
                ('type', models.IntegerField(db_index=True, default=0)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'references',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(db_index=True, max_length=191, null=True)),
                ('title', models.CharField(db_index=True, max_length=191)),
                ('description', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=255, null=True)),
                ('title', models.CharField(db_index=True, max_length=191)),
                ('description', models.TextField(null=True)),
                ('link', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'sliders',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=255, null=True)),
                ('name', models.CharField(db_index=True, max_length=191)),
                ('email', models.CharField(db_index=True, max_length=191)),
                ('phone', models.CharField(db_index=True, max_length=191)),
                ('position_name', models.CharField(db_index=True, max_length=191)),
                ('twitter', models.CharField(db_index=True, max_length=255, null=True)),
                ('facebook', models.CharField(db_index=True, max_length=255, null=True)),
                ('instagram', models.CharField(db_index=True, max_length=255, null=True)),
                ('linked_in', models.CharField(db_index=True, max_length=255, null=True)),
                ('address', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=255, null=True)),
                ('gender', models.CharField(db_index=True, max_length=2, null=True)),
                ('country', models.CharField(db_index=True, max_length=191, null=True)),
                ('address', models.TextField(null=True)),
                ('about_me', models.TextField(null=True)),
                ('reset_token', models.CharField(db_index=True, max_length=191, null=True)),
                ('confirm_token', models.CharField(db_index=True, max_length=191, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_user_details',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=255, null=True)),
                ('name', models.CharField(db_index=True, max_length=191)),
                ('position', models.CharField(db_index=True, max_length=191)),
                ('quote', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contents.customer')),
            ],
            options={
                'db_table': 'testimonials',
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(db_index=True, max_length=191)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contents.portfolio')),
            ],
            options={
                'db_table': 'portfolios_images',
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contents.reference'),
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('status', models.SmallIntegerField(db_index=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contents.article')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contents.articlecomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'articles_comments',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='references',
            field=models.ManyToManyField(to='contents.reference'),
        ),
    ]