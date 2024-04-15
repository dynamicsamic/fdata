from django.db.models import Count

from .models import Circuit


def get_circuits():
    return Circuit.objects.annotate(num_races=Count("races")).order_by(
        "-num_races"
    )
