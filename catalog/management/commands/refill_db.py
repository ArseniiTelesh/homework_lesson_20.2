import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")

        Category.objects.all().delete()
        Product.objects.all().delete()

        with open("catalog_data.json", encoding="utf-8") as json_file:
            data = json.load(json_file)

            product_for_create = []
            category_for_create = []

            for category in data:
                if category["model"] == "catalog.category":
                    category_for_create.append(
                        Category(
                            name=category["fields"]["name"],
                            description=category["fields"]["description"],
                        )
                    )
            Category.objects.bulk_create(category_for_create)
            for product in data:
                if product["model"] == "catalog.product":
                    product_for_create.append(
                        Product(
                            name=product["fields"]["name"],
                            description=product["fields"]["description"],
                            category=Category.objects.get(
                                pk=product["fields"]["category"]
                            ),
                            price=product["fields"]["price"],
                            created_at=product["fields"]["created_at"],
                            updated_at=product["fields"]["updated_at"],
                        )
                    )

            Product.objects.bulk_create(product_for_create)
