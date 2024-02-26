from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
            email='1',
            first_name='1',
            last_name='1',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('1')
        user.save()