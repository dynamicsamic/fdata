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

    def _str(self, s: str) -> str:
        return f"{self.__class__.__name__}({s})"


class Circuit(AbstractBaseModel):
    short_name = models.CharField(max_length=128)
    official_name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.SmallIntegerField(blank=True)
    url = models.URLField()

    def __str__(self) -> str:
        return self._str(self.short_name)


class Driver(AbstractBaseModel):
    short_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=256)
    url = models.URLField()

    def __str__(self) -> str:
        return self._str(f"{self.first_name} {self.last_name}")


class Constructor(AbstractBaseModel):
    short_name = models.CharField(max_length=256)
    name = models.CharField(max_length=500)
    nationality = models.CharField(max_length=256)
    url = models.URLField()

    def __str__(self) -> str:
        return self._str(self.short_name)


class ResultSatus(AbstractBaseModel):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self._str(self.name)


class Race(AbstractBaseModel):
    circuit = models.ForeignKey(
        Circuit, on_delete=models.PROTECT, related_name="races"
    )
    year = models.PositiveSmallIntegerField()
    round = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=256)
    date = models.DateField()
    url = models.URLField()

    def __str__(self) -> str:
        return self._str(f"{self.name}, {self.year}")


class DriverStanding(AbstractBaseModel):
    race = models.ForeignKey(
        Race, on_delete=models.PROTECT, related_name="driver_standings"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, related_name="standings"
    )
    points = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()
    wins = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self._str(
            f"Race:{self.race_id}, Driver:{self.driver_id}, "
            f"Pos:{self.position}, Points:{self.points}"
        )


class ConstructorStanding(AbstractBaseModel):
    race = models.ForeignKey(
        Race, on_delete=models.PROTECT, related_name="constr_standings"
    )
    constructor = models.ForeignKey(
        Constructor, on_delete=models.PROTECT, related_name="standings"
    )
    points = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()
    wins = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self._str(
            f"Race:{self.race_id}, Driver:{self.constructor_id}, "
            f"Pos:{self.position}, Points:{self.points}"
        )


class Result(AbstractBaseModel):
    race = models.ForeignKey(
        Race, on_delete=models.PROTECT, related_name="results"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, related_name="race_results"
    )
    constructor = models.ForeignKey(
        Constructor, on_delete=models.PROTECT, related_name="race_results"
    )
    grid_position = models.ForeignKey(
        DriverStanding, on_delete=models.PROTECT, related_name="race_results"
    )
    status = models.ForeignKey(
        ResultSatus, on_delete=models.PROTECT, related_name="race_results"
    )
    car_number = models.PositiveSmallIntegerField()
    final_position = models.PositiveSmallIntegerField()
    points = models.PositiveSmallIntegerField()
    laps = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self._str(
            f"Race:{self.race_id}, Driver:{self.driver_id} "
            f"Constructor:{self.constructor_id}, Status:{self.status_id}"
            f"Position:{self.final_position}, Points:{self.points}"
            f"Laps:{self.laps}"
        )


class Qualifying(AbstractBaseModel):
    race = models.ForeignKey(
        Race, on_delete=models.PROTECT, related_name="qualifyings"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, related_name="qualifyings"
    )
    constructor = models.ForeignKey(
        Constructor, on_delete=models.PROTECT, related_name="qualifyings"
    )
    car_number = models.PositiveSmallIntegerField()
    position = models.PositiveSmallIntegerField()
    q1 = models.TimeField(null=True)
    q2 = models.TimeField(null=True)
    q3 = models.TimeField(null=True)

    def __str__(self) -> str:
        return self._str(
            f"Race:{self.race_id}, Driver:{self.driver_id}, "
            f"Costructor:{self.constructor_id}, Pos:{self.position}, "
            f"Time:{self.q3 or self.q2 or self.q1}"
        )


class LapTime(AbstractBaseModel):
    race = models.ForeignKey(
        Race, on_delete=models.PROTECT, related_name="lap_times"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, related_name="lap_times"
    )
    lap = models.PositiveSmallIntegerField()
    position = models.PositiveIntegerField()
    time = models.TimeField()
    time_ms = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self._str(
            f"Race:{self.race_id}, Driver:{self.driver_id}, Time:{self.time}, "
            f"Lap no:{self.lap_no}, Pos:{self.position}"
        )


class PitStopTime(AbstractBaseModel):
    race = models.ForeignKey(
        Race, on_delete=models.PROTECT, related_name="pitstop_times"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, related_name="pitstop_times"
    )
    stop_number = models.PositiveSmallIntegerField()
    lap = models.PositiveSmallIntegerField()
    time = models.TimeField()
    duration = models.FloatField()
    duration_ms = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self._str(
            f"Race:{self.race_id}, Driver:{self.driver_id}, Lap:{self.lap}, "
            f"Stop no:{self.stop_number}, Duration:{self.duration}"
        )
