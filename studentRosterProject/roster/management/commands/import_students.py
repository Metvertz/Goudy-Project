import csv
from django.core.management.base import BaseCommand
from roster.models import StudentWorker

class Command(BaseCommand):
    help = 'Import student workers from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import.')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                _, created = StudentWorker.objects.get_or_create(
                    name=row[0],
                    email=row[1]
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added student worker {row[0]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Student worker {row[0]} already exists'))
