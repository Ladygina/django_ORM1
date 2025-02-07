import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('D:\pycharm\ORM1\databases\work_with_database\phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            phone_curr = Phone(id=phone['id'][:50],
                               name=phone['name'][:50],
                               price=phone['price'][:50],
                               image=phone['image'][:50],
                               release_date = phone['release_date'][:50],
                               lte_exists = phone['lte_exists'][:50],
                               slug=slugify(phone['name'][:50]))
            phone_curr.save()


