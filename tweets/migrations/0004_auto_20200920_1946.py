# Generated by Django 2.2 on 2020-09-20 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0003_tweet_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_user', through='tweets.TweetLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
