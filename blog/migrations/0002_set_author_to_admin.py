from django.db import migrations


def set_author_to_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    BlogPost = apps.get_model('blog', 'BlogPost')
    try:
        admin_user = User.objects.get(username='djangoadmin')
    except User.DoesNotExist:
        admin_user = User.objects.filter(is_superuser=True).first()
    if admin_user:
        BlogPost.objects.all().update(author=admin_user)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_author_to_admin, reverse_code=migrations.RunPython.noop),
    ]
