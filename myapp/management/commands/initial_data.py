# myapp/management/commands/initial_data.py
from django.core.management.base import BaseCommand
from myapp.models import Category, Tag

class Command(BaseCommand):
    help = 'Populate initial data for the application'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating initial data...'))

        # Create categories
        categories = ['Technology', 'Science', 'Travel', 'Food']
        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS('Categories created successfully.'))

        # Create tags
        tags = ['Python', 'Django', 'Machine Learning', 'Adventure', 'Cuisine']
        for tag_name in tags:
            Tag.objects.create(name=tag_name)

        self.stdout.write(self.style.SUCCESS('Tags created successfully.'))

        self.stdout.write(self.style.SUCCESS('Initial data populated successfully.'))