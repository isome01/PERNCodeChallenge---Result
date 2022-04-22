import pytz
from datetime import datetime


def wrap_double_quotes(text=''):
    return f'"{text}"'


def wrap_single_quotes(text=''):
    return f"'{text}'"


def match_values_to_column_sequence(values, columns):
    """ Returns list of values in the order their corresponding columns
    :param values: dict() -> values to match
    :param columns: list() -> the columns that the values should be matched to
    :return: list()
    """
    seq = [values.get(c, None) for c in columns]
    return seq


def get_todays_date_iso_format():
    """Simple getter for today's date that returns a string
    :return: string -> string of datetime
    """
    tz = pytz.timezone('US/Central')
    todays_date = wrap_single_quotes(datetime.now(tz=tz).isoformat(sep=' '))

    return todays_date


def get_column_string(columns):
    """
    :param columns: a list of collective strings and dictionaries (name:alias) of column names
            to select from assumed table. A dictionary assumes aliases
            as a key values to overshadow provided column names upon return.
    :return: String
    """
    col_str = ''
    if columns and type(columns) is list:
        for c in columns:
            if type(c) is dict:
                for name, alias in c.items():
                    col_str = f"{col_str}{',' if col_str else ''}{name} AS {alias}"
            else:
                col_str = f"{col_str}{',' if col_str else ''}{c}"

    else:
        print(f'Columns not of type list; defaulting to "*"')
        col_str = '*'

    return col_str


def build_values(values):
    """
        :param values: list of dicts: values
        :return: string
        """
    # assert any values that have nothing
    values = [(v if v else 'null') for v in values]
    values_string = get_column_string(values)
    return f'({values_string})'

