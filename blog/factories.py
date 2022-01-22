import factory
from django.contrib.auth import get_user_model
from faker import Factory as FakerFactory
from django.utils.timezone import now
from blog.models import Post
faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    email = factory.Faker('safe_email')
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_at = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0

    class Meta:
        model = Post
