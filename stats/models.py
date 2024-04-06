from django.db import models


class AbstractBaseModel(models.Model):
    id = models.IntegerField(primary_key=True)

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        """Get model field names.

        Returns:
            list[str]: list of model fieldnames.
        """
        return [field.name.capitalize() for field in cls._meta.fields]

    class Meta:
        abstract = True


class Circuit(AbstractBaseModel):
    short_name = models.CharField(max_length=128)
    official_name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.SmallIntegerField(blank=True)
    url = models.URLField(max_length=256)

    def __str__(self) -> str:
        return f"{self.short_name}"


class Race(AbstractBaseModel):
    circuit = models.ForeignKey(
        Circuit, on_delete=models.PROTECT, related_name="races"
    )
    circuit_name = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    race_number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=256)
    date = models.DateField()
    wikiurl = models.URLField(max_length=256)

    def __str__(self) -> str:
        return f"{self.circuit_name} {self.year}"
