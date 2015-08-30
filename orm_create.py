import utils

from django.utils import timezone

from app import models


def orm_create(n_records):
    for i in xrange(0, n_records):
        models.TestModel.objects.create(
            field_1=i,
            field_2=str(i),
            field_3=timezone.now(),
        )


if __name__ == '__main__':
    utils.timed(orm_create)
