import factory

class ProductFactory(factory.Factory):
    class Meta:
        model = dict
    id = factory.Sequence(lambda n: n+1)
    name = factory.Faker("word")
    category = factory.Iterator(["toys", "electronics", "books"])
    available = factory.Iterator([True, False])
