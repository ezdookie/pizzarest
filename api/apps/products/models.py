from django.db import models

PIZZA_SIZES = (
    ('personal', 'Personal'),
    ('large', 'Large'),
    ('familiar', 'Familiar'),
)


class PizzaModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pizza'


class PizzaVariantModel(models.Model):
    pizza = models.ForeignKey(PizzaModel, related_name='variants', on_delete=models.DO_NOTHING)
    size = models.CharField(choices=PIZZA_SIZES, max_length=10)

    class Meta:
        db_table = 'pizza_variant'
        unique_together = ['pizza', 'size']
