"""
Django command for waiting for database to avaliable
"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django command for wait for database
    """

    def handle(self, *args, **options):
        """Entrypoint for Database"""
        self.stdout.write("Waiting for Database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError,OperationalError):
                self.stdout.write("Retry to connect db, in 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is avaliable and connected"))
