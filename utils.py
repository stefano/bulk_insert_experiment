import os
import time

import django
from django.db.transaction import atomic

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from app import models


def timed(fn):
    n_records = 10000

    start = time.time()
    with atomic():
        fn(n_records)
    end = time.time()

    count = models.TestModel.objects.count()
    models.TestModel.objects.all().delete()
    assert count == n_records

    print 'Created {} records in {}ms'.format(
        n_records,
        int((end - start) * 1000),
    )
