from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name='Электрогенераторы', description='устройство, в котором неэлектрические виды энергии (механическая, химическая, тепловая и т. д.) преобразуются в электрическую энергию.')

        products = [
            {'name': 'Huter DY3000LX', 'price': '28658',
             'description': 'Портативный бензиновый электрогенератор Huter DY3000LX', 'category': category},
            {'name': 'LDG 13000LXА Huter', 'price': '180538',
             'description': 'Электрогенератор дизельный LDG 13000LXА Huter', 'category': category},
            {'name': 'Huter DY6500LXG', 'price': '74738',
             'description': 'Мультитопливный генератор Huter DY6500LXG', 'category': category},
            {'name': 'Huter DN4400i', 'price': '42218',
             'description': 'Инверторный электрогенератор Huter DN4400i', 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))