# books/management/commands/load_authors.py
import json
from django.core.management.base import BaseCommand
from books.models import Author

class Command(BaseCommand):
    help = 'Load authors from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data['root']:
                Author.objects.create(
                    name=item['name'],
                    # Aggiungi altri campi necessari
                )
        self.stdout.write(self.style.SUCCESS('Authors loaded successfully'))
