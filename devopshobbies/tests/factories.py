import factory

from devopshobbies.tests.utils import faker
from devopshobbies.users.models import (
        BaseUser,
        Profile,
        )
from devopshobbies.blog.models import (
        Subscription,
        Post,
        )
from django.utils import timezone


class BaseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseUser

    email    = factory.Iterator(['fr@gmail.com', 'it@gmail.com', 'es@gmail.com'])
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

class SubscriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subscription

    target        = factory.SubFactory(BaseUserFactory)
    subscriber    = factory.SubFactory(BaseUserFactory)

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post 

    title   = factory.LazyAttribute(lambda _: f'{faker.unique.company()}')
    content = factory.LazyAttribute(lambda _: f'{faker.unique.company()}')
    slug    = factory.LazyAttribute(lambda _: f'{faker.unique.company()}')
    created_at           = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    updated_at           = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    author = factory.SubFactory(BaseUserFactory)

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user                 = factory.SubFactory(BaseUserFactory)
    posts_count          = factory.LazyAttribute(lambda _: 0 )
    subscription_count  = factory.LazyAttribute(lambda _: 0 )
    subscriber_count    = factory.LazyAttribute(lambda _: 0 )
    bio                  = factory.LazyAttribute(lambda _: f'{faker.unique.company()}')
 
