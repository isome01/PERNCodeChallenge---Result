from common.tools import get_column_string, get_todays_date_iso_format, match_values_to_column_sequence, \
    build_values, wrap_single_quotes
from common.movies.columns import default_movie_columns, movie_columns_wo_id
from server.model.movies import create


def add_new_movie(data):
    columns = movie_columns_wo_id

    data['avg_rating'] = wrap_single_quotes(data['avg_rating'])
    data['description'] = wrap_single_quotes(data['description'])
    data['title'] = wrap_single_quotes(data['title'])
    data['rating_classification'] = wrap_single_quotes(data['rating_classification'])
    data['release_date'] = wrap_single_quotes(data['release_date'])
    data['runtime'] = wrap_single_quotes(data['runtime'])

    values = match_values_to_column_sequence(
        values={
            **data,
            'created': get_todays_date_iso_format(),
            'updated_at': get_todays_date_iso_format(),
        },
        columns=columns
    )

    return create(values=build_values(values), columns=get_column_string(columns))
