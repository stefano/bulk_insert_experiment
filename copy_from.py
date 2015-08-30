import utils

from contextlib import closing
import csv
from cStringIO import StringIO

from django.db import connection
from django.utils import timezone


def copy_from(n_records):
    stream = StringIO()
    writer = csv.writer(stream, delimiter='\t')

    for i in xrange(0, n_records):
        writer.writerow([i, str(i), timezone.now().isoformat()])

    stream.seek(0)

    with closing(connection.cursor()) as cursor:
        cursor.copy_from(
            file=stream,
            table='app_testmodel',
            sep='\t',
            columns=('field_1', 'field_2', 'field_3'),
        )


if __name__ == '__main__':
    utils.timed(copy_from)
