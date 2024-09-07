# Generated by Django 5.0.3 on 2024-09-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_rename_posts_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='post_author',
            new_name='review_author',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='post_date',
            new_name='review_date',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='post_name',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='post_status',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='post_type',
        ),
        migrations.AddField(
            model_name='reviews',
            name='book_id',
            field=models.CharField(default='default_book_id', max_length=300),
        ),
        migrations.AddField(
            model_name='reviews',
            name='review_comment',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]
