from datetime import timedelta


def add_gigasecond(birth_date):
    return birth_date + timedelta(seconds=1_000_000_000)
