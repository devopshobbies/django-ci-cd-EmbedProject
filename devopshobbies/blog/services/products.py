from django.db.models import QuerySet
from devopshobbies.blog.models import Product


def create_product(name: str) -> QuerySet[Product]:
    return Product.objects.create(name=name)
