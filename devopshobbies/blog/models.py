from django.db import models
from devopshobbies.common.models import BaseModel


class Product(BaseModel):
    name = models.TextField(max_length=255)
