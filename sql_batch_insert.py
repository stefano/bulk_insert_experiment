import utils

from contextlib import closing

from django.db import connection
from django.utils import timezone


def sql_batch_insert(n_records):
    sql = 'INSERT INTO app_testmodel (field_1, field_2, field_3) VALUES {}'.format(
        ', '.join(['(%s, %s, %s)'] * n_records),
    )
    params = []
    for i in xrange(0, n_records):
        params.extend([i, str(i), timezone.now()])

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, params)


if __name__ == '__main__':
    utils.timed(sql_batch_insert)
