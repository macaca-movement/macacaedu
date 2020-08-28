from django.core.management import BaseCommand
from mover.models import Mover


class Command(BaseCommand):
    def handle(self, *args, **options):
        u, _ = Mover.objects.get_or_create(username='test')
        u.set_password('test')
        u.is_staff = True
        u.is_superuser = True
        u.save()
