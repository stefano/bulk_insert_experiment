import utils

from django.utils import timezone

from app import models


def orm_bulk_create(n_records):
    instances = [
        models.TestModel(
            field_1=i,
            field_2=str(i),
            field_3=timezone.now(),
        )
        for i in xrange(0, n_records)
    ]

    models.TestModel.objects.bulk_create(instances)


if __name__ == '__main__':
    utils.timed(orm_bulk_create)
