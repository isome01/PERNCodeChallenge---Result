from server.config.driver import postgres, map_postgres_response
from common.movies.columns import default_movie_columns
import json


def load_runtime_to_json(results):
    if type(results) == 'list':
        results = [{**r, 'runtime': json.loads(r['runtime'])} for r in results]
    elif type(results) == 'dict':
        results = {**results, 'runtime': json.loads(results['runtime'])}

    return results


def list_all():
    client = postgres()
    results = []
    try:
        with client() as db:
            prep = db.prepare(f"""SELECT * FROM pcc_movies;""")
            results = prep()

    except Exception as e:
        print(f'Error: {e}')

    return map_postgres_response(
        columns=default_movie_columns,
        values=results
    )


def get_by_id(movie_id):
    client = postgres()
    results = []
    try:
        with client() as db:
            prep = db.prepare(f"""SELECT * FROM pcc_movies WHERE movie_id={movie_id};""")
            results = prep()

    except Exception as e:
        print(f'Error: {e}')

    results = map_postgres_response(
        columns=default_movie_columns,
        values=results
    )
    return load_runtime_to_json(results)


def create(columns, values):
    client = postgres()
    results = []
    try:
        with client() as db:
            print(f"""
                INSERT INTO pcc_movies({columns})
                VALUES {values}
                returning movie_id;
            """)
            prep = db.prepare(f"""
                INSERT INTO pcc_movies({columns})
                VALUES {values}
                returning movie_id;
            """)
            results = prep()

    except Exception as e:
        print(f'Error: {e}')

    return results
