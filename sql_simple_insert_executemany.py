import utils

from contextlib import closing

from django.db import connection
from django.utils import timezone


def sql_simple_insert_executemany(n_records):
    with closing(connection.cursor()) as cursor:
        cursor.executemany(
            'INSERT INTO app_testmodel (field_1, field_2, field_3)'
            'VALUES (%s, %s, %s)',
            [(i, str(i), timezone.now()) for i in xrange(0, n_records)],
        )


if __name__ == '__main__':
    utils.timed(sql_simple_insert_executemany)
