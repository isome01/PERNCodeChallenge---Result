import os
import postgresql.driver as pqsl_driver


def map_postgres_response(columns, values):
    """ This function maps a postgres response (which is usually a Tuple) to
        a CSV, or default dict/JSON
    :param columns: type list
    :param values: type list of tuples
    :return: list()
    """
    mapped_values = list()

    for data in values:
        cols_len = len(columns)
        obj = {}
        for index in range(0, cols_len, 1):
            obj[columns[index]] = data[index]
        mapped_values.append(obj)

    return mapped_values


def postgres():
    """Driver for PostgreSQL in the nature it is"""
    try:
        hostname = os.getenv('DB_HOST')
        psql_port = 5432
        psql_config = pqsl_driver.default.host(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=hostname,
            port=psql_port,
            database='postgres',
            sslmode='prefer'
        )
        driver = psql_config
        print(f'Set up postres driver with specs:\n - host:{hostname}\n - port:{psql_port}')
    except Exception as e:
        print('Unable to set host options', e)
        raise AssertionError
    print(f'postres-driver specs:\n - host:{hostname}\n - port:{psql_port}')
    return driver
