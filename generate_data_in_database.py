import utils

from contextlib import closing

from django.db import connection


def generate_data_in_database(n_records):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """
            INSERT INTO app_testmodel (field_1, field_2, field_3)
            SELECT
                i,
                i::text,
                now()
            FROM
                generate_series(0, %s - 1) AS s(i)
            """,
            (n_records,),
        )


if __name__ == '__main__':
    utils.timed(generate_data_in_database)
